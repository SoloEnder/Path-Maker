import os

def build_path(src_dir: str, target_path: str) -> str:
    """
    Make an absolute path

    Args:
        - src_dir (str): the value __file__ of the file which call the function
        - target_path (str): a relative path to the target path

    Returns:
        - str: the built absolute path
    """
    base_path = os.path.dirname(src_dir)
    target_path = os.path.join(base_path, target_path)
    path = os.path.abspath(target_path)

    return path