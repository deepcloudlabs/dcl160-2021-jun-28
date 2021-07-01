# DCL-160: Python Programming

These projects are created as part of the following training: DCL-160 "Python Programming"

Please follow the link for the complete training catalog: https://www.deepcloudlabs.com/resources

# Module 10 - Modules and Packages

Python'da bir paket oluşturmak için bir dizin yaratmanız yeterli olacaktır:

![Installation folder](module10-figure01.png?raw=true "package directory content")

Bu dizin yapısı içinde **`__init__.py`** dosyası modül yüklenirken bir kere çalıştırılır ve modülle ilgili başlangıç işlemleri gerçekleştirilir:

```python
print("deepcloudlabs module is loaded!")
# all initialization code goes here

from deepcloudlabs.dictionary import lines

with open("deepcloudlabs/dictionary-tur.txt", "r") as the_file:
    for line in the_file.readlines():
        lines.append(line.strip())
```

Böylelikle modül içindeki **dictionary.py** dosyası içinde tekrar tekrar dosyanın yüklenmesine gerek olmaz:


```python
lines = []


def get_word(index):
    return lines[index]
```

Burada **lines** listesi her zaman modül yüklenirken sözlük dosyası okunarak doldurulur.
