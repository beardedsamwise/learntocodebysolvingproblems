# https://dmoj.ca/problem/wc17c1j2

def convert_to_faranheit(celcius):
    celcius = int(celcius)
    if  (-40 <= celcius <= 40):
        faranheit = celcius / (5 / 9) + 32
        return faranheit
    else:
        raise ValueError("The temperature in F must be between -40 and 40 degrees")

celcius = input()

print(convert_to_faranheit(celcius))