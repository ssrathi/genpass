from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='genpassword',
    version='1.0.0',
    author='Shyamsunder Rathi',
    author_email='shyam29@gmail.com',
    url='https://github.com/ssrathi/genpass',
    description='Generate secure, random and memorable passwords of a specified length.',
    long_description=readme(),
    packages=['genpass'],
    zip_safe=False,
    license='Public Domain',
    keywords='password memorable',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'genpassword = genpass.genpass_cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: Public Domain',
    ],
)
