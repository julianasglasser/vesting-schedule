import os, sys, re

version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")

with open('vesting.py') as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

SETUP_ARGS = dict(
    name='vesting',
    version=version,
    description=('Receives a filename and a taget date and returns all vestings events by employee and award type.'),
    long_description=long_description,
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9'
    ],
    py_modules = ['vesting',],
    install_requires = [
        'pandas>=1.3.0',
    ]
)

if __name__ == '__main__':
    from setuptools import setup, find_packages

    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)
