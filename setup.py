from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='maxiverse', 
    version='0.0.5',
    author="Balavignesh M",
    author_email="crystelpheonix@gmail.com",
    packages=setuptools.find_packages(),
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # package_dir={'':'maxiverse'},     # Directory of the source code of the package
    install_requires=[
        #   'scikit-learn==0.22.2.post1',
        #   'pandas==1.1.5',
        #   'xgboost==0.90'
        'scikit-learn',
        'pandas',
        'xgboost'
      ],)