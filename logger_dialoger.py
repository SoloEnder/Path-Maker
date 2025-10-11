import os
import json

try:
    from ..utils.logger import logger

except ImportError:
    logger_found = False

else:
    logger_found = True

def logging(path: str, type: str = ""):
    """
    Make a log message to the logger if it is found, or saved in a file else

    Args:
        file_type (str): the type of the unfound file (can be 'img', or 'file', default to 'file')
        path (str): the unfound path
    """
    home = os.path.expanduser("~").lower()
    path = path.lower()

    if home in path:
        path = path.replace(home, "~")

    types = {
        "img":"image"
        }
    
    type = types[type] if type in types.keys() else "file"

    message = f"{type} '{path}' not found"

    from .path_maker import make_path

    if logger_found == True:
        logger.logging(src_dir=__file__, msg="", lvl=3)

    else:
        logs_folder = make_path(__file__, "../../data/path_maker/logs", type="dir", check_existence=False)

        if not os.path.exists(logs_folder):
            os.makedirs(logs_folder)

        log_filepath = os.path.join(logs_folder, "reports.log")

        with open(log_filepath, "a") as f:
            f.write(f"\n{message}")
