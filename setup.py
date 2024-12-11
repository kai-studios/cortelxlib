from setuptools import setup, find_packages

setup(
    name="cortelxlib",  
    version="0.1",  
    description="Library for CortelXLoader project",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    author="kai studio",  
    author_email="diekunnazar@gmail.com",  
    url="https://github.com/kai-studios/cortelxlib",  
    packages=find_packages(),  
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later", 
        "Operating System :: OS Independent",
    ],
)
