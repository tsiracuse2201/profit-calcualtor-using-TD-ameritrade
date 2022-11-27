with open('transactions.txt') as f:
    thing = {}
    count = 1
    for line in f:
        
        if line.rstrip():
            t = line.split()
            if count % 2==1:
                ticker = t[4]
                
                if t[4] not in thing: 
                    thing[t[4]] = []
            if count % 2 == 0:
                thing[ticker].append(t[0])
                
            count+=1
            
            
            
    print(thing)
    
    for key in thing:

        sumit= 0
        for x in thing[key]:
            print(float(x.replace(',','')))
            sumit += float(x.replace(',',''))
            
        print(key,sumit)  
        
