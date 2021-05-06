

def identify_range_and_count(list_of_nos):
    #ar=[3,5,3,10,15]
    list_of_nos.sort() #sort the element to ascending order
    count=[]
    strt=[]
    end=[]
    result = []
    i=0
    ct=-1
    pre= list_of_nos[0]-5 
    length = len(list_of_nos)
    #in this logic I am comparing the current element with the previous element
    #First element doesn't have a previous value so i.e., why the initial previous contains a negative index
    
    while(i< length):
        if ((list_of_nos[i]-pre)<2): #whenever there is a range the difference of current and previous value is either '0'(when they are equal) or '1'
            count[ct]+=1
            end[ct]=list_of_nos[i]
        else:
            count.append(1)
            strt.append(list_of_nos[i])
            end.append(list_of_nos[i])
            ct+=1

        pre=list_of_nos[i] #with every itteration current value becomes previous
        i+=1
    
    print("Range, Readings")

    for i in range(ct+1):
        #print(str(strt[i])+"-"+str(end[i])+", "+str(count[i]))
        result.append(str(strt[i])+"-"+str(end[i])+" "+str(count[i]))
        
    return result
