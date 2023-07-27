def main():
    print("This program converts us dollars to Pounds Sterling")
    print()

    dollars = eval(input("Enter  amount "))

    pounds =  convert_to_pounds(dollars)

    print("This is",  pounds, "pounds.")

convert_to_pounds = lambda  dollars: dollars *0.82

main()
