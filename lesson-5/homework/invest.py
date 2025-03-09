def invest(amount, rate, years):
    for i in range(years):
        amount=amount+amount*rate
        print(f"year {i+1}: ${amount:.2f}")
amount=float(input("Enter amount: "))
rate=float(input("Enter the annual percentage rate: "))
years=int(input("Number of years: "))
invest(amount,rate,years)