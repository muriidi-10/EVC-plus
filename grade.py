
try:
    dhibcaha = float(input("Fadlan geli dhibcaha aad keentay (0-100): "))

    if dhibcaha < 0 or dhibcaha > 100:
        print("Khalad: Fadlan geli tiro u dhaxaysa 0 iyo 100.")
    else:
        
        total_marks = 100
        percentage = (dhibcaha / total_marks) * 100

  
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F (Wuu dhacay)"

    
        print("-" * 30)
        print(f"Natiijada: {percentage}%")
        print(f"Darajada: {grade}")
        print("-" * 30)

except ValueError:
    print("Khalad: Fadlan geli tiro (number) oo keliya.")