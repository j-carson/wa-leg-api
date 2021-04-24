import requests
from typing import Dict, Any, Tuple
from bs4 import BeautifulSoup, Tag
from wa_leg_api.exceptions import WaLegApiException

WSLSITE = "http://wslwebservices.leg.wa.gov"


def unpack_array(array: Tag, keydict: Dict) -> list:
    """Parse section of return where tag == arrayofsomething
    into a list

    Parameters
    ----------
    array: bs4.Tag
        Section of returned tree to be parsed as an array

    Returns:
        list of items
    """
    answer = []

    for item in array:
        if type(item) is not Tag:
            continue
        answer.append(unpack_thing(item, keydict)[1])
    return answer


def unpack_struct(struct: Tag, keydict: Dict) -> Dict:
    """Parse a tag with children, if tag is not arrayof....

    Parameters
    ----------
    struct: bs4.Tag
        Section of returned tree to be parsed as a complex type

    Returns
    -------
    Dict
        The parsed section
    """
    answer = {}
    for item in struct:
        if type(item) is not Tag:
            continue
        name, content = unpack_thing(item, keydict)
        answer[name] = content
    return answer


def unpack_thing(thing: Tag, keydict: Dict) -> Tuple[str, Any]:
    """Parse a chunk of the returned data

    Parameters
    ----------
    thing: bs4.Tag
        root node to unpack from

    Returns
    -------
    name: str
        Name of field unpacked
    contents: Any
        - str if it's a single item
        - list if it's an array item
        - dict if it's a more complex return type
    """
    name = thing.name

    if len(thing.contents) > 1:
        if thing.name.startswith("arrayof"):
            contents = unpack_array(thing, keydict)
        else:
            contents = unpack_struct(thing, keydict)
    else:
        contents = thing.string
        typecaster = keydict.get(name, lambda x: x)
        contents = typecaster(contents)

    return name, contents


def call(service: str, function: str, argdict: dict, keydict: dict) -> Dict:
    """This is the backend to all the stubs

    service: str
        Which service
    function: str
        Function request inside service
    argdict: Dict
        Arguments to the request
    """
    url = f"{WSLSITE}/{service}Service.asmx/{function}"
    response = requests.get(url, params=argdict)
    if not response.ok:
        raise WaLegApiException(response.status_code, response.reason, response.text, argdict)

    body = BeautifulSoup(response.text, "html.parser")
    answer = unpack_struct(body, keydict)
    return answer


if __name__ == "__main__":
    from sponsor import get_sponsors

    result = get_sponsors("2019-20")
