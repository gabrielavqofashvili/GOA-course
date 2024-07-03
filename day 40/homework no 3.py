# ლუწი რიცხვებისთვის ცარიელი სია
even_numbers = []

# კენტი რიცხვებისთვის ცარიელი სია
odd_numbers = []

while True:
    try:
        num = int(input("შეიყვანეთ რიცხვი (შეწყვეტაა 'q' დაწერეთ): "))
        if num == 'q':
            break
        elif num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    except ValueError:
        print("შეცდომა: გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")

# ლუწი და კენტი რიცხვების დაბეჭდვა
print("ლუწი რიცხვების სია:", even_numbers)
print("კენტი რიცხვების სია:", odd_numbers)
