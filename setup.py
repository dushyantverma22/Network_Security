from setuptools import find_packages, setup
from pathlib import Path
from typing import List

def get_requirements()->list[set]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt", "r") as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Dushyant",
    author_email="dushyantdchss@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

## -e . is referring to setup.py