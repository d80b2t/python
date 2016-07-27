phoneBook = {}

for n in range(int(eval(input()))):
    entry = eval(input())
    phoneBook[entry.split()[0]] = entry.split()[1]

while True:
    try:
        name = eval(input())
        print((name + '=' + phoneBook[name] if phoneBook.get(name) else "Not found"))
    except:
        break

