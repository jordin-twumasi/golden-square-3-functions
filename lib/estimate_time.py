def estimate_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for an empty list")
    words = text.split()
    word_count = len(words)
    return word_count / 200 #Constant fow words per minute