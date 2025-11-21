import os

def load_markdown_file(file_path: str) -> str:
    """
    Reads and returns the content of a markdown file.

    Args:
        file_path: The path to the markdown file.

    Returns:
        The content of the markdown file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")
