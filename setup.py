from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    ''' this function will return a list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        # requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

#this is the metadata for the package that will be installed in the package manager and installed 
setup(
    name='end-to-end-ml-project',
    version='0.1',
    description='An end-to-end machine learning project using the PySpark library',
    author='ramesh sah',
    author_email='rsah3798@gmail.com',
   
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)