# odin-slides

![odin-slides Logo](img/odin_slides_logo.png)

**odin-slides** is an advanced Python tool that empowers you to effortlessly draft impressive PowerPoint presentations. Leveraging the capabilities of Language Models (LLM), odin-slides enables content summarization, slide generation, and seamless presentation creation or updating based on user input and a chosen template. Whether you're preparing a business pitch, a conference presentation, or a classroom lecture, odin-slides simplifies the process and saves you valuable time.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Installing from the Git Repository](#installing-from-the-git-repository)
  - [Development Installation](#development-installation)
  - [Distribution Installation](#distribution-installation)
- [Usage](#usage)
- [Examples](#examples)
- [Supported File Types](#supported-file-types)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgments and Credits](#acknowledgments-and-credits)
- [Contact](#contact)

## Features

- **Smart Presentation Creation:** Easily create new PowerPoint presentations or update existing ones with odin-slides' user-friendly command-line interface. Simply provide a template and let odin-slides handle the rest.

- **Smart Content Summarization:** odin-slides supports Microsoft Word (docx) files for creating presentations. Even large Word documents are automatically summarized for concise and effective presentation creation. (Note: Other file types such as LaTeX and PDF will be supported in future updates.)

- **Customizable Language Models:** odin-slides supports different language models, with OpenAI GPT-3.5 Turbo as the initial model. You have the flexibility to choose the language model that best fits your presentation needs.

- **Automatic Template Loading:** Specify your desired PowerPoint file as a template, and odin-slides will automatically load its layout theme. No need to manually configure the template every time you create a new presentation.

- **Session Resumption:** Save your presentation creation sessions and resume them later, so you can work at your own pace. odin-slides keeps track of your progress and allows you to pick up right where you left off.

- **Extensibility:** odin-slides is designed to support additional Language Models and file types in future updates. Stay tuned for enhanced functionality and new features.

## Installation

### Installing from the Git Repository

To use the latest version of odin-slides directly from the Git repository, follow these simple steps:

1. Install odin-slides as a command-line tool using pip:

```bash
pip install git+https://github.com/leonid20000/odin-slides.git
```

### Development Installation

To install odin-slides in development mode (editable mode) and contribute to its development, follow these steps:

1. Clone the odin-slides repository to your local machine.

```bash
git clone https://github.com/leonid20000/odin-slides.git
```

2. Change into the following directory.

```bash
cd odin_slides
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Install odin-slides in development mode.

```bash
pip install -e .
```

Now you can make changes to the odin-slides codebase, and the changes will be immediately reflected when you run the odin-slides command-line tool.

### Distribution Installation

To install odin-slides from a distribution package, follow these steps:

1. Download the latest distribution package from the releases page.

2. Install odin-slides using pip:

```bash
pip install /path/to/odin_slides-x.x.x.tar.gz
```

Replace `/path/to/odin_slides-x.x.x.tar.gz` with the path to the downloaded distribution package.

## Usage

To run odin-slides, execute the following command in your terminal:

```bash
odin-slides -t <template_file> -o <output_file> [-i <input_file_path>] [-s <session_file_path>]
```

`<template_file>`: Path to an existing PowerPoint file to copy the layout theme from.

`<output_file>`: Desired output file name for the presentation (without the extension).

`<input_file_path>` (optional): Path to an input Word document to create the presentation based on. Large Word documents will be automatically summarized for presentation purposes.

`<session_file_path>` (optional): Path to a previously saved session file to resume.

Note: For input files larger than 5000 words, odin-slides automatically summarizes them for presentation purposes. You can also resume sessions to continue your presentation creation journey.

## Examples

- Create a new presentation from scratch:

```bash
odin-slides -t /path/to/template.pptx -o my_presentation
```

- Resume a session and continue working on a presentation:

```bash
odin-slides -t /path/to/template.pptx -o my_presentation -s /path/to/my_presentation_session.pkl
```

- Generate a presentation from an existing Word document:

```bash
odin-slides -t /path/to/template.pptx -o my_presentation -i /path/to/input.docx
```


## Supported File Types

odin-slides currently supports the following file types for input documents:

- Microsoft Word (docx): Easily generate presentations from your existing Word documents. Even large Word documents are automatically summarized for concise and effective presentation creation. (Note: Other file types such as LaTeX and PDF will be supported in future updates.)

## Contributions

Contributions to odin-slides are welcome! If you find any issues, have suggestions for improvements, or would like to contribute in any way, please feel free to open an issue or submit a pull request.



## Acknowledgments and Credits

This project was created by Dr. Leonit Zeynalvand and offered under the MIT License.

