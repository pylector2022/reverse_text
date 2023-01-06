"""

"""
import pathlib


def reverse_string(string_: str) -> str:
    """

    :param string_:
    :return:
    """
    if not isinstance(string_, str):
        raise TypeError(f'Got {type(string_)}, expected string')
    new_words = []
    for word in string_.split():
        new_word = []
        nonletters = []
        for index, char in enumerate(word):
            if char.isalpha():
                new_word.append(char)
            else:
                nonletters.append((index, char))
        new_word = new_word[::-1]
        for item in nonletters:
            new_word.insert(*item)
        new_words.append(''.join(new_word))
    return ' '.join(new_words)


def read_text_from_file(path: pathlib.Path) -> list:
    """

    :param path:
    :return:
    """
    with open(path) as f:
        return f.readlines()


def write_text_into_file(path: pathlib.Path, text: str) -> None:
    """

    :param path:
    :param text:
    :return:
    """
    with open(path, 'w') as f:
        f.writelines(text)


def reverse_text_from_file(input_path: str, reversed_filename: str ='reversed.txt'):
    """

    :param input_path:
    :param reversed_filename:
    :return:
    """
    if not isinstance(input_path, str):
        raise TypeError(f'Got {type(input_path)}, expected string')
    if not isinstance(reversed_filename, str):
        raise TypeError(f'Got {type(reversed_filename)}, expected string')
    path = pathlib.Path(input_path)
    reversed_lines = []
    lines = read_text_from_file(path)
    for text in lines:
        reversed_lines.append(reverse_string(text))
    new_path = path.absolute().parent
    write_text_into_file(new_path / reversed_filename, '\n'.join(reversed_lines))


if __name__ == '__main__':
    ...
