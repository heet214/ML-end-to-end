from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' This function returns the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author="Heet Zatakia",
    author_email="heetzatakia@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# notes

'''
# file_path: str is a parameter named file_path with a type hint indicating that it should be a string (**`str`**). 
This means that when you call this function, you should pass a string argument to it, likely representing a path to a file.
-> List[str] is a return type hint that tells you the function is expected to return a list of strings (**`List[str]`**).
Each element in the list is a string.

# with is a context manager in Python that is used here with the open() function.
It ensures that resources are properly managed,
and the file is automatically closed after the block of code under it is executed,
even if an error occurs within the block.
open(file_path) is a function that opens the file located at the path specified by the file_path variable. If no mode is specified, as in this case, it defaults to reading the file ('r' mode).
as file_obj creates a file object file_obj that you can use to perform various operations on the file, such as reading from or writing to it.

# Add '-e .'
-e . is an indication that there exists a setup.py and is linked to it
This setup allows you to have a single source of truth for your package dependencies, 
which is the setup.py file in your project directory. Instead of listing all dependencies in requirements.txt,
you can just specify -e ., 
and pip will refer to setup.py to resolve and install all necessary packages.

remove it from the requirements list in setup.py

'''
