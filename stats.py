def count_words(text):
    # counts out the number of words in a string splitting based on white space
    # Args: Uses text strings 
    # Returns: an integer consisting of the number of words in the text
	# (number of elements in the resulting list)
    
	words =  text.split()
	return len(words)