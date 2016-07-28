n = int(input())                   

arrayIn = list(input().split(" ")) 
arrayIn = map(int, arrayIn)        
arrayOut = [0]*100                 

for element in arrayIn:            
    arrayOut[element]+=1           

print(*arrayOut, sep=" ") 
