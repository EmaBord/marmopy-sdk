from setuptools import find_packages, setup


setup(
    name='marmopy',

    version="0.4.0",

    description='Marmo wallet Python SDK',

    author='Agustin Aguilar, Joaquin Gonzalez, Majed Takieddine',

    author_email='agusxrun@gmail.com, jpgonzalezra@gmail.com, majd_takialddin@hotmail.com',

    url='https://github.com/ripio/marmopy-sdk',

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        "web3",
        "rlp",
        "pycryptodome",
        "coincurve",
        "eth-abi",
        "requests"
    ],

    extras_require={
        "dev": [
            "pylint",
            "pytest",
            "tox>=1.8.0"
        ]
    },

    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
