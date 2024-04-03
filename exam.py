try:
    number = int(input("Enter a number "))
    result = 10/number
    print(result)
except Exception as e:
    print("Error:Some exception has occurred.")
else:
    print("No exceptions found.")
finally:
    print("Program execution has ended.")