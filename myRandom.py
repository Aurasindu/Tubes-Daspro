import time

epochtime = int(time.time() * 10)
pi = "3141592653589793238462643383279502884197"
memo = [1]

first_num = 1
current_n = 0

def myLen(arr) :
    return arr[0]

def myAppend(arr, el,) :
    res = [0 for i in range(arr[0] + 1)]
    res[0] = arr[0] + 1
    for i in range(1, arr[0]) :
        res[i] = arr[i]
    res[arr[0]] = el
    return res

for i in range(len(str(epochtime))) :
    first_num *= (int(str(epochtime)[i]) + 3)
    first_num %= 10*int(pi[i]) + int(pi[i+1])


memo = myAppend(memo, first_num)

for i in range(30) :
    next_num = (epochtime^(100*(int(pi[i])) + 10*(int(pi[i+1])) + int(pi[i+2]))) % 168147839
    memo = myAppend(memo, next_num)

def star(n1, n2) :
    return (n1 + n1^n2 + n2) ^ (n1 * n2)

def gen_rnd(n, j = 6, k = 31) :
    global memo
    if n < myLen(memo) :
        return memo[n]
    else :
        next_val = (star(gen_rnd(n-j), gen_rnd(n-k))) % 9111
        memo = myAppend(memo, next_val)
        return next_val
    
def randint_1_5() :
    global current_n
    global memo

    current_n += 1
    return (gen_rnd(current_n) + 1) % 5 + 1

if __name__ == "__main__" :
    counter = [0,0,0,0,0]
    for i in range(1, 10001) :
        counter[randint_1_5() - 1] += 1
    print(counter)
