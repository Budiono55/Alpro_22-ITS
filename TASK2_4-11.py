# Zaki Zaidan
# 5007221058

# find the days in the month. 
# use "determining leap year", months data
# for future development, input validator need to be applied.

DATA_MONTHS={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:31,
    7:30,
    8:31,
    9:31,
    10:30,
    11:31,
    12:30}

MONTHS_NAME={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December",
}

def YearAuth(YEAR_INPUT):
    LeapYear = (YEAR_INPUT % 4 ==0)
    # if LeapYear == True:
    #     print("Leap")
    # else:
    #     print("Ori")
    return LeapYear

print(" --------------- NUMBER OF the DAYs FINDER ---------------")
YEAR_INPUT = eval(input("Desired Year: "))
MONTH_INPUT = int(input("Type ur desired month in number: "))

YearAuth(YEAR_INPUT)

# Months check
if MONTH_INPUT in DATA_MONTHS:
    # Leap check
    if YearAuth(YEAR_INPUT) == True:
        DATA_MONTHS[2] = 29
    print(MONTHS_NAME[MONTH_INPUT], "in", YEAR_INPUT, "has", DATA_MONTHS[MONTH_INPUT], "days")
else:
    print("This is earth. not Jupiter.")
    


#print(YearAuth(YEAR_INPUT))
