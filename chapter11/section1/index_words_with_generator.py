def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index

text = """The Zen of Python, by Tim Peters"""
print(list(index_words(text)))
