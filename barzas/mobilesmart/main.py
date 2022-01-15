import re
global str

with open("input.txt", encoding="utf-8") as file:
	file_one = file.readline().strip()

	with open(file_one, encoding="windows-1251") as file:
		str_file = file.read()
		fio = re.findall(r"Фамилия=\"(\w+)\"\sИмя=\"(\w+)\"\sОтчество=\"(\w+)\"", str_file)
		if len(fio) == 0:
			print("Данных не найдено")
			exit(0)

	if (len(fio) > 0):
		with open("output.txt", "w", encoding="utf-8") as out_file:
			i = 0
			for people in fio:
				i = i + 1
				out_file.write(str(i) + ") "+ people[0] + " " + people[1] + " " + people[2] + "\n")

