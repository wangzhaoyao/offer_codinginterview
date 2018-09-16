def dp_probability(n, s, dmax = 6, dmin = 1):
    if s < n * dmin or s > n * dmax :
        return 0
    dp1 = [0] * (n * dmax + 1)

    for i in range(1, dmax + 1):
        dp1[i] = 1
    print (dp1)

    for i in range(2, n + 1):
        dp2 = [0] * (n * dmax + 1)
        for j in range(dmin * i, dmax * i + 1):#(n-6n)
            for k in range(dmin, dmax + 1):#(1-6)
                if j > k :
                    dp2[j] += dp1[j - k]
        print (dp2)
        dp1 = dp2
    print ("total = {0}, prob = {1}%".format(dp2[s], dp2[s]*100/dmax**n))
    return dp2[s]
dp_probability(5,10)