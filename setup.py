"""
The setup.py file is an essential part of packaging and distributing
python projects . It is used to setuptools
(or disutils in older python versions)to define the configuration
of your project such as meta data,dependencies, and entry points. This file allows you to specify the
necessary information for building, installing, and distributing your package. 
"""
from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    this function will return the list of requirements
    """
    requirements_lst :List[str] = []
    try:
        with open("requirements.txt",'r') as f:
            #read the requirements from the file and split them into a list of strings
            lines = f.readlines()
            #process the lines to remove any whitespace and empty lines
            for line in lines:
               requirement = line.strip()
               #ignore empty lines and comments.
               if requirement and requirement!='-e .':
                   requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_lst
print(get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author="Kevin",
    author_email="kevin.jesu11@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
      )
