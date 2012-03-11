version = '0.0.1'


import os
from setuptools import setup, find_packages


def read(*paths):
    return open(os.path.join(os.path.dirname(__file__), *paths)).read()


setup(
    name = 'jb.recipe.supervisor',
    version = version,
    author = "Jonathan Ballet",
    author_email = "jon@multani.info",
    url = "https://github.com/multani/jb.recipe.supervisor",
    description = "Recipe for installing Supervisor",
    long_description = (
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
    ),
    keywords = "buildout recipe supervisor template",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Buildout',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Systems Administration',
    ],

    license = "BSD",
    packages = find_packages('.'),
    namespace_packages = ['jb', 'jb.recipe'],
    install_requires = [
        'setuptools',
        'z3c.recipe.scripts',
        'collective.recipe.template',
        'supervisor',
    ],
    entry_points = {
        'zc.buildout': [
            'default = jb.recipe.supervisor:InstallSupervisor',
        ]
    },
    include_package_data = True,
    zip_safe=False,
)
