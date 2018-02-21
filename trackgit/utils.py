import os
import subprocess

def get_git_hash():
    """Returns the git description (shortened git hash)

    Parameters
    ----------

    Returns
    -------
    label : string
        Shortened git hash
    """
    label = subprocess.check_output(["git", "describe", "--always"]).strip()
    return label.decode('utf-8')

def check_git_status():
    """Check if there's any modifications to commit in the repo 

    Parameters
    ----------

    Returns
    -------
    status : boolean
        True if nothing. False otherwise.
    """
    status = subprocess.check_output(["git", "status", "--porcelain"]).splitlines()
    # Skip the files that are not version controlled
    status = [file_status for file_status in status if file_status[:2] != b'??']
    if len(status) > 0:
        return False
    return True

def make_git_tagged_dir(log_dir):
    """Create a directory with git hash appened to directory name.
    
    Parameters
    ----------
    log_dir : string
        Name of the directory before tagging to be created.

    Returns
    -------
    tagged_dir : string
        Name of the directory created with git tag.
    """
    if not check_git_status():
        raise ValueError("Changes are present, need to commit!")

    tagged_dir = log_dir + "_" + get_git_hash() 
    
    if os.path.exists(tagged_dir):
        raise ValueError("Directory %s already exists!" % tagged_dir)    
    else:
        os.makedirs(tagged_dir)

    return tagged_dir
