total_amount = 10000

amount_to_be_withdrawn = input("Enter the amount to be withdrawn: ")

print("Processing your request...")

try:
    total_amount = total_amount - int(amount_to_be_withdrawn)
    print("Amount withdrawn successfully!")
    print("Your current balance is: ",total_amount)
    print("Thank you for using our service!")
except ValueError:
    print("Invalid input. Please enter a valid number. !!!!!!")
	
	

def divide_numbers(num1, num2):

    try:
        res = num1 / num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else: # This block will execute if no exceptions were raised in the try block.
        print("Division successful.")
    finally: # This block will execute regardless of whether an exception was raised or not.
        print("Execution of the divide_numbers function is complete.")

    return res

print(divide_numbers(11,0))




age_ = int(input("Enter your age: "))

if age_ < 0:
    raise Exception("Age cannot be negative.")
elif age_ > 0 and age_ < 18:
    print("You are a minor.")
elif age_ >= 18 and age_ < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
