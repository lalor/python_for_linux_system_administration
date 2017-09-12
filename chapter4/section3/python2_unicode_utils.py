def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value

def to_str(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value
