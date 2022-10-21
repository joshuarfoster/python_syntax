def print_upper_words(words,must_start_with):
    """Given list of words, it prints each word, that starts with a character defined in must_start_with, in uppercase.

for example:
    print_upper_words(['banana','apple','pear'],must_start_with=['b','p'])

    Should print:
    'BANANA'
    'PEAR'
    """
    for word in words:
        valid=False
        for char in must_start_with:
            if char == word[0]:
                valid=True
        if valid:
            print (word.upper())

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"})