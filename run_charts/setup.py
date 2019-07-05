try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='run_charts',
    version='1.0',
    description='Make run chart from the date collected in the .txt files.\
    Prompt for the data every day. Execute automaticaly using cron',
    author='Mateusz Kanabrocki',
    author_email='mateusz.kanabrocki@gmail.com',
    packages=['run_charts'],  #same as name
    install_requires=['nose'], #external packages as dependencies
    url='https://github.com/mateuszkanabrocki/projects/tree/master/?',
    download_url='https://github.com/mateuszkanabrocki/projects/tree/master/?',
    include_package_data=True #include MANIFEST.in file
    # 'py_modules': ['MODULE_NAME'],
    # 'scripts': [],
)

# setup(**config)
