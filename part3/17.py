a = alcohol_consumption = float(input("alcohol consumption(oz): "))
w = weight = float(input("weight(lb): "))
g = gender = input("gender(m/f): ")
h = elapsed_time_to_drink_alcohol = float(input("elapsed time to drink alcohol(h): "))
bac_limit = 0.08

if gender.lower() == 'm' or gender.lower() == "male":
    r = 0.73
elif gender.lower() == 'f' or gender.lower() == "female":
    r = 0.6
else:
    print("please enter a correct gender.")

bac = blood_alcohol_content = (a * 5.14 / w * r) - 0.015 * h

if bac >= 0:
    message1 = "\nyour blood alcohol content: " + str(bac)
else:
    message1 = "\nyour blood alcohol content: 0"

if bac < bac_limit:
    message2 = "\nIt is legal for you to drive."
else:
    message2 = "\nIt is not legal for you to drive."

print(message1, message2)
