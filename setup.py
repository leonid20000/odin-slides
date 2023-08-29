from setuptools import setup, find_packages

setup(
    name="odin-slides",
    version="0.5",
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
    long_description_content_type="text/markdown",
    long_description = """
## Odin-Slides: Empower Your Presentations with AI

Odin-Slides is an advanced Python tool that empowers you to effortlessly craft impressive PowerPoint presentations. By harnessing the capabilities of Language Models (LLM), Odin-Slides takes presentation creation to the next level.

### Key Features:

1. **Smart Presentation Creation:**
   Easily craft new PowerPoint presentations or update existing ones through odin-slides' intuitive command-line interface. Provide a template, and let odin-slides manage the rest, ensuring a seamless experience.

2. **Input-Driven Presentation Generation:**
   Harness the power of odin-slides to effortlessly transform Microsoft Word (docx) files into captivating presentations. This intelligent tool expertly distills extensive Word documents, converting input into impactful and concise slides. Keep an eye out for upcoming updates that will expand compatibility to include file formats like LaTeX and PDF.

3. **Customizable Language Models:**
   odin-slides supports various language models, with OpenAI GPT-3.5 Turbo as the initial option. Tailor your choice of language model to best suit your presentation requirements, granting you flexibility and control.

4. **Automatic Template Loading:**
   Specify your desired PowerPoint file as a template, and odin-slides will automatically apply its layout theme. Eliminate the need for manual template configuration each time you create a presentation.

5. **Session Resumption:**
   Save your presentation creation sessions for future resumption, allowing you to work at your preferred pace. odin-slides keeps track of your progress, enabling you to seamlessly continue from where you left off.

6. **Extensibility:**
   odin-slides is designed for extensibility, accommodating additional Language Models and file types in forthcoming updates. Anticipate enhanced functionality and new features as the tool evolves.

Stay ahead in the world of presentations with odin-slides — your versatile and intelligent partner in creating impactful content.
""",
    description="An advanced Python tool that empowers you to effortlessly draft impressive PowerPoint presentations from Word documents using generative AI.",
    url="https://github.com/leonid20000/odin-slides",
    author="Dr. Leonit Zeynalvand",
    license="MIT",    
)