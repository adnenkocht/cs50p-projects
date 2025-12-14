def main():
    name:str=input("camel case: ")
    name=snake_case(name)
    print(f"snake case: {name}")


def snake_case(name:str)-> str:
    snake:str=""
    for letter in name:
        if letter!=letter.upper():
            snake=snake+letter
        else:
            snake=snake+"_"+letter.lower()  
    return snake


main()