def make_snippet(text):
    if not isinstance(text,str):
        raise Exception("Must input a string")

    words = text.split()
    if len(words) > 5:
     return f"{' '.join(words[:5])}..."
    
    return text