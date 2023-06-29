#!/usr/bin/python3


""" importing re module for search and replace """
import re #regular expression

def double_space_to_dot(text):
    """
        It defines what happens to a user input.
        it searches through it and replaces any string that
        ends with 2 consecutive spaces with a dot to show end of sentence.
        and returns the modified data as the users input.
        Else the user continues typing without any modification done to the input

    """

    # parse the text using re
    parsed = re.findall(r'\S+|\s+', text) # pass in the text to the search pattern
    # loop through parsed word and replace words that end with double spaces with a dot at the end of the word.
    for word in range(len(parsed)):
        # check for conditions
        if parsed[word].endswith('  '):#the double spaces
            # do the replacement
            parsed[word] = parsed[word][:-2] + '.'

    # modify the user's input to return the replaces string
    remodel_parsed = ''.join(parsed)
    return(remodel_parsed)


#testing it
if __name__ == "__main__":
    user_input = input('type here: ')
    result = double_space_to_dot(user_input)
    print(result)


