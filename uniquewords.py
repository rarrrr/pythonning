#1. Given a piece of text, split it up into words, and find the unique words it contains.
text1 = """
To figure it out, I used the same essential methodology as I did for the short stories: I looked at the tables of contents for 20 anthologies of poetry published between 1992 and 2016 (you can see the full list of anthologies I surveyed at the bottom of the page) and added them all up. My aim was to see what has been included in "general" poetry anthologies for English-speaking readers, so I looked at anthologies that collected international, American, and English-language poems, and I accepted all time periods, but did not allow for any segmentation or specialization otherwise."""

#non-ASCII characters in text1: is there a way to find and remove these easily?
#punctuation: how to split this as well?

#creates an ordered list of each word in text1 and assigns it to a variable called wordlist
wordlist = text1.split()
#print type(wordlist)
unique_words = set(wordlist)
print unique_words
# Should print something like: 'the', 'and', 'find', etc.
print len(unique_words)
# Should print number of unique words in the text
