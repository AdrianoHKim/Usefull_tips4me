# 9. read file into list

names = [line.strip() for line in open("names.txt", "r")]

print(names)
