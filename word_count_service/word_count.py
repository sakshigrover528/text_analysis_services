from collections import Counter
from shared_resources.preprocess_text import preprocess_text


def count(text: str) -> int:
    """
    Counts the occurrences of each word in the text.

    Args:
        text (str): The input text.

    Returns:
        Total number of words in the text.
    """
    # get tokenized text from the input 
    words = preprocess_text(text)

    return len(words)
