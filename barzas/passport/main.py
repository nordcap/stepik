import re

with open("input.txt") as file:
    file_one = file.readline().strip()
    file_two = file.readline().strip()
    with open(file_one, encoding="windows-1251") as file_one, open(file_two, encoding="windows-1251") as file_two:
        str_in_file_one = file_one.read()
        str_in_file_two = file_two.read()
        passport_one = re.findall(r"СерНомДок=\"(\d{2}\s\d{2}\s\d{6})\".+\n.*Фамилия=\"([А-Я]+)\"\sИмя=\"([А-Я]+)\"\sОтчество=\"([А-Я]+)\"", str_in_file_one)
        passport_two = re.findall(r"СерНомДок=\"(\d{2}\s\d{2}\s\d{6})\".+\n.*Фамилия=\"([А-Я]+)\"\sИмя=\"([А-Я]+)\"\sОтчество=\"([А-Я]+)\"", str_in_file_two)

        if (len(passport_one) > 0 and len(passport_two) > 0):
            with open("output.txt", "w", encoding="utf-8") as out_file:
                i = 0
                for people_one in passport_one:
                    for people_two in passport_two:
                        if (people_one[1] == people_two[1] and people_one[2] == people_two[2] and people_one[3] == people_two[3]):
                            if (people_one[0] != people_two[0]):
                                i = i + 1
                                out_file.write(str(i) + ") " + people_one[1] + " " + people_one[2] + " " + people_one[3] + "\nПаспорт: " + people_one[0] + " сменился на " + people_two[0] + "\n")
