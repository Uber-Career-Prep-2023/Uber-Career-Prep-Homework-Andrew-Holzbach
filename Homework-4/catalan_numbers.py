"""
Using: Tabulation 
O(n) time complexity O(n) space complexity
Took 25 minutes

Proof:
f(0) = 1
f(1) = 1
f(n) = (2n)!/(n+1)!n!
f(n+1) = (2(n+1))!/(n+2)!(n+1)! = ((2n+2)*(2n+1)*(2n)!)/ (n+2)(n+1)!(n+1)(n)!
= f(n) * ((2n+2)*(2n+1))/((n+2)*(n+1)) 

"""

def catalan_nums(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        nums = [1,1]
        for i in range(1, n):
            prior = nums[-1]
            coeff = ((2*i+2)*(2*i+1))/((i+2)*(i+1))
            print(coeff)
            nums.append(coeff*prior)
    return nums

print(catalan_nums(5))