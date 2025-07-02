def word_count(text):
    words = text.split()
    return len(words)
    
def character_count(text):
    counts = {}
    for ch in text:
        lowered = ch.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    return counts

def sort_on(items):
    return items["num"]

def sort_char_count(text):
    dict_list = []

    counts = character_count(text)
    for key, value in counts.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
