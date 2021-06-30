calisanlar = []
try:
    with open("employees.csv", mode="r") as myfile:
        for line in myfile.readlines():
            fullname, salary, department, birth_year, is_full_time = line.strip().split(",")
            fullname = fullname.title()
            salary = float(salary)
            birth_year = int(birth_year)
            is_full_time = is_full_time == "FULL_TIME"
            calisanlar.append((fullname, salary, birth_year, department, is_full_time))
except PermissionError:
    print("Cannot open/write to file. Try to change permission: chmod +w")
except Exception as err:
    print("Error has occured: " + str(err))
for calisan in calisanlar:
    print(calisan)
