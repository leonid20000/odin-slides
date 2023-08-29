"""
llm_ops.py - Module for Language Model Operations.

This module provides functions for interacting with language models to perform various tasks,
such as summarizing content and generating chat responses for creating or updating slide content.

Module Functions:
    - get_LLM_summarization(word_content, logger):
        Get a summarization of the provided word content using a language model.

    - get_chat_response(word_content, slideDeck, prompt, logger):
        Get a chat response for creating or updating text content for slides.

Dependencies:
    - os
    - requests
    - json
    - utils (custom utility functions in utils.py)

Environment Variables:
    - ODIN_SLIDES_LLM_API_KEY: API key for accessing the language model services.

Note: This version of odinSlides only supports OpenAI APIs, but future updates will extend support for other LLMs.

"""

import os
import json
import requests

from .utils import format_error

def get_LLM_summarization(word_content,logger):
    """Get a summarization of the provided word content using a language model.

    Args:
        word_content (str): The content to be summarized.
        logger (logging.Logger): The logger object to record any errors.

    Returns:
        str or None: The summarized content or None if an error occurs.
    """
    # Replace 'your_custom_api_endpoint' with the actual endpoint of your custom API
    api_endpoint = 'https://api.openai.com/v1/chat/completions'
    api_key = os.environ.get('ODIN_SLIDES_LLM_API_KEY')

    if api_key is None:
        print(format_error("API key not found. Please make sure the 'ODIN_SLIDES_LLM_API_KEY' environment variable is set to the API key for your desired LLM. (In this version of odinSlides only OpenAI APIs are supported. This will be extended to also include other LLMs in future updates.)"))
        raise ValueError("API key not found. Please make sure the 'ODIN_SLIDES_LLM_API_KEY' environment variable is set.")
    if len(word_content.split()) < 1000:
        model = "gpt-3.5-turbo"
    else:
        model = "gpt-3.5-turbo-16k"

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Input Article: " + word_content},
            {"role": "system", "content": "User will ask you to shorten the Input Article. Make sure that the shortened version captures all the key points. \n  Response format: Keep the format of the Input Article. \n Output only the shortened article."},
            {"role": "user", "content": "Shorten the Input Article."}
        ],
        "temperature": 0.9,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6
    }


    try:
        # Make an HTTP POST request with the API key and a timeout of 10 seconds
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.post(api_endpoint, json=data, headers=headers, timeout=300)
        response_data = response.json()
        #print(response_data)

        # Access the 'content' attribute inside the 'message' object of choices[0]
        print("\n Using "+data["model"]+" :")
        if 'usage' in response_data:
            print(response_data['usage'])
            logger.debug(response_data['usage'])
        if 'error' in response_data:
            print(format_error("API response indicates error: "))
            print(response_data)
            raise ValueError("Bad API response!")
        response_message = response_data['choices'][0]['message']['content']
        return response_message

    except requests.exceptions.Timeout:
        print("Error: Request to API timed out. Please try again later or check your internet connection.")
        logger.error("Request to API timed out. Please try again later or check your internet connection.")
        return None



def get_chat_response(word_content, slideDeck, prompt,logger):
    """Get a chat response for creating or updating text content for slides.

    Args:
        word_content (str): The word content to consider while generating chat response.
        slideDeck (list): The existing slide deck represented as a list of dictionaries.
        prompt (str): The prompt to ask the chatbot.
        logger (logging.Logger): The logger object to record any errors.

    Returns:
        str or None: The chat response or None if an error occurs.
    """
    for slide in slideDeck:
        # Set the value for the narration key to a default
        slide["narration"] = "Presentation Transcript: \n "

    api_endpoint = 'https://api.openai.com/v1/chat/completions'
    api_key = os.environ.get('ODIN_SLIDES_LLM_API_KEY')

    if api_key is None:
        print(format_error("API key not found. Please make sure the 'ODIN_SLIDES_LLM_API_KEY' environment variable is set to the API key for your desired LLM. (In this version of odinSlides only OpenAI APIs are supported. This will be extended to also include other LLMs in future updates.)"))
        raise ValueError("API key not found. Please make sure the 'ODIN_SLIDES_LLM_API_KEY' environment variable is set.")

    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [
            {"role": "system", "content": "User will ask you to create or update text content for some slides"+(" based on the aforementioned Input Article" if word_content else "")+". The response format should be a valid json format structured as this: [{\"slide_number\": <Float>, \"title\": \"<String>\", \"content\": \"<String>\", \"narration\": \"<String>\"},{\"slide_number\": <Float>, \"title\": \"<String>\", \"content\": \"<String>\", \"narration\": \"<String>\"}] \n content field in the response comprehensive enough as it is the main text of each slide. \n For content use a mix of bullet points and text when applicable. \n If you are modifying an existing slide leave the slide number unchanged but if you are adding slides to the existing slides, use decimal digits for the slide number. for example to add a slide after slide 2, use slide number 2.1, 2.2, ... \n If user asks to remove a slide, set its slide number to negative of its current value because slides with negative slide number will be excluded from presentation. \n The existing slides are as follows: "+json.dumps(slideDeck)},
            {"role": "system", "content": "For each slide the content field is the main body of the slide while the narration field is just an example transcript of the presentation of the content field. \n Never mention the slide number in the transcript."},
            {"role": "system", "content": "For each slide, the content field should be the default field to modify if modification is demanded by the user for the slide, not the narration field. "},
            {"role": "system", "content": "For each slide, the narration field should only be populated if explicitely asked in user prompt, otherwise should be left empty. "},
            {"role": "system", "content": "Response should be valid json. slide_number, title,and content are mandatory keys."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6
    }
    if word_content:
        data["messages"].insert(0, {
            "role": "system",
            "content": "Input Article: " + word_content
            })

    try:
        # Make an HTTP POST request with the API key and a timeout of 10 seconds
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.post(api_endpoint, json=data, headers=headers, timeout=300)
        response_data = response.json()
        #print(response_data)

        # Access the 'content' attribute inside the 'message' object of choices[0]
        print(response_data['usage'])
        logger.debug(response_data['usage'])
        response_message = response_data['choices'][0]['message']['content']
        logger.debug(response_message)
        return response_message

    except requests.exceptions.Timeout:
        logger.error("Request to API timed out. Please try again later or check your internet connection.")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None
