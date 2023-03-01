# Sarah Stephenson and Rosemary Hoffman
def perfect_number(n):
    divisors_sum=0
    for i in range (1, n):
        if n % i==0:
            divisors_sum +=i
    if divisors_sum==n:
        print(n)
    else:
        print("False")
perfect_number(1000)
# print(perfect_number(6))
# print(perfect_number(10000))
