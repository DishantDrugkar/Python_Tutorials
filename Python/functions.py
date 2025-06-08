# Calculate average of Three Numbers
def sum(a, b, c) :
    add = a + b + c / 3

    return add
 
print(sum(93, 94, 97)) 


# Factorial Number

def fact(n) :
    fact_no = 1
    for i in range(1, n + 1):
        fact_no = fact_no * i

    print(fact_no)

fact(5)

# Currency Converter USD to INR

def currency(usd_val) :
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val , "INR")

currency(1)