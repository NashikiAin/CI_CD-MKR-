import pytest
from main import get_top10words, write_to_file


@pytest.fixture
def input_file(tmp_path):
    input_file_path = tmp_path / "test_input.txt"
    with open(input_file_path, 'w', encoding='utf-8') as file:
        file.write("apple orange banana banana orange apple apple mango mango mango mango")
    return input_file_path

def test_get_top10words(input_file):
    expected_output = [('mango', 4), ('apple', 3), ('orange', 2), ('banana', 2)]
    assert get_top10words(input_file) == expected_output


@pytest.mark.parametrize("top_words, expected_content", [
    ([('mango', 4), ('apple', 3), ('orange', 2), ('banana', 2)], "[Console] Your 10 most popular words with text!: \n \nmango-4\napple-3\norange-2\nbanana-2\n"),

])
def test_write_to_file(top_words, expected_content, tmp_path):
    output_file = tmp_path / "test_output.txt"
    write_to_file(top_words, output_file)
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == expected_content
