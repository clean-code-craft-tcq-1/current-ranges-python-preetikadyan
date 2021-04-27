

def identify_range_and_count(list_of_nos):
    #ar=[3,5,3,10,15]
    list_of_nos.sort()
    count=[]
    strt=[]
    end=[]
    i=0
    ct=-1
    pre= list_of_nos[0]-5 #to make sure that in the first itteration it doesn't satisfy the if condition and go to else
    
    while(i<len(list_of_nos)):
        if ((list_of_nos[i]-pre)<2):
            count[ct]+=1
            end[ct]=list_of_nos[i]
        else:
            count.append(1)
            strt.append(list_of_nos[i])
            end.append(list_of_nos[i])
            ct+=1

        pre=list_of_nos[i]
        i+=1
    
    print("Range, Readings")

    for i in range(ct+1):
        print(str(strt[i])+"-"+str(end[i])+", "+str(count[i]))
