import setuptools 

setuptools.setup(
    name = "palindrome",
    version='1.0',
    ext_modules = [setuptools.Extension('_palindrome', ['palindrome.c','palindrome.i'])]
)