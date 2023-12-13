with open("input2.txt", 'r') as file:
    lines= file.readlines()
    ans=0
    for line in lines:
        #data= line.split('\n')
        see= True
        gameno, line= line.split(':')
        for event in line.split(';'):
            for balls in event.split(','):
                
                number,color = balls.split()
                mydict={'red':12, 'green':13, 'blue':14}
                if int(number) > mydict.get(color,0):
                    see=False
        if see:
            ans+= int((gameno).split()[-1])
            print(gameno)
print(ans) #add all gamenos          
           
        
            
    
