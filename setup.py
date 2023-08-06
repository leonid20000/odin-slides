from setuptools import setup, find_packages

setup(
    name="odin-slides",
    version="0.2",
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

    description="An advanced Python tool that empowers you to effortlessly draft impressive PowerPoint presentations. Leveraging the capabilities of Language Models (LLM), odin-slides enables content summarization, slide generation, and seamless presentation creation or updating based on user input",
    url="https://github.com/leonid20000/odin-slides",
    author="Dr. Leonit Zeynalvand",
    license="MIT",    
)