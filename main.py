print(
    "Hey there! I am the Elite101 Prework chatbot. Nice to meet you!\n________________________________________\n\n\n"
)
name = input("What is your name? ")
age = int(input(f"Hi {name}. Could you please enter your age here: "))
print(
    f"Oh what I would do to become {age} again. Anyways, {name} how may I assist you today?"
)
boolean = True
while boolean:
  option = int(
      input(
          f"\n\nPlease type in the corresponding number value to proceed the options below\n1. ___________ \n2. ___________ \n3. ___________ \n4. ___________ \n5. Exit \n\nEnter number here: "
      ))

  if option == 1:
    print("\n\nThanks for choosing option 1\n\n")
  elif option == 2:
    print("\n\nThanks for choosing option 2\n\n")
  elif option == 3:
    print("\n\nThanks for choosing option 3\n\n")
  elif option == 4:
    print("\n\nThanks for choosing option 4\n\n")
  elif option == 5:
    print(
        f"Thank you {name} for using our service! Goodbye and have a great day! "
    )
    boolean = False
  else:
    print("\n\nPlease select a valid option.")
