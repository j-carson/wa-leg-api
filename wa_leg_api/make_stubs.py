"""
Generates python stubs from the Washington State Legislature Schema XML Responses
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import Dict, Tuple

SERVICES = [
    "Amendment",
    "CommitteeMeeting",
    "CommitteeAction",
    "Committee",
    "Legislation",
    "LegislativeDocument",
    "RcwCiteAffected",
    "SessionLaw",
    "Sponsor",
]


def snake_case(identifier: str) -> str:
    """Make a JavaScript identifier into a Python one

    Parameters
    ----------
    identifier: str
        Javascript identifier in CapitalSnakeCase or lowerSnakeCase

    Returns
    -------
    pythid: str
        Python-standard identifier in snake_case
    """
    pythid = re.sub(r"[A-Z]", lambda x: "_" + x.group(0).lower(), identifier)

    if pythid[0] == "_":
        pythid = pythid[1:]

    return pythid


def makearglists(args: Dict) -> Tuple[str, str]:
    """
    Returns the python code for argument declaration and argument passing to
    the function that does the work

    Parameters
    ----------
    args: dict
        Arg info for function returned by Wash Leg website

    Returns
    -------
    arg_declare: str
        String to paste into argument declaration of stub function
    arg_pass: str
        String to paste into backend call of stub function
    """

    for key in args:
        pytype = args[key]["type"].replace("s:", "").lower()
        if pytype == "string":
            pytype = "str"
        elif pytype == "boolean":
            pytype = "bool"
        args[key]["python_type"] = pytype
        args[key]["python_arg"] = snake_case(key)

    arg_types = [f'{args[key]["python_arg"]}: {args[key]["python_type"]}' for key in args]
    arg_declare = ", ".join(arg_types)

    all_args = ", ".join([f"{key}={args[key]['python_arg']}" for key in args])
    arg_pass = f"argdict = dict({all_args})"

    return arg_declare, arg_pass


def make_python_code(servicename: str, functionname: str, args: Dict, fp):
    """
    Generate the stub for a single service request type

    Parameters
    ----------
    servicename: str
        Which service
    functionname: str
        Which request type
    args: dict
        Argument info returned by Wash Leg XML service
    fp: file
        File to paste the stub into
    """
    arg_declare, arg_pass = makearglists(args)
    helpful_url = f'http://wslwebservices.leg.wa.gov/{servicename.lower()}service.asmx?op={functionname}'

    fp.write("\n\ndef ")
    fp.write(snake_case(functionname))
    fp.write(f"({arg_declare}) -> Dict:\n")
    fp.write(f'    """See: {helpful_url}"""\n')
    fp.write(f"    {arg_pass}\n")
    fp.write(
        f'    return waleg.call("{servicename}", "{functionname}", argdict)\n'
    )


def make_stub_files():
    """Queries the definitions of each service and at wslwebservices.leg.wa.gov
    and creates python stub files
    """
    for service in SERVICES:

        fp = open(f"{service.lower()}.py", "w")
        fp.write("from typing import Dict\n")
        fp.write("from datetime import datetime  # noqa\n")
        fp.write("from wa_leg_api import waleg\n")

        wsdl = requests.get(
            f"http://wslwebservices.leg.wa.gov/{service}Service.asmx?WSDL"
        )
        legxml = BeautifulSoup(wsdl.content, "xml")
        schema = legxml.find("s:schema")

        protocols = schema.findAll("s:element", recursive=False)
        for info in protocols:
            name = info["name"]

            if any((not name.startswith("Get"), name.endswith("Response"))):
                continue

            args = info.findAll("s:element")
            arg_dict = {arg.attrs["name"]: arg.attrs for arg in args}

            make_python_code(service, name, arg_dict, fp)
        fp.close()


if __name__ == "__main__":
    make_stub_files()
