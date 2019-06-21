try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='_tests.py',
    version='1.0',
    description='Modules working like simple cmdlets.',
    author='Mateusz Kanabrocki',
    author_email='mateusz.kanabrocki@gmail.com',
    packages=['cmdlets'],  #same as name
    install_requires=['nose'], #external packages as dependencies
    url='https://github.com/mateuszkanabrocki/projects/tree/master/?',
    download_url='https://github.com/mateuszkanabrocki/projects/tree/master/?',
    include_package_data=True #include MANIFEST.in file
    # 'py_modules': ['MODULE_NAME'],
    # 'scripts': [],
)

# config = {
#     'description': 'Simple text-based game run in the web browser.,
#     'author': 'Mateusz Kanabrocki',
#     # 'url': 'https://github.com/mateuszkanabrocki/projects/tree/master/gothonweb',
#     'download_url': 'https://github.com/mateuszkanabrocki/projects/tree/master/gothonweb',
#     'author_email': 'mateusz.kanabrocki@gmail.com',
#     'version': '0.1',
#     'install_requires': ['nose'],
#     # 'packages': ['NAME'],
#     # 'py_modules': ['MODULE_NAME'],
#     # 'scripts': [],
#     'name': 'projectnamegothonweb'

# setup(**config)
