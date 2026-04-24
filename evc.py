
try:
    user_input = int(input("Enter a password: ")) 

 
    if user_input == 1234:
        print("Password-ku waa sax!")
        
        options = ["1. Anfac gudaha", "2. Anfac dibada"]
        print("\nMid door:")
        print("\n".join(options))
        user_choice = input("> ")

        if user_choice == "1":
            xirmo = ["1. 1 USD", "2. 2 USD", "3. 5 USD"]
            print("\nFadlan dooro xirmo:")
            print("\n".join(xirmo))
            xirmo_choice = input("> ")

            if xirmo_choice == "1":
                xaqiijin = ["1. Haa", "2. Maya"]
                print("\nMa hubtaa inaa ku shubatid xirmada 1 USD?")
                print("\n".join(xaqiijin))
                text = input("> ")

                if text == "1":
                    print("\nHanbalyo! Waxaad heshey 100 daqiiqo.")
                else:
                    print("\nHowshii waa la joojiyay. Macsalaamo.")

    else:
        print("KHALAD: Password-ka aad gelisay waa khaldan yahay!")

except ValueError:
    print("KHALAD: Fadlan geli lambar oo keliya (Tusaale: 1234)!")