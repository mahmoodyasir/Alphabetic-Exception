class AlphabeticException(Exception):
    pass


value = input()
isNum = True

try:
    float(value)
except ValueError:
    isNum = False

if isNum:
    try:
        if type(float(value)) == int or type(float(value)) == float:
            raise AlphabeticException
    except AlphabeticException:
        print("Please enter an alphabet")
else:
    print("It is string")
