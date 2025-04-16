def celcius_to_fran(celcius):
    return ((celcius * 9/5) + 32)

try:
    print("Type the Celcius value :")
    cel = int(input())
    result = celcius_to_fran(cel)
    print(f"Fran = {result}")
except err:
    print("Invalid value")
