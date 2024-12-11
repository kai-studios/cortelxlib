from setuptools import setup, find_packages

setup(
    name='cortelxlib', 
    version='0.1.0',   
    packages=find_packages(),  
    install_requires=[ 
        'requests',  
    ],
    author='kai studio',
    author_email='diekunnazar@gmail.com',
    description='A library for managing modular systems, loading models dynamically, and providing an isolated execution environment for secure operations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kai-studios/cortelxlib',
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
