import setuptools

setuptools.setup(
    name="solsrv",
    version="0.1.0",
    author="Matthew Farrellee",
    author_email="matt@cs.wisc.edu",
    descrption="A playground for document serving",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mattf/solsrv",
    packages=setuptools.find_packages(),
    package_data={
        "solsrv": ["solsrv.yaml"],
    },
    install_requires=[
        'connexion[swagger-ui]',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
