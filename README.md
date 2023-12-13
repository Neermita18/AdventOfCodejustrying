Advent of Code Day 2 Part 1

A coding contest held in the month of December according to the Advent Calendar. Just giving them a try.

Need to sum all the days where the given constraint holds.
(ans) contains that. 

Used a dictionary for the constraint.
(mydict)
Set a variable to check if the constraint holds or not on a given day. (see)


Learnt file handling(properly) and new functions.

code!!
with open("input2.txt", 'r') as file:
    lines= file.readlines()
    ans=0
    for line in lines:
        #data= line.split('\n')
        see= True
        gameno, line= line.split(':')
        for event in line.split(';'):
            for balls in event.split(','):
                
                n,color = balls.split()
                mydict={'red':12, 'green':13, 'blue':14}
                if int(n) > mydict.get(color,0):
                    see=False
        if see:
            ans+= int((gameno).split()[-1])
            print(gameno)
print(ans) #add all gamenos        
