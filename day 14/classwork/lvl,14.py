nums = []
for i in range(10):
    user_num = int(input(F"შეიყვანეთ {i+1}-ე რიცხვი: "))
    nums.append(user_num)

for user_num in nums:
    if user_num % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")