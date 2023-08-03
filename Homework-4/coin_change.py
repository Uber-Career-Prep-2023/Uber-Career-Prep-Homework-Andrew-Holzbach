"""
Tried tabulation and then thinking about memoization, ended up not finished after 40 minutes :(
"""
def change(coins, msum):
    """
    tab = {}
    tab[0] = 1
    for psum in range(1,msum+1):
        tab[psum] = 0
        for coin in coins:
            if psum - coin >= 0:
                tab[psum] += tab[psum-coin]
        print(psum,tab[psum])
    return tab[msum]
    """
    num_coins = len(coins)
    memo = {}
    counter = tuple()
    for _ in range(num_coins):
        counter = counter + tuple(0)


    

print(change([2,5,10],20))

