#Advent of Code Day 2 Part 1 and 2


A coding contest held in the month of December according to the Advent Calendar. Just giving them a try. Used Python.

Part 1

Need to sum all the days where the given constraint holds.
(ans) contains that. 

Used a dictionary for the constraint.
(mydict)
Set a variable to check if the constraint holds or not on a given day. (see)


Learnt file handling(properly) and new functions.

code1!!


```
with open("input2.txt", 'r') as file:
    lines= file.readlines()
    ans=0
    for line in lines:
        #data= line.split('\n')
        see= True
        gameno, line= line.split(':') #first element is the gameno, remaining we use later
        for event in line.split(';'): #events differentiated by ;
            for balls in event.split(','): #each event has number of balls and color
                
                number,color = balls.split() #store those values
                mydict={'red':12, 'green':13, 'blue':14} #the constraint
                if int(number) > mydict.get(color,0):  #checking if the number of balls of a color in given event is more than constraint
                    see=False #can't add if it is
        if see:
            ans+= int((gameno).split()[-1]) #gameno contains 'Game : number.' accessing the number
            print(gameno)
print(ans) #add all gamenos
```

code2!!
```
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

```
