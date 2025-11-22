filename = "file.txt"
with open(filename, "r") as file:
    content = file.read()
lines = content.split("\n")
num_lines = len(lines)
words = content.split()
num_words = len(words)
num_chars = len(content)
print("Number of lines:", num_lines)
print("Number of words:", num_words)
print("Number of characters:", num_chars)
