# This script asks a person for their weight and then provides their weight on the Moon, Mars, and Jupiter
# (Let's prentend that you can acutally stand on the surface of Jupiter)

# Ask for the user's weight on Earth and specify to the interpreter that the input will be a floating point number.
weight_earth = float(input("Enter your weight on Earth (in pounds): "))

# Predefined weight factors relative to Earth
factor_moon = 0.165 # In other words, mulitplying your weight by 0.165 provides your weight on the moon
factor_mars = 0.378
factor_jupiter = 2.528

# Calculate weights using the factors
weight_moon = weight_earth * factor_moon
weight_mars = weight_earth * factor_mars
weight_jupiter = weight_earth * factor_jupiter

# Display results
# \n tells the interpreter to skip a line before printing.
print("\nYour weight on other worlds using separate calculations and default format for the floating point output:") # \n tells the interpreter to skip a line before printing this line.
# The "f" at the beginning of the print statement represents an f-string. It allows you to insert variable results into your print statements.
print(f"Moon: {weight_moon} lbs") 
print(f"Mars: {weight_mars} lbs")
print(f"Jupiter: {weight_jupiter} lbs")

# .2f is a feature of f-strings and tells the interpreter to print the float with a specific number of decimal places
print("\nYour weight on other worlds using separate calculations and formating for two decimal places:")
print(f"Moon: {weight_moon:.2f} lbs") 
print(f"Mars: {weight_mars:.2f} lbs")
print(f"Jupiter: {weight_jupiter:.2f} lbs")


print("\nYour weight on other worlds using calculations inside the print statements and formatting for the floating point output:")
print(f"Moon: {weight_earth * factor_moon:.2f} lbs") 
print(f"Mars: {weight_earth * factor_mars:.2f} lbs")
print(f"Jupiter: {weight_earth * factor_jupiter:.2f} lbs")