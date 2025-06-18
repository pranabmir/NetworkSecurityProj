from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #function to check requirements list

    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for i in lines:
                requirement = i.strip()
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print('requirement.txt not found')
    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Pranab Mir",
    author_email="pranabmir1994@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)