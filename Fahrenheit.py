# A simple program to convert degrees Celsius to Fahrenheit

def convert() :
    print("Temperature converter. Use CTRL + C to quit.")

    while True :
        try :
            celsius = float(input("What is the temperature you want to convert to Fahrenheit ? : "))

            if celsius < -273.15 :
                print("You can't go lower than absolute zero")
            elif celsius == -273.15 :
                print("This is absolute zero. Pretty cold...")
            else :
                fahrenheit = celsius * (9/5) + 32
                print(f"This temperature in Fahrenheit is : {fahrenheit:.2f}")

        except KeyboardInterrupt :
            print("\nQuitting program... \nGoodbye ! :D")
            break

convert()