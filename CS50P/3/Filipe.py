Filipe={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    sum=0
    print("Welcome to Filipe's restaurant")
    while True:
        try:
            print("Please enter your order (or press Ctrl+Z to finish):")
            order = input("Item: ").strip().title()
            if order in Filipe:
                sum=Filipe[order]+sum
                print(f"{Filipe[order]:.2f}$ and the total is {sum:.2f}$")
            else:
                print("Item not found")   
            
        except EOFError:  
            print(f"the order is over. The total is:{sum:.2f} $")
            break
        
main()


    