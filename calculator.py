def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
print(__name__)

# print("THis is a simple calculator")
#
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
#
# print(f"the sum is: {add(num1,num2)}")
# print(f"the difference  is: {subtract(num1,num2)}")
#if imported name = module name
#if not imported name = __main__
#if __name__ == "__main__":

if __name__ == "__main__":
    print("THis is a simple calculator")

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    print(f"the sum is: {add(num1,num2)}")
    print(f"the difference  is: {subtract(num1,num2)}")
#this module will run only from the file and not via import
#print__main
#only want to run the code directly not while importing the module