from collections import Counter
import re

def get_top10words(file_path):
    """
    Function to extract the top 10 most common words from a text file.

    Parameters:
    - file_path (str): Path to the input text file.

    Returns:
    - list: A list containing tuples of the top 10 most common words along with their frequencies.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return Counter(words).most_common(10)

