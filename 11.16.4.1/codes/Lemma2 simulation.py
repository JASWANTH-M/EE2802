from math import comb

def binomial_expansion(R, B, n):
    sum = 0
    for k in range(R+1):
        for m in range(B+1):
            if (m+k == n):
                sum += (comb(R, k) * comb(B, m))

    return sum

R = 10
B = 3
n = 4
result = binomial_expansion(R, B, n)
print(result)

# Expected result according to the formula
expected_result =  comb(R+B, n)
print(expected_result)

if result == expected_result:
    print("The binomial expansion is verified.")
else:
    print("The binomial expansion is not verified.")