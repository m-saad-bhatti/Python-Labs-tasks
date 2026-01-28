while True:  # Infinite loop to keep the program running
    print("\n***** Typecasting *****")
    print("1. Float to Integer")
    print("2. Integer to Float")
    print("3. Int/Float to String")
    print("4. Convert to a List")
    print("5. Exit Program") 
    choice = input("Enter your choice (1-5): ")    
    if choice == '1':
        a = input("Enter a Float value: ")
        f = eval(a)
        print('Current type:', type(f))
        i = int(f)
        print("After conversion:", i, "type is", type(i))    
    elif choice == '2':
        input2 = input("Enter an Integer Value: ")
        e = eval(input2)
        print('Current type:', type(e))
        i = float(e)
        print("After conversion:", i, "type is", type(i))    
    elif choice == '3':
        input3 = input("Enter a value (int/float): ")
        ev = eval(input3)
        print('Current type:', type(ev))
        str_value = str(ev)
        print("After conversion:", str_value, "type is", type(str_value))    
    elif choice == '4':
        input4 = input("Enter some values (int/str/float, separated by spaces): ")
        values = input4.split()  # Splitting input into a list of values
        print("Converted to a list:", values, "type is", type(values))    
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and program    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

