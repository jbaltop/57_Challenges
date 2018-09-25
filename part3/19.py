def main():
    w = float(input("weight(lb): "))
    h = float(input("height(in): "))

    bmi = (w / (h * h)) * 703

    message1 = "\nyour bmi: " + str(bmi)

    if bmi > 18.5 and bmi < 25:
        message2 = "\nYou are within the ideal weight range."
    else:
        message2 = "\nYou are overweight. You should see your doctor."

    print(message1, message2)


main()
