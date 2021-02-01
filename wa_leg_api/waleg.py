import requests
from typing import Dict, Any
from bs4 import BeautifulSoup, Tag

WSLSITE = 'http://wslwebservices.leg.wa.gov'

def unpack_array(array: Tag) -> list:
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
        answer.append(unpack_thing(item)[1])
    return answer

def unpack_struct(struct: Tag) -> Dict:
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
        name, content = unpack_thing(item)
        answer[name] = content
    return answer
            
def unpack_thing(thing: Tag) -> Tuple[str, Any]:
    """Parse a chunk of the returned data
    
    Parameters:
    
    
    """
    
    
    name = thing.name
    
    if len(thing.contents) > 1:
        if thing.name.startswith('arrayof'):
            contents = unpack_array(thing)
        else:
            contents = unpack_struct(thing)
    else:
        contents = thing.string

    return name, contents
    

def call(service: str,  function: str, argdict: dict) -> Dict:
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
    
    body = BeautifulSoup(response.content, 'html.parser')
    answer = unpack_struct(body)
    return answer
    

if __name__ == "__main__":
    from sponsor import get_sponsors
    result = get_sponsors('2019-20')