

def zodiac_sign_identifier():
    while True:
        print("Type your birthday and get your zodiac sign!🤩🤔 ")
        month = input("Enter your birth month ").strip().lower()
        date = int(input("Enter your birth date "))

        if(month == "may" and date >= 21)  or (month == "june" and date <= 20):
            print("You are a GEMINI👬♊")
        elif(month == "march"  and date >= 21) or (month == "april" and date <= 19):
            print("You are a ARIES!♈🐏")
        elif (month == "april" and date >= 20) or (month == "may" and date <= 20):
            print("you are a TAURUS!♉🐂")
        elif(month == "june" and date >= 21) or (month == "july" and date <= 22):
            print("you are a CANCER!♋🦀")
        elif(month == "july" and date >= 23) or (month == "august" and date <= 22):
            print("you are a LEO!♌🦁")
        elif(month == "august" and date >= 23) or (month == "september" and date <= 22):
            print("you are a VIRGO!♍👧")
        elif(month == "september" and date >= 23) or (month == "october" and date <= 22):
            print("you are a LIBRA!♎⚖")
        elif(month == "october" and date >=23) or (month == "november" and date <= 21):
            print("you are a SCORPIO!♏🦂")
        elif(month == "november" and date >= 22) or (month == "december" and date <= 21):
            print("you are a SAGITTARIUS!♐🏹")
        elif(month == "december" and date >= 22) or (month == "january" and date <= 19):
            print("you are a CAPRICORN!♑🐐")
        elif(month == "january" and date >= 20 ) or (month == "february" and date <= 18):
            print("you are a AQUARIUS!♒🏺")
        elif(month == "february" and date >= 19) or (month == "march" and date <= 20):
            print("you are a PISCES🐟♓")
        else:
            print("Invalid month!")

zodiac_sign_identifier()