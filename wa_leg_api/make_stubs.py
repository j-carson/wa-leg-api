"""
Generates python stubs from the Washington State Legislature Schema XML Responses
"""

import re
from typing import IO, Any, Dict, Tuple

import requests
from bs4 import BeautifulSoup, Tag

NOT_WORKING = ["GetLegislativeBillListFeatureData"]


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


def makearglists(args: Dict[str, Any]) -> Tuple[str, str]:
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
    arg_pass = f"argdict: Dict[str,Any] = dict({all_args})"

    return arg_declare, arg_pass


def make_keydict(key_to_type: Dict[str, Any]) -> str:
    """
    Returns the python code for declaring a dictionary that
    changes the returned strings to their correct types

    Parameters
    ----------
    key_to_type: dict
        keys are the field names in the returned structure, values
        are the functions to call to cast to correct type

    Returns
    -------
    keydict_declare: str
        String to paste into stub function to create the desired dictionary
    """
    accum = "{"

    for key, val in key_to_type.items():
        # no need to cast str to str
        if val != "str":
            accum += f"'{key}':{val},\n"

    accum += "}"
    return f"keydict : Dict[str,Any] = {accum}"


def make_python_code(
    servicename: str, functionname: str, args: Dict[str, Any], key_to_type: Dict[str, Any], fp: IO[str]
) -> None:
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
    key_to_type: dict
        How to unpack returned data
    fp: file
        File to paste the stub into
    """
    arg_declare, arg_pass = makearglists(args)
    return_keys = make_keydict(key_to_type)
    helpful_url = f"http://wslwebservices.leg.wa.gov/{servicename.lower()}service.asmx?op={functionname}"

    fp.write("\n\ndef ")
    fp.write(snake_case(functionname))
    fp.write(f"({arg_declare}) -> Dict[str,Any]:\n")
    fp.write(f'    """See: {helpful_url}"""\n')
    fp.write(f"    {arg_pass}\n")
    fp.write(f"    {return_keys}\n")
    fp.write(f'    return waleg.call("{servicename}", "{functionname}", argdict, keydict)\n')


def make_stub_files():
    """Queries the definitions of each service and at wslwebservices.leg.wa.gov
    and creates python stub files
    """
    for service in SERVICES:

        fp = open(f"{service.lower()}.py", "w")
        fp.write("from typing import Dict,Any\n")
        fp.write("from datetime import datetime  # noqa\n")
        fp.write("from dateutil import parser  # noqa\n")
        fp.write("from wa_leg_api import waleg\n")

        wsdl = requests.get(f"http://wslwebservices.leg.wa.gov/{service}Service.asmx?WSDL")
        legxml = BeautifulSoup(wsdl.content, "xml")
        schema = legxml.find("s:schema")

        protocols = schema.findAll("s:element", recursive=False)
        structtypes = schema.findAll("s:complexType", recursive=False)
        enumtypes = schema.findAll("s:simpleType", recursive=False)

        def lookup_datatype(type_name):
            if type_name.startswith("tns:ArrayOf"):
                type_name = type_name.replace("tns:ArrayOf", "")
            else:
                type_name = type_name.replace("tns:", "")

            for dt in structtypes:
                if dt.attrs["name"] == type_name:
                    return dt

            for dt in enumtypes:
                if dt.attrs["name"] == type_name:
                    return dt

            if type_name == "AnyType":
                return None  # cannot decode this further

            raise Exception(f"{type_name} not found")

        for info in protocols:
            name = info["name"]
            if name in NOT_WORKING:
                continue

            response_name = name + "Response"

            if any((not name.startswith("Get"), name.endswith("Response"))):
                continue

            args = info.findAll("s:element")
            arg_dict = {arg.attrs["name"]: arg.attrs for arg in args}

            for r in protocols:
                if r["name"] == response_name:
                    response_info = r
                    break
            else:
                raise Exception(f"Response {response_name} not found")

            def update_keydict(typeinfo, acc_dict):
                type_replace = {
                    "s:int": "int",
                    "s:string": "str",
                    "s:boolean": 'lambda boolstr: (boolstr.lower() == "true")',
                    "s:dateTime": "parser.parse",
                }
                attrs = typeinfo.attrs
                if attrs["type"].startswith("tns:"):
                    nested_info = lookup_datatype(attrs["type"])
                    if nested_info:
                        if nested_info.name == "complexType":
                            elems = nested_info.findAll("s:element")
                            for el in elems:
                                update_keydict(el, acc_dict)
                        else:
                            for item in nested_info:
                                if type(item) is not Tag:
                                    continue
                                item_type = item.attrs["base"]
                                acc_dict[nested_info.attrs["name"].lower()] = type_replace[item_type]
                                break
                else:
                    acc_dict[attrs["name"].lower()] = type_replace[attrs["type"]]

            key_to_type = {}
            returnvals = response_info.findAll("s:element")
            for val in returnvals:
                update_keydict(val, key_to_type)

            make_python_code(service, name, arg_dict, key_to_type, fp)
        fp.close()


if __name__ == "__main__":
    make_stub_files()
