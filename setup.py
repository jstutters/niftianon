from setuptools import setup

setup(
    name='niftianon',
    version='0.1.0',
    packages=['niftianon'],
    zip_safe=True,
    author='Jon Stutters',
    author_email='j.stutters@ucl.ac.uk',
    description='Anonymiser for NIFTI images',
    url='https://github.com/jstutters/niftianon',
    install_requires=[
        'Click',
        'nibabel'
    ],
    entry_points='''
        [console_scripts]
        niftianon=niftianon.cli:anonymise
    ''',
    license='MIT',
    classifiers=[
    ]
)
