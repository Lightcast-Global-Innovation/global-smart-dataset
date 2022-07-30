# coding=utf-8
import setuptools

setuptools.setup(
    name='lightcast-smart-dataset',
    version='0.1.26',
    scripts=['lightcast-smart-dataset'],
    author="Global Data Science Team - Lightcast",
    author_email="globaldatascience@lightcast.io",
    description="Utility use the Lightcast Global Smart Dataset",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Lightcast-Global-Innovation/global-smart-dataset",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests',
                      'xlsxwriter',
                      'pandas',
                      'docopt']
)
