def auto_dp(func, cache=1000):
    stat_list = list()
    stat_dict = dict()
    value_dict = dict()
    def new_func(*args):
        poped = None
        if len(stat_list) >= cache:
            poped = stat_list.pop(0)
        if poped is not None:
            stat_dict[poped] -= 1
            if stat_dict[poped] == 0:
                del stat_dict[poped]
                del value_dict[poped]
        if args in stat_dict:
            stat_dict[args] += 1
            stat_list.append(args)
            return value_dict[args]
        value_dict[args] = func(*args)
        stat_list.append(args)
        stat_dict[args] = 1
        return value_dict[args]
    return new_func

import sys

sys.setrecursionlimit(50000)

@auto_dp

def p_count(n,m):
    if n == 1 or m == 1:
        return 1
    if n < m:
        return p_count(n,n)
    if n == m:
        return 1 + p_count(n,m-1)
    return p_count(n-m,m) + p_count(n,m-1)

print p_count(100,99)
