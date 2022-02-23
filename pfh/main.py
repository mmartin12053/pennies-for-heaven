




# from re import L


def main():
    p = int(input("how many pennies do you have:\n"))
    dollars = 0
    half = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0


    while p > 0:
        if p >= 100:
            p -= 100
            dollars += 1
            print(p)
        # elif p >= 50:
        #     p -= 50
        #     half +=1
        elif p >= 25:
            p -=25
            quarters += 1
            print(p)
        elif p >= 10:
            p-=10
            dimes += 1
            print(p)
        elif p >= 5:
            p-=5
            nickels+=1
            print(p)
        else:
            pennies += p
            p=0

    print(f"""dollars: {dollars}
    half-dollars: {half}
    quarters: {quarters}
    dimes: {dimes}
    nickels: {nickels}
    pennies: {pennies}""")

    main()
main()