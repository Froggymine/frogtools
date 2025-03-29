from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Froggymines CTF and etc tools'
LONG_DESCRIPTION = 'Froggymines CTF and etc tools'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="frogtools", 
        version=VERSION,
        author="Froggymine",
        author_email="t@mmc.au",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'ctf'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Other Audience",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS",
            "Operating System :: POSIX :: Linux",
        ]
)