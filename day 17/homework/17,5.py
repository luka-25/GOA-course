def get_vowels(text):
    vowels = "aeiouAEIOUაეიოუ"
    return ''.join([char for char in text if char in vowels])