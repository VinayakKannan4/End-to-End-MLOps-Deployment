## IMPORTS

from setuptools import find_packages, setup
from typing import List


## Hyphen_E_dot variable
h_e_d = '-e .'

## REQUIREMENTS>TXT FUNCTION
def get_req(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        [line.replace("\n","") for line in req]

        if h_e_d in req:
            req.remove(h_e_d)
    
    return req

setup(
name = 'MLProject',
version='0.0.1',
author='Vinayak',
author_email='vk297@georgetown.edu',
packages=find_packages(),
install_requires = get_req('requirements.txt')

)