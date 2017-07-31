#0. You're given a list of verbs in present tense as before. You're also given a set of bad words. Exclude the bad words, and convert the remaining into simple past tense.

bad_words = { 'suck', 'lie', 'destroy' }
present_verbs = [ 'walk', 'talk', 'suck', 'like', 'destroy', 'fish', 'lie' ]

#List Comprehensions - makes it easy to exclude items in one list from another
#make a new list:

good_words = [word for word in present_verbs if word not in bad_words]

def to_simple_past_tense(verb):
  if verb.endswith("e"):
    return verb + "d"
  else:
    return verb + "ed"

past_verbs = [ to_simple_past_tense(verb) for verb in good_words ]
print past_verbs

# This should print ["walked", "talked", "liked", "fished", "lied"]
