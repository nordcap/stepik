"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке."""
with open("2.4-1.txt", "r") as input_file, open("2.4-1-out.txt", "w") as out_file:
    arr = []
    for line in input_file:
        arr.append(line.strip())
    arr.reverse()
    out = "\n".join(arr)
    out_file.write(out)
