p = principal = int(input("principal($): "))
r = rate_of_interest = float(input("rate of interest(%): "))
t = number_of_years = int(input("number of years: "))

i = interest = round(p * r / 100 * t, 2)
a = principal_and_interest = p + i
result = "\nAfter " + str(t) + " years at " + str(r) + "%, the investment will be worth $" + str(a)

print(result)
