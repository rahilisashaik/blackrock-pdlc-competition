import subprocess

def display_results(file_path):
    """
    Opens a file using the default application on macOS.

    Args:
    file_path (str): The path to the file to be opened.
    
    """
    file_path = "random_word_generator.MARKDOWN"
    try:
        subprocess.run(['open', file_path])
    except Exception as e:
        print(f"An error occurred while trying to open the file: {e}")

if __name__ == "__main__":
    file_path = '../PDLC/standardization/random_word_generator.MARKDOWN'
    # process_file(file_path)

    subprocess.run(['open', file_path])

