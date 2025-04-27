from itertools import product

def solution(users, emoticons):
    sales = [10,20,30,40]
    sale_permutation = list(product(sales, repeat=len(emoticons)))
 
    zzzz = []
    for sale_ in sale_permutation:
        total_per_sale = []
        register = 0
        for zz,user in enumerate(users):
            user_threshold =user[0]
            sum_user = 0
            for s,e in zip(sale_,emoticons):
                if s>= user_threshold:
                    sum_user +=e*(100-s)/100
            if sum_user>= user[1]:
                sum_user =0
                register +=1
            total_per_sale.append(sum_user)

        ttotal_per_sale = int(sum(total_per_sale))

        zzzz.append((register,ttotal_per_sale))
    zzzz.sort(reverse =True)
    answer = list(zzzz[0])
    return answer






