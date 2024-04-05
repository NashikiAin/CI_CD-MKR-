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

def write_to_file(top_words, output_file):
    """
    Function to write the top 10 most common words to an output file.

    Parameters:
    - top_words (list): A list containing tuples of the top 10 most common words along with their frequencies.
    - output_file (str): Path to the output text file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("[Console] Your 10 most popular words with text!: \n \n")
        for word, count in top_words:
            file.write(f"{word}-{count}\n")

if __name__ == "__main__":
    input_file = "Project/input.txt"  
    output_file = "Project/output.txt"  
    top_words = get_top10words(input_file)
    write_to_file(top_words, output_file) 
    print("[Console] Top 10 words have been written to output.txt file. Check your output file =)")