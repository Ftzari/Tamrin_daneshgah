def calc_monthly_payment(p: float, r: float, d: int):
    try:
        r = (r / 100)
        monthly_payment = p * (r*pow(1+r, d))
        monthly_payment = (monthly_payment / pow(1+r, d)-1)/12

    except ZeroDivisionError:
        n = d * 12
        monthly_payment = p / n
    return monthly_payment


p = float(input("Input Principal: "))
r = float(input("Input Rate: "))
d = float(input("Input Duration: "))
print(calc_monthly_payment(p, r, d))

#fatemeh tazari
#Sunday. 7:45  ~  10

