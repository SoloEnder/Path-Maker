
import os
from .logger_dialoger import logging

def return_path(path: str, found: bool) -> str:
    """
    Make, search and return an image path

    Args:
        src_dir (str): the value __file__ of the caller file
        target_path (str): an relative path of the searched path

    Returns:
        str: the needed path (if it exists) or an image for illustrate the load fail
    """
    
    if found:
        return path
    
    else:
        from .path_maker import make_path
        logging(path, "img")
        failed_load_img = make_path(__file__, "image_load_failed.png")
        return failed_load_img
    