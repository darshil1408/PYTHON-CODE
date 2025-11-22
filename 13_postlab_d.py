file1 = r"D:\ICT\SEM 3\PWP\LAB CODE\LAB 13\file1.txt.txt"
file2 = r"D:\ICT\SEM 3\PWP\LAB CODE\LAB 13\file2.txt.txt"
merged = r"D:\ICT\SEM 3\PWP\LAB CODE\LAB 13\merged.txt.txt"
with open(file1, "r") as f1, open(file2, "r") as f2, open(merged, "w") as m:
    m.write(f1.read())
    m.write("\n")
    m.write(f2.read())
print("Files merged successfully.")
