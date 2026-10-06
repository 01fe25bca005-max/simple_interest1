def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Input
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

# Calculate
si = simple_interest(p, r, t)

print("Simple Interest =", si)
