# (Bonus) Do the same to another price of text. Then find the unique words *in common* with the previous text.

text1 = """
To figure it out, I used the same essential methodology as I did for the short stories: I looked at the tables of contents for 20 anthologies of poetry published between 1992 and 2016 (you can see the full list of anthologies I surveyed at the bottom of the page) and added them all up. My aim was to see what has been included in "general" poetry anthologies for English-speaking readers, so I looked at anthologies that collected international, American, and English-language poems, and I accepted all time periods, but did not allow for any segmentation or specialization otherwise."""

text2 = """
Drivers be aware. The Highways Agency found over 200 dead crows on the A421, near the Northampton roundabout recently, and there was concern that they may have died from Avian Flu. A Pathologist examined the remains of all the crows, and, to everyone's relief, confirmed the problem was NOT Avian Flu.
The cause of death appeared to be from vehicular impacts. However, during analysis it was noted that varying colours of paints appeared on the bird's beaks and claws. By analysing these paint residues it was found that 98% of the crows had been killed by impact with motorbikes, while only 2% were killed by cars.
The Agency then hired an Ornithological Behaviourist to determine if there was a cause for the disproportionate percentages of motorbike kills versus car kills. The Ornithological Behaviourist quickly concluded that when crows eat road kill, they always have a look-out crow to warn of danger. They discovered that while all the lookout crows could shout "Cah", not a single one could shout "bike"
"""

wordlist1 = text1.split()
unique_words1 = set(wordlist1)

wordlist2 = text2.split()
unique_words2 = set(wordlist2)

#combinedlist = wordlist1 + wordlist2
#print combinedlist
#print set(combinedlist)
# or:
#print set(wordlist1 + wordlist2)
# ^^ this gives us a list of all the unique words in both 1 and 2

common_words = []

for word in unique_words1:
    if word in unique_words2:
        common_words.append(word)

print common_words
# Should print the words in common between text1 and text2
