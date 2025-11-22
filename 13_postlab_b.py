filename = "ict.txt"
lines_list = []
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        lines_list.append(line)
print("List of lines:")
print(lines_list)
