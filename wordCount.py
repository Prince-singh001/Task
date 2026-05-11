filename = input("Enter file name: ")

try:
    file = open(filename, "r")

    content = file.read()

    words = content.split()

    print("Total words in file:", len(words))

    file.close()

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("Something went wrong:", e)