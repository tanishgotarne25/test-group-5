"""
Text helpers.
The worked example every contribution is modelled on.
"""


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    if not isinstance(suffix, str):
        raise TypeError("suffix must be a string")

    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")

    if len(text) <= limit:
        return text

    return text[:limit - len(suffix)] + suffix


def capitalize_words(text):
    """Capitalize the first letter of every word.

    >>> capitalize_words("hello world")
    'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()


def reverse_text(text):
    """Reverse the given text.

    >>> reverse_text("hello")
    'olleh'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]


def count_characters(text):
    """Count characters excluding spaces.

    >>> count_characters("hello world")
    10
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.replace(" ", ""))


def remove_extra_spaces(text):
    """Remove unnecessary spaces between words.

    >>> remove_extra_spaces("hello    world")
    'hello world'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


if __name__ == "__main__":

    sample = "hello world"

    print("Word Count:", word_count(sample))
    print("Truncate:", truncate(sample, 8))
    print("Capitalize:", capitalize_words(sample))
    print("Reverse:", reverse_text(sample))
    print("Character Count:", count_characters(sample))
    print("Remove Extra Spaces:",
          remove_extra_spaces("hello    world"))