name = input("What is your name? ")
age = int(input("What is your age? "))
boolean = True
while boolean:
  option = int(
      input(
          "Hi " + name +
          " how may I assist you today. Please type in the corresponding number value to proceed the options below\n1. ___________ \n2. ___________ \n3. ___________ \n4. ___________ \n5. Exit \n\nEnter number here: "
      ))

  if option == 1:
    print("Thanks for choosing option 1")
  elif option == 2:
    print("Thanks for choosing option 2")
  elif option == 3:
    print("Thanks for choosing option 3")
  elif option == 4:
    print("Thanks for choosing option 4")
  elif option == 5:
    print("Thank you for using our service! Goodbye and have a great day! ")
    boolean = False
  else:
    print("Please select a valid option.")
