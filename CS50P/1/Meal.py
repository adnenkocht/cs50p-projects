def main():
    n=input("give time  ")
    hours=convert(n)
    if 7.0 <= hours <= 8.0:
        print("breakfast")
    elif 12.0 <= hours <= 13.0:
        print("lunch")
    elif 18.0 <= hours <= 19.0:
        print("dinner")  

    


def convert(time):
    t=float(time[:time.find(":")])+int(time[time.find(":")+1:])/60
    return t
    


if __name__ == "__main__":
    main()