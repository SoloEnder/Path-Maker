import os
from tkinter.messagebox import showerror

base_path = os.path.dirname(__file__)
target_path = os.path.join(base_path, "image_load_failed.png")
path = os.path.abspath(target_path)
load_failed_icon = path if os.path.exists(path) else None

try:
    from ..logger import logger

except ImportError:
    logger_found = False

else:
    logger_found = True

def make_path(src_dir, target_path, is_image=False, request_src="app"):

    """
    Make a path and return it if it exsist

    Args:
        src_dir (str): the variable __file__ of the file wich call the function
        target_path (str): the name of the target path
        is_image (bool): say if the 'target_path' argument is an image (default to False)
        request_src (str, optionnal): if this is the user who call the function, his value will be 'user' else, 'program'. Default set to 'program'.
    

    Returns:
        path (str): the path of the needed file/dir
        return (None): if the made path doesn't exists
        load_failed_icon (tk.PhotoImage):  an image for show image load fail, only returned if the 'target_type' argument is set to 'img'
        """

    base_path = os.path.dirname(src_dir)
    target_path = os.path.join(base_path, target_path)
    path = os.path.abspath(target_path)

    if os.path.exists(path):
        return path

    else:

        if request_src == "user":
            showerror(title="File Manager", message=f"File not found")
            return

        else:
            home = os.path.expanduser("~").lower()
            path = path.lower()

            if home in path:
                path = path.replace(home, "~")
            
            if logger_found == True:
                logger.logging(__name__, f"path '{path}' doesn't exists", 2)

            else:
                
                with open("reports.txt", "a", encoding="utf-8") as f:
                    f.write(f"path '{path}' doesn't exists\n")

            return load_failed_icon if is_image == False else None