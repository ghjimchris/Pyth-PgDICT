gender = input("Enter your gender (M/F): ")
for i in gender:
    if i.upper() == 'M':
        print("You are male.")
    elif i.upper() == 'F':
        print("You are female.")
    else:
        continue
    print(i, end=" ")