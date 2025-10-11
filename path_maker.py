import os
from . import logger_dialoger
from . import image_path

def make_path(src_dir: str, target_path: str, type: str = "", check_existence: bool = True) -> str | bool:
    
    """
    Make a path and return it if it exsist

    Args:
        src_dir (str): the variable __file__ of the file wich need the path
        target_path (str): the name of the target path
        type (str): the category of the file ("img"->image). default to ""
        resuest_src (str): the source of the request ('internal' if the caller is not in package, else 'external')
    
    Returns (case 'check_existence = True')
        str: the built path
        bool: False if the built path don't exists

    Returns (case 'check_existence = False'):
        str: the built path
        """

    base_path = os.path.dirname(src_dir)
    target_path = os.path.join(base_path, target_path)
    path = os.path.abspath(target_path)

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
            logger_dialoger.logging(path)
            return False
        
        else:
            return path