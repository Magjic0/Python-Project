def to_hex(text):
    hex_result = ""
    for char in text:
        hex_result += format(ord(char), '02x')
    return hex_result