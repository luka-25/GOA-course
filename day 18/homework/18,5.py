items = ["apple", "banana", "avocado", "cherry", "cucumber"]
choice = input("გსურს სიის გასუფთავება? (დიახ/არა): ")

if choice.lower() == "დიახ":
    items.clear()
    print("სია გასუფთავებულია:", items)
else:
    print("სია დარჩა უცვლელი:", items)
