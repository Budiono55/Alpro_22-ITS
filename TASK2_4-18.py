# Zaki Zaidan
# 5007221058

# USD and IDR Money Exchanger

# USD to IDR converter function
def USDtoIDR(rate):
    AMOUNT_INPUT= eval(input("Enter the USD amount: "))
    result = AMOUNT_INPUT * rate
    print(AMOUNT_INPUT, "US Dollar is Rp", result)

# IDR to USD converter function
def IDRtoUSD(rate):
    AMOUNT_INPUT= eval(input("Enter the IDR amount: "))
    result = AMOUNT_INPUT / rate
    print(AMOUNT_INPUT, "Rupiah is $", result)

print("Exchange rate info")
print("USD to IDR = 15503")
RATE_INPUT = eval(input("Enter the exchange rate from dollars to IDR: "))
MODE_INPUT = int(input("Enter 0 to convert dollars to IDR and 1 vice versa: "))

if MODE_INPUT == 0:
    USDtoIDR(RATE_INPUT)
elif MODE_INPUT == 1:
    IDRtoUSD(RATE_INPUT)
else:
    print("Incorrect input")