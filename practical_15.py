def insertionSort(percent):
    for i in range(1, len(percent)):
        key = percent[i]
        j = i - 1
        while j>=0 and key < percent[j]:
            percent[j + 1] = percent[j]
            j-=1
        percent[j + 1] = key
    print(percent)

def shellSort(percent): 
    gap=len(percent)//2           
    while gap>0: 
        j=gap 
        while j<len(percent): 
            i=j-gap                
            while i>=0: 
                if percent[i+gap]>percent[i]: 
                    break
                else: 
                    temp = percent[i+gap]
                    percent[i + gap] = percent[i]
                    percent[i] = temp 
                i=i-gap  
            j+=1
        gap=gap//2
    print(percent)
    print("Top Five Scores:")
    for i in range(5):
        print(f"{i+1}. {percent[i]}")

arr = [23.4, 45.6, 11.09, 53.9, 9.3, 99.9, 1.0]
print("Using Insertion Sort:")
insertionSort(arr)
print("Using Shell Sort:")
shellSort(arr)