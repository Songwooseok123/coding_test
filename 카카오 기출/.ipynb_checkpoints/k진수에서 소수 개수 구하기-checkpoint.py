def n_to_k(n,k):
    k_n =''
    while True:
        k_n +=str(n%k)
        mok = n//k
        n = mok
        if n == 0:
            break
    
    return k_n[::-1]
    
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution(n, k):
    zz = n_to_k(n, k).split('0')
    cc =0
    for z in zz:
        if z =='':
            continue
        if is_prime(int(z)):
            cc +=1
    
    return cc