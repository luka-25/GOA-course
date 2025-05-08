fruits = ["apple", "banana", "cherry", "pear", "kiwi"]
index = int(input("შეიყვანეთ ინდექსი (0-დან იწყება): "))

if 0 <= index < len(fruits):
    fruits.pop(index)
    print("განახლებული სია:", fruits)
else:
    print("არასწორი ინდექსი.")
