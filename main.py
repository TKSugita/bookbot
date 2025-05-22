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

import sys
from stats import count_words, sort_char_count
from stats import count_characters

def main():
    """
    Main function that reads Frankenstein text and prints it to console.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_path = sys.argv[1]  # Relative path to the book file
    
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    char_count = count_characters(book_content)
    sorted_char = sort_char_count(char_count)
    print(f"Found {word_count} total words")
    for char_dict in sorted_char:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    


# Execute the main function
if __name__ == "__main__":
    main()


