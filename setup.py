from setuptools import setup, find_packages

setup(
    name="banana_ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=8.0.0",
        "pytest-cov>=6.0.0",
    ],
    author="lofibrainwav",
    author_email="your.email@example.com",
    description="An AI-powered project management and automation tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lofibrainwav/BANANA-AI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
) 