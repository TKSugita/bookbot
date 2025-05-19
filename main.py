def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.
    
    Args:
        filepath (str): Path to the file to be read
        
    Returns:
        str: The contents of the file as a string
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at {filepath} was not found."
    except Exception as e:
        return f"Error reading file: {e}"

from stats import count_words
from stats import count_characters

def main():
    """
    Main function that reads Frankenstein text and prints it to console.
    """
    book_path = "./books/frankenstein.txt"  # Relative path to the book file
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    character_count = count_characters(book_content)
    print(f"{word_count} words found in the document")
    print(character_count)

# Execute the main function
if __name__ == "__main__":
    main()


