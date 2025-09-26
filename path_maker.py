import os
from tkinter.messagebox import showinfo, showerror
import tkinter as tk

def make_path(src_dir, target_path, request_src="program"):
    
    """ 
    Make a path and return it if it exsist
    
    Args:
        src_dir (str): the variable __file__ of the file wich call the function
        target_path (str): the name of the target path
        request_src (str, optionnal): if the this is the user who call the function, his value will be 'user' else, 'program'. Default set to 'program'
        
    Returns:
        path (str): the path of the needed file/dir
        return (None): if the made path doesn't exists"""
        
    base_path = os.path.dirname(src_dir)
    target_path = os.path.join(base_path, target_path)
    path = os.path.abspath(target_path)
    
    if os.path.exists(path):
        return path
        
    else:
        
        if request_src == "user":
            showerror(title="File Manager", message=f"Le dossier que vous recherchez n'existe pas")
            
        else:
            print("file", path, "not found")
            return