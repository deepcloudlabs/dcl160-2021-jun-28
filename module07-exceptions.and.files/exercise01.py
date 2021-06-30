employees = [
    ("jack shephard", "Sales", 100000, 1978, True),
    ("kate austen", "IT", 200000, 1985, True),
    ("ben linus", "Finance", 150000, 1967, True),
    ("james sawyer", "HR", 70000, 1970, True),
    ("kim kwon", "Sales", 120000, 1986, True),
    ("sun kwon", "IT", 200000, 1969, False),
    ("hugo reyes", "IT", 120000, 1992, True)
]

try:
    with open("employees.csv", mode="w") as myfile:
        for fullname, department, salary, birth_year, is_full_time in employees:
            # text io -> HRF
            myfile.write(
                f"{fullname},{salary},{department},{birth_year},{'FULL_TIME' if is_full_time else 'PART_TIME'}\n")
except PermissionError:
    print("Cannot open/write to file. Try to change permission: chmod +w")
except Exception as err:
    print("Error has occured: " + str(err))
