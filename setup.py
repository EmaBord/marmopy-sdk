from setuptools import find_packages, setup


setup(
    name='marmopy',
    
    version="0.1.2",
    
    description='Marmo wallet Python SDK',
    
    author='Majed Takieddine',
    
    author_email='majd_takialddin@hotmail.com',
    
    url='https://github.com/ripio/marmopy-sdk',
    
    packages=find_packages(exclude=('tests',)),
    
    install_requires=["web3",'rlp',"pycryptodome","coincurve"],
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    
)