import math

def SN_rate(s, x):
    N = len(s)
    sum_s = 0
    sum_x = 0
    for n in range(N):
        sum_s += s[n]*s[n]
        sum_x += x[n]*x[n]
    ans = 10 * (math.log(sum_s) - math.log(sum_x))
    return ans
