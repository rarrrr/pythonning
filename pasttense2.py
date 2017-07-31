#a quicker way to do what we did in pasttense.py
present_verbs = ["walk", "talk", "like", "fish"]
def to_simple_past_tense(verb):
  if verb.endswith("e"):
    return verb + "d"
  else:
    return verb + "ed"

past_verbs = [ to_simple_past_tense(verb) for verb in present_verbs ]
print past_verbs

#or just
#print [ to_simple_past_tense(verb) for verb in present_verbs ]
#print type(past_verbs)
