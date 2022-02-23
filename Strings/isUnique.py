#using data structure
def is_unique(string):
    return len(set(string)) == len(string)
  
 def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True


def is_unique_chars_using_set(string: str) -> bool:
    characters_seen = set()
    for char in string:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True
  
# without data structure
def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True
