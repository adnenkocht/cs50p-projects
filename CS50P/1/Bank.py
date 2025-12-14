x=input("The greeting:")
x=x.strip()
if x.lower().startswith("hello"):
    print("0$")
elif x.lower().startswith("hey"):
    print("20$") 
else: print("100$")       

