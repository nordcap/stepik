import re

with open("input.txt", encoding="utf-8") as file:
    file_one = file.readline().strip()
    file_two = file.readline().strip()
    with open(file_one, encoding="windows-1251") as file_one, open(file_two, encoding="windows-1251") as file_two:
        str_in_file_one = file_one.read()
        str_in_file_two = file_two.read()
        passport_one = re.findall(r"СерНомДок=\"([\d|\s]+)\".+\n.*Фамилия=\"(\w+)\"\sИмя=\"(\w+)\"\sОтчество=\"(\w+)\"", str_in_file_one)
        passport_two = re.findall(r"СерНомДок=\"([\d|\s]+)\".+\n.*Фамилия=\"(\w+)\"\sИмя=\"(\w+)\"\sОтчество=\"(\w+)\"", str_in_file_two)

        if len(passport_one) == 0:
            print("Данных в первом списке не найдено")
            exit(0)
        if len(passport_two) == 0:
            print("Данных во втором списке не найдено")
            exit(0)

        if (len(passport_one) > 0 and len(passport_two) > 0):
            with open("output.txt", "w", encoding="utf-8") as out_file:
                i = 0
                for people_one in passport_one:
                    for people_two in passport_two:
                        if (people_one[1].upper() == people_two[1].upper() and people_one[2].upper() == people_two[2].upper() and people_one[3].upper() == people_two[3].upper()):
                            str1 = "".join(people_one[0].split())
                            str2 = "".join(people_two[0].split())
                            if (str1 != str2):
                                i = i + 1
                                out_file.write(str(i) + ") " + people_one[1] + " " + people_one[2] + " " + people_one[3] + "\nПаспорт: " + people_one[0] + " сменился на " + people_two[0] + "\n")
                if i == 0:
                    out_file.write("Различий не найдено")
