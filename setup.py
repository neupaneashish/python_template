import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_template",
    version="0.0.1",
    author="Ashish Neupane",
    author_email="neupane.ashish161@gmail.com",
    description="Python template for ML projects using azure",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="<project-url>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)