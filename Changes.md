Bug 1:

Was "if opt = "1":" changed to if opt == "1":

Trying to assign a value instead of comparing one 



Bug 2:
run_system_monolith

Was missing brackets so the function was never called and the program did nothing.

Changed to 

run_system_monolith()



Bug 3:

Infinte loop
loading = 0
    while loading < 5:
        print("Loading module " + str(loading))

"loading" never increases in the while loop so its going to run forever.


loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1





Bug 4:


Bug 4:

if opt == "1":  
            print("Current Crew List:")
            
            for i in range(10):
                print(n[i] + " - " + r[i]) 


        The loop was trying to acess indexes that dont exist. Initally n and r only have 4 items.


changed to 

    if opt == "1":  
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 

