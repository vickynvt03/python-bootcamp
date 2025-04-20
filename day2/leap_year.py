try:
    num = int(input("Enter the year; "))
    if num % 4 == 0:
              print(f"The year {num} is a leap year")
    else:
        print(f"The year {num} is not a leap year")
except ValueError:
    print("error in year value")
except:
    print("Invalid value")

