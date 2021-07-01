print("deepcloudlabs module is loaded!")
# all initialization code goes here

from deepcloudlabs.dictionary import lines

with open("deepcloudlabs/dictionary-tur.txt", "r") as the_file:
    for line in the_file.readlines():
        lines.append(line.strip())