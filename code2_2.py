from collections import defaultdict
with open("input2.txt", 'r') as file:
    lines= file.readlines()
    ans=0
    for line in lines:
        #data= line.split('\n')
        finalval=1
        gameno, line= line.split(':')
        numbers=defaultdict(int)
        for event in line.split(';'):
            
            for balls in event.split(','):
                
                number,color = balls.split()
                numbers[color]=max(int(numbers[color]),int(number)) #create dictionary with colors as the key. It'll hold the value of maximum number of a colored #ball across all events in a game
                  
        #print(numbers)
        for i in numbers:
            v=numbers[i]
            finalval=finalval*v
        ans= ans+finalval    
            
    print(ans) 
