
with open("notes.txt", "w") as f:
    f.write("Hello\nI am learning Python\n")


with open("notes.txt", "r") as f:
    print(f.read())
