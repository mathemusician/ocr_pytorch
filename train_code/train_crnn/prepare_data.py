"""

This 1) converts image files to a list of text files and 2) transfers their characters to a pickled file.

"""


import os
import config
import pickle as pl
from typing import Any
from pathed import Path, filedir, cwd


def make_text_file(image_dir):
    """
    makes text_file.txt which contains file_paths to images and the corresponding text:

    /absolute/path/to/image_1.jpg\tword_in_image_1
    /absolute/path/to/image_2.jpg\tword_in_image_2
    ...

    you may have to modify this to fit your dataset

    Parameters:
        image_dir: directory that stores images
    Returns:
        path to text_file.txt
    """
    # path to image files
    image_dir = Path(image_dir, custom=True)

    # get valid files
    file_list = [
        filename
        for filename in image_dir.ls()
        if ((os.path.isfile(image_dir / filename)) and (filename != ".DS_Store"))
    ]

    text_list = []

    # files names look like randomnum_word_randomnum.jpg
    for file_name in file_list:
        image_text = file_name.split("_")[1]

        if "." in image_text:
            image_text = image_text.split(".")[0]
        text_list.append(image_dir / (file_name + r"\t" + image_text + "\n"))

    text = "".join(text_list)

    with open(filedir/"text_file.txt", "w") as file_handler:
        file_handler.write(text)

    return filedir / "text_file.txt"


def pickle(data: Any, path: str) -> None:
    """
    one-liner for pickling python objects:
    pickle(data, 'path/to/pickled/file')

    Parameters:
        data: almost any python object
        path: /path/to/pickle/file.pl
    Returns:
        Nothing
    """

    with open(path, "wb") as file_handler:
        pl.dump(data, file_handler)


def unpickle(path: str) -> Any:
    """
    one-liner for retrieving pickled data:
    data = unpickle('path/to/pickled/file')

    Parameters:
        path
    Returns:
        pickled data
    """
    with open(path, "rb") as file_handler:
        return pl.load(file_handler)


def view_pickled_data(path: str) -> str:
    """
    Parameters:
        path to pickled file
    Returns:
        string version of pickled file
    """
    data = unpickle(path)
    print(data)
    return str(data)


def pickle_from_text_file(path: str) -> str:
    """

    makes custom_alphabet.pkl
    custom_alphabet.pkl contains a list of valid characters:

    [
        ' ', 'a', 'b', 'c', ...
    ]

    Parameters:
        path: path to text_file.txt
    Returns:
        path to custom_alphabet.pkl
    """
    words = []
    with open(path, "r") as file_handler:
        lines = file_handler.readlines()
        for line in lines:
            url, word = line.split("\\t")
            word = word.replace("\n", "")
            words.append(word)

    # convert words into a set of characters
    # the set automatically contains one of every item
    words = set([char for char in ("".join(words))])

    pickle([' '] + list(words), filedir/"custom_alphabet.pkl")

    return filedir / "custom_alphabet.pkl"


if __name__ == "__main__":
    path_to_text_file = make_text_file(config.image_dir)
    print(path_to_text_file)
    path_to_pickle = pickle_from_text_file(path_to_text_file)
    print(path_to_pickle)
    view_pickled_data(path_to_pickle)
