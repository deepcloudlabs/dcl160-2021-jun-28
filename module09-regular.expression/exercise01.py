import re

meyveler = ["elma", "kiraz", "kivi", "muz", "karpuz", "kavun", "seftali"]

pattern1 = "^[kK][a-zA-Z]*[zZ]$"  # Language: "kz", "kaz", "kabz", ...
pattern2 = "k+"  # k, kk, kkk, kkkk, ...
pattern3 = ".+i.+"
pattern4 = r"\d{11}"
pattern5 = r"\w{6,}"
pattern6 = r"\w{6}\w*"

empty_line_pattern = "^$"
empty_string = ""

# \d -> digit: [0-9]
# \w -> alphabet character: [a-z]
# \s -> white space: [ \t\r\n]

for meyve in meyveler:
    if re.fullmatch(pattern5, meyve.lower()):
        print(meyve)

tc_kimlik_no = "1234567891012"
if re.fullmatch(pattern4, tc_kimlik_no):
    print(f"{tc_kimlik_no} is a valid identity no!")
else:
    print(f"{tc_kimlik_no} is NOT a valid identity no!")

message = "1                  2         3             4     5         "
print(re.sub(r"\s+", " ", message.strip()))
print(re.split(r"\s+", message.strip()))

contact = "Jack Bauer, Home: 555-555-6789, Work: 555-555-1234-30"
result = re.search(r"(\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}-\d{2})", contact)
print(result.groups())
print(result.group(1))
