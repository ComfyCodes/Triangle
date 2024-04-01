def triangle_type(a, b, c):
    if a == b == c:
        return "Enakostranični trikotnik"
    elif a == b or b == c or a == c:
        return "Enakokraki trikotnik"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Pravokotni trikotnik"
    else:
        return "Raznostranični"
def main():
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        
        
        if a > 100 or b > 100 or c > 100:
            print('Value limit: 100.')        
        elif a <= 0 or b <= 0 or c <= 0:
            print("Invalid input, value must be positive")
        elif a + b <= c or a + c <= b or b + c <= a:
            print("Invalid input, The sum of any two sides must be greater than the third side.")
        else:
            triangle = triangle_type(a, b, c)
            print("The triangle is:", triangle)
    except ValueError:
        print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()