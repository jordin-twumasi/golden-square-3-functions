def count_words(text):
  if not isinstance(text, str):
    raise Exception("Must input a string")

  words = text.split()
  return len(words)