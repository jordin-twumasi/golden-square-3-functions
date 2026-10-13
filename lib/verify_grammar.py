def verify_grammar(text):
  if text[-1] in '!?.' and text[0].isupper():
    return True
  else:
    return False