present_verbs = ["walk", "talk", "like", "fish"]
def to_simple_past_tense(verb):
  if verb.endswith("e"):
    return verb + "d"
  else:
    return verb + "ed"

past_verbs = []
for verb in present_verbs:
    past_verb = to_simple_past_tense(verb)
    past_verbs.append(past_verb)

print past_verbs
