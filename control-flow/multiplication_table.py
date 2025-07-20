number = int(input("Enter a number to see its multiplication table:"))

for factor in range(1,11):
    print(f"{number} * {factor} = {factor * number}")