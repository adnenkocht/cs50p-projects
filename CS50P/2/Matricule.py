def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    if len(s)>6 or len(s)<2:
        return False
    if s[0].isdecimal() or s[1].isdecimal():
        return False
    if s.isalpha():
        return True
    number=False
    for ch in s:
        if not(ch.isalpha()) and number==False:
            number= True
            if ch=="0":
                return False
        if ch.isalpha() and number==True:
            return False    
    
      
                           
    return True

main()