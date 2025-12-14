def main():
    x=get()
    if x>=99:
        print("F")
    elif x<=1:
        print("E")
    else:
        print(f"{x}%")        


def get():
    fuel = 0
    while True:      
        try :
            x= input("Fraction: ")
            numerator, denominator = x.split("/")
            if int(numerator) < 0 or int(denominator) <= 0 or int(numerator) > int(denominator):
                raise ValueError("Numerator and denominator must be positive integers and numerator must not exceed denominator.")       
            fuel = int(numerator) / int(denominator)
            break
        except (ValueError, ZeroDivisionError):
            print("Numerator and denominator must be positive integers and numerator must not exceed denominator.")
    return int(fuel*100)            



main()








