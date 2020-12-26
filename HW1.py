val1 = input("Enter string value: ")
val2 = int(input("Enter integer value: "))
val3 = float(input("Enter float value: "))
val4 = bool(input("Enter bool value: "))
val5 = input("Enter the list value: ")
val5 = val5.split()

tval1 = type(val1)
tval2 = type(val2)
tval3 = type(val3)
tval4 = type(val4)
tval5 = type(val5)

print(f"""
First Value  : {val1} -- Type: {str(tval1)[8:-2]}
Second Value : {val2} -- Type: {str(tval2)[8:-2]}
Third Value  : {val3} -- Type: {str(tval3)[8:-2]}
Fourth Value : {val4} -- Type: {str(tval4)[8:-2]}
Fifth Value  : {val5} -- Type: {str(tval5)[8:-2]}
""")