#Convert Feet and Inches into Meters and Centimeters

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12) + inches
total_cmeters = total_inches * 2.54

meter = total_cmeters /100

print('Meters,', total_cmeters, 'Centimeters,', meter)