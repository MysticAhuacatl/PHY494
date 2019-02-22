# HW02 2.2

T_K = float(input("Temperature in Kelvin --> "))
theta_F = float(input("Temperature difference in Fahrenheit --> "))

delta_T_K = 5/9 * theta_F
T_total = T_K + delta_T_K

print("Total T " + str(T_total) + " K")
