

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



Bug 5:

 elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")


it dosent append new_rank and new_div to their respective lists so any new_name added dosent have an associated rank and div. It also messes up the current implimentation for View Crew

changed to 



 elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")


Bug 6:


rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")




It dosent check if the index is valid before assigning that value to a variable which causes the program to crash.

    rem = input("Name to remove: ")
    found = False 
    idx = 0

    for i in range(len(n)):
        if n[i] == rem: 
            found = True 
            idx = i 


    if found == True:
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        print("Removed.")
    else: 
        print("Error: That person is not in the crew.")



Bug 7:

print("High ranking officers: " + count)

Trying to concatenate str and int. need to use printf

print(f"High ranking officers: " + {count})



Bug 8:

if rank == "Captain" or "Commander":


it wasnt comparing commander against anything so the  statement is always true 

if rank == "Captain" or rank == "Commander":



Bug 9:

x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            

x is hardcoded to be 10 so these lines of code are redudant.Unsure of the inteded implementation so i will just remove it for now. 




