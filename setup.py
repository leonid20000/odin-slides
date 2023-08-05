from setuptools import setup, find_packages

setup(
    name="odin-slides",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'python-pptx',
        'python-docx',
        'requests',
        'colorama',
        'tqdm'
    ],
    entry_points={
        "console_scripts": [
            "odin-slides=odin_slides.main:main",
        ],
    },
    test_suite="tests",
)