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
           
        
            
    
