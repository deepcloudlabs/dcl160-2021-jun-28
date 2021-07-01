numbers = [4, 8, 15, 16, 23, 42]
print(max(numbers))
complex(1, 2)  # 1+2j

for builtin_module in dir(__builtins__):
    print(builtin_module)

help(numbers)

x = 42

print(isinstance(x, int))

help(x)

# re -> module

# tamamini_ara()
# ayristir()

# import re -> re.fullmatch()

import sys

for a_path in sys.path:
    print(a_path)

print("What are available in 'sys' module:")
for name in dir(sys):
    print(name)

from deepcloudlabs.utils import lost_numbers as nums, is_even as cift_mi

print(nums)
print(cift_mi(42))

import deepcloudlabs.hr

print(dir(deepcloudlabs))
example = {
    "identity": "9876543210",
    "fullname": "kate austen"
}
jack = deepcloudlabs.hr.Employee("12345678910", "jack bauer")

kate = deepcloudlabs.hr.Employee(**example)

print(jack.identity, jack.fullname)
print(kate.identity, kate.fullname)

from deepcloudlabs.dictionary import get_word

print(get_word(42))
