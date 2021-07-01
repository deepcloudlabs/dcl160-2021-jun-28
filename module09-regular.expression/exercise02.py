import re

pattern1 = r"\w{11,}"  # words longer than 12-char
pattern2 = "^[^iuoea]+$"
pattern3 = r"^[iuoea]\w*[iuoea]$"
pattern4 = r"\wa\w|\w{2}a\w{2}|\w{3}a\w{3}"
pattern_list = []
for i in range(1, 9):
    start = "\\w{" + str(i) + "}"
    pattern_list.append(start + "a" + start)

pattern5 = "|".join(pattern_list)

print(pattern_list)
with open("dictionary-tur.txt", mode="r") as myfile:
    words_longer12 = []
    for word in myfile.readlines():
        striped = word.strip()
        if re.fullmatch(pattern5, striped):
            words_longer12.append(striped)
    words_longer12.sort(key=len, reverse=True)
    for word in words_longer12:
        print(f"{word}:{len(word)}")
    print(len(words_longer12))
