from setuptools import find_packages,setup 

def  get_requirements(path):
    requirements = []
    with open(path,"r") as file:
        requirements =  file.readlines()
        requirements  = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements



setup(
    name = "project",
    version= "1.0",
    author = "Shivam",
    packages= find_packages(),
    install_requires = get_requirements("./requirements.txt")

)