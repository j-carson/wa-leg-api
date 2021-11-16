from typing import Any, Dict, List, Tuple

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

from wa_leg_api.exceptions import WaLegApiException

WSLSITE = "http://wslwebservices.leg.wa.gov"


def unpack_array(array: Tag, keydict: Dict[str, Any]) -> List[Any]:
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


def unpack_struct(struct: Tag, keydict: Dict[str, Any]) -> Dict[str, Any]:
    """Parse a tag with children, if tag is not arrayof....

    Parameters
    ----------
    struct: bs4.Tag
        Section of returned tree to be parsed as a complex type

    Returns
    -------
    Dict[str,Any]
        The parsed section
    """
    answer = {}
    for item in struct:
        if type(item) is not Tag:
            continue
        name, content = unpack_thing(item, keydict)
        answer[name] = content
    return answer


def bs4_string_decode(thing: Any) -> Any:
    """Parse a bs4 item to a str or bool type"""
    if type(thing) is NavigableString:
        string = thing.strip()
    else:
        string = str(thing)

    # Active flag returned by get_legislation isn't
    # in the schema and doesn't get parsed correctly
    if string == "true":
        return True
    elif string == "false":
        return False
    else:
        return string


def unpack_thing(thing: Tag, keydict: Dict[str, Any]) -> Tuple[str, Any]:
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
        # "votes" returned by legislation.get_roll_calls is also an array
        if (thing.name.startswith("arrayof")) or (thing.name == "votes"):
            return name, unpack_array(thing, keydict)
        else:
            return name, unpack_struct(thing, keydict)
    else:
        contents = thing.string
        typecaster = keydict.get(name, bs4_string_decode)
        return name, typecaster(contents)


def call(service: str, function: str, argdict: Dict[str, Any], keydict: Dict[str, Any]) -> Dict[str, Any]:
    """This is the backend to all the stubs

    service: str
        Which service
    function: str
        Function request inside service
    argdict: Dict
        Arguments to the request
    keydict: Dict
        Dictionary of returned keys and functions to cast the key
        the correct type (if the correct type for key is something

        other than a string).
    """
    url = f"{WSLSITE}/{service}Service.asmx/{function}"
    response = requests.get(url, params=argdict)
    if not response.ok:
        raise WaLegApiException(response.status_code, response.reason, response.text, argdict)

    body = BeautifulSoup(response.text, "html.parser")
    answer = unpack_struct(body, keydict)
    return answer


if __name__ == "__main__":
    from wa_leg_api.sponsor import get_sponsors

    result = get_sponsors("2019-20")
