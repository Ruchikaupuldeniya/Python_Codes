def greet(f_name,l_name):
    print(f"Hi {f_name} {l_name}")
    print("Welcome aboard")
    
    
    
greet("Ruchika","Harshajith")


def multiply(*number):
    total = 1
    for number in number:
        total*=number
    return total

print(multiply(2,3,4,5))