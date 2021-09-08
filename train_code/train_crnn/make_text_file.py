"""

text_file.txt contains file_paths to images and the correseponding text. It looks like this:

/absolute/path/to/image_1.jpg\tword_in_image_1
/absolute/path/to/image_2.jpg\tword_in_image_2
...

you will have to modify this to fit your dataset
"""

from pathed import Path
import os

file_dir = Path("/Users/mosaicchurchhtx/Desktop/1", custom=True)

# get valid files
file_list = [
    filename
    for filename in file_dir.ls()
    if ((os.path.isfile(file_dir / filename)) and (filename != ".DS_Store"))
]


text_list = []

for file_name in file_list:
    image_text = file_name.split("_")[1]
    text_list.append(file_dir / (file_name + r"\t" + image_text + "\n"))


text = "".join(text_list)

with open("text_file.txt", "w") as file_handler:
    file_handler.write(text)
