def count_words(text):
    # counts out the number of words in a string splitting based on white space
    # Args: Uses text strings 
    # Returns: an integer consisting of the number of words in the text
	# (number of elements in the resulting list)
    
	words = text.split()
	return len(words)

def count_characters(text):
      # load text into dictionary by character

    #initialize variables
    char_count = {}

    # to remove case dependency
    text = text.lower()

    # use a for loop to step through each char in text and increase the count associated to the letter (key)

    for char in text:
        if char in char_count:
                char_count[char] += 1
        else:
              char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    # Sorts char_count

    # init return variable
    char_list = []

    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list   
