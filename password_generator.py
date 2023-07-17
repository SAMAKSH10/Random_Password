import string
import random

input_length = int(input("Enter the length of password: "))
mix=""

print("Enter the combination of password: \n"
      "1. Letters\n"
      "2. Digits\n"
      "3. Special Characters\n"
      "4. All of the above\n"
      "5. Done\n")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mix += string.ascii_letters
        
    elif choice == 2:
        mix += string.digits
        
    elif choice == 3:
        mix += string.punctuation
        
    elif choice == 4:
        mix += string.ascii_letters + string.digits + string.punctuation
        
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
print("Your password is: ", end="")
for i in range(input_length):
    print(random.choice(mix), end="")