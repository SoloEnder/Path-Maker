import os
import logging
from .core import build_path
from . import image_path

logger = logging.basicConfig()

def make_path(src_dir: str, target_path: str, type: str = "", check_existence: bool = True) -> str | bool:
    
    """
    Make a path and return it if it exsist

    Args:
        - src_dir (str): the value __file__ of the file which call the function
        - target_path (str): a relative path to the target path
        - type (str): the category of the file ("img"->image). default to ""
    
    Returns (case 'check_existence = True')
        str: the built path
        bool: False if the built path don't exists

    Returns (case 'check_existence = False'):
        str: the built path
        """
    path = build_path(src_dir, target_path)
    
    path_returners = {
        "img":image_path.return_path,
    }
    
    if not check_existence:
        return path

    if os.path.exists(path):
        path_found = True

    else:
        path_found = False

    if type in path_returners.keys():
        path_returner = path_returners[type]
        return path_returner(path, path_found)
    
    else:

        if path_found == False:
            return False
        
        else:
            return path