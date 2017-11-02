pyg = 'ay'

original = raw_input('Enter a word:')


if len(original) > 0 and original.isalpha():
    word = original.lower()

    first = word[0]

    new_word = word[1:len(word) ]

    print new_word + first + pyg
else:
    print 'Please enter a valid word'
