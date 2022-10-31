def print_upper_words(words, must_start_with):
    ''' prints out input words in their upper cases starting with the specified letters'''
    for word in words:       
        if {word[0].upper()}.issubset(must_start_with) or {word[0].lower()}.issubset(must_start_with):
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
