


def solution(fees, records):
    answer= []
    import math
    record_dic ={}

    for record in records:
        car_num = record[6:10]
        time = record[:6]

        if car_num not in  record_dic:
            record_dic[car_num] = [time]
        else:
            record_dic[car_num].append(time)
    for i in record_dic:
        if len(record_dic[i]) %2 !=0:
            record_dic[i].append('23:59')
    record_dic= sorted(record_dic.items())
    for i in range(len(record_dic)):
        record_per_car = record_dic[i][1]

        time_sum= 0
        for j in range(0,len(record_per_car),2):
            
            aa = (int(record_per_car[j+1][:2]) - int(record_per_car[j][:2]))*60
            bb= int(record_per_car[j+1][3:]) - int(record_per_car[j][3:])
            time_sum += aa+bb
            
        
        if time_sum <=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+( math.ceil((time_sum-fees[0])/fees[2]) )*fees[-1])

    return answer



