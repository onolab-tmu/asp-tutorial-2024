import numpy as np

def difference_equation(a, b, x):
    def calc_y(n):
        N = a.size
        M = b.size
        sum_a, sum_b = 0
        if n == 0:
            return np.sum(b[k_b] * x[n-k_b])
        else:
            for k_a in range(N):
                sum_a += a[k_a] * calc_y(n-k_a)
        for k_b in range(M):
            if n-k_b < 0:
                continue
            else:
                sum_b += b[k_b] * x[n-k_b]

        return (-sum_a + sum_b) / a[0]
    
    y = np.zeros(x.size)
    for n in range(x.size):
        y[n] = calc_y(n)

    return y
