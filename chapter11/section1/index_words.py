def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            result.append(index)
    return result

text = """The Zen of Python, by Tim Peters"""
print(index_words(text))
