# Zaki Zaidan Akbar
# 5007221058
# INTRO TO PROGRAMMING USING PYTHON 6.8

def celciusToFahrenheit(celcius):
    fahrenheit= (9/5)* celcius + 32
    
    return fahrenheit

def fahrenheitToCelcius(fahrenheit):
    celcius = (5/9)* (fahrenheit-32)
    
    return celcius

print("Celcius", "      ", "Fahrenheit", "      ", "|", "Fahrenheit", "      ", "Celcius", "      ")
for i,j in zip(range(31,41), range(120,21,-10)):
    print(i, "          ", round(celciusToFahrenheit(i),2), "             ", "|", j, "             ", round(fahrenheitToCelcius(j),2), "          ")
    #print(fahrenheitToCelcius(i))
    #print(celciusToFahrenheit(i))
