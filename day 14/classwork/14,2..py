names = []
for i in range(5):
    name = input(f"შეიყვანეთ {i+1}-ე სახელი: ")
    names.append(name)

for name in names:
    if len(name) > 5:
        print(name + " მეტია 5 ასოზე. ")
    