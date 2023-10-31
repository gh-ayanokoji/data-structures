def sel_sort(percent):
    for i in range(len(percent)):
        min = i
        
        for j in range(i+1, len(percent)):
            if percent[j] < percent[min]:
                min = j

        temp = percent[min]
        percent[min] = percent[i]
        percent[i] = temp

    print(percent)

def bub_sort(percent):
    for i in range(len(percent)):
        swap = 0
        for j in range(len(percent)-i-1):
            if percent[j]>percent[j+1]:
                temp = percent[j]
                percent[j] = percent[j+1]
                percent[j+1] = temp
                swap = 1
        if swap == 0:
            break
    print(percent)

    
arr = [23.4,45.6,11.09,53.9]
bub_sort(arr)