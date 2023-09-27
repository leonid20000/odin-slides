import argparse
import time
import pickle

from tqdm import tqdm
from colorama import init


from .utils import setup_debug_logger, read_word_file, read_big_word_file, format_error, format_info
from .llm_ops import get_LLM_summarization
from .presentation import build_slides_with_llm

def main():
    """Entry point for the OdinSlides presentation creation tool.

    Reads user input from command-line arguments and performs the necessary operations
    to create or update a PowerPoint presentation based on provided input files or resumes
    a previously saved session.

    Args:
        None

    Returns:
        None
    """
    # Call init() once to enable colored text on Windows. On other platforms it is optional.
    init()
    parser = argparse.ArgumentParser(description="OdinSlides is a productivity tool to help you draft a presentation.")
    parser.add_argument("-t", "--template_file", required=True, help="Path to an existing PowerPoint file to copy the layout theme from.")
    parser.add_argument("-o", "--output_file", required=True, help="Desired output file name for the presentation")
    parser.add_argument("-i", "--input_file_path", type=str, nargs="?", default=None, help="Path to an input word document to make the presentation based on (optional)")
    parser.add_argument("-s", "--session_file_path", type=str, nargs="?", default=None, help="Path to a previously saved session (optional)")
    args = parser.parse_args()

    try:
        # Set this variable to control debug mode
        debug_mode = False

        # Set up the logger based on the debug_mode
        logger = setup_debug_logger(debug_mode)
        word_content=""
        word_content_list=[]
        #5000 is roughly about the max_word_count_without_summarization (in the input document) to effectively use with a 16k context capacity. Dont increase.
        max_word_count_without_summarization=5000
        # If input_file_path is provided and we are not resuming a saved session, attempt to read the word content from the input file
        if args.input_file_path and not args.session_file_path:
            try:
                print(format_info("Loading the document into context ... ")+"\n")
                word_content = read_word_file(args.input_file_path,logger)
                doc_word_count=len(word_content.split())
                logger.debug(doc_word_count)
                summarization_chunk_size=doc_word_count // 10
                #logger.debug(word_content)
                if doc_word_count > max_word_count_without_summarization :
                    print(format_info("Document is big. Loading a summarized version into context ... ")+"\n")
                    word_content_list=read_big_word_file(args.input_file_path,summarization_chunk_size,logger)
                    for i,raw_content in tqdm(enumerate(word_content_list), total=len(word_content_list), desc="Processing", unit="document_part"):
                        temp_summary=""
                        while not temp_summary:
                            temp_summary=get_LLM_summarization(raw_content,logger)
                            word_content_list[i]=temp_summary
                            time.sleep(1)
                    word_content="\n".join(word_content_list)
                    logger.debug("Shortened Document: "+word_content)
                    #for item in word_content_list:
                        #logger.debug(item)
                print(format_info("Input article loaded successfully.")+"\n")
            except Exception as e:
                print(format_error("Could not process input file: ")+ f"{e}"+"\n")
                logger.error(f"Error processing input file: {e}")
                raise


        # If session_file_path is provided, attempt to resume the session
        if args.session_file_path:
            # Load session data from the session file
            with open(args.session_file_path, 'rb') as file:
                loaded_data = pickle.load(file)
                logger.debug(loaded_data)
            # Access slideDeckHistory variable from the loaded data
            word_content = loaded_data['word_content']
            build_slides_with_llm(args.template_file,word_content, args.output_file+".pptx", args.session_file_path, logger)
        else:
            build_slides_with_llm(args.template_file,word_content, args.output_file+".pptx", None, logger)

    except Exception as e:
        print(format_error("Something went wrong: ")+f"{e}"+"\n")
    except KeyboardInterrupt:
        print("\n"+format_info("Exiting..."))
        print("Enjoying this project? Your support means a lot!")
        print("If you find this open-source effort helpful, please consider giving it a star on GitHub.")
        print("GitHub Repository: https://github.com/leonid20000/odin-slides")
        print("Have ideas, found a bug, or need assistance?")
        print("Feel free to create issues or submit pull requests on GitHub.")
        print("\n"+format_info("Thank you for being part of the open-source community. See you next time!"))

    finally:
        # Remember to close the log handler when done
        for handler in logger.handlers:
            handler.close()


if __name__ == "__main__":
    main()
