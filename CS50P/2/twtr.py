def main():
    word:str=input("give the word to shorten: ")
    voy=['A', 'E', 'I', 'O','U']
    shrtd:str=""
    for letter in word:   
        if not(letter.upper() in voy):
            shrtd=shrtd+letter
    print(f"the word becomes {shrtd}")
main()    