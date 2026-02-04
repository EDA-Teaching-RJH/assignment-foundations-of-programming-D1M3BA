
import time


def main():
    print("BOOTING SYSTEM...")
    time.sleep(0.5)
    
    
    names, ranks, divisions, ids = init_database()
    print("Initilising databse")
    time.sleep(0.5)
    print("Sucessful")
    time.sleep(0.5)

    full_name = input("Enter your full name: ").strip().title()
    print(f"Logging in: {full_name} ")
    time.sleep(0.5)
    
    print(f"Student: {full_name} is now logged in")
    time.sleep(0.5)
    print("WELCOME TO FLEET COMMAND")

    while True:
        opt = int(display_menu())
        if opt == 1:
            display_roster(names, ranks, divisions, ids)
        elif opt == 2:
            add_member(names, ranks, divisions, ids)
        elif opt == 3:
            remove_member(names, ranks, divisions, ids)
        elif opt == 4:
            update_rank(names,ranks, divisions, ids)
       ## elif opt == 5:
            

       ## elif opt == 6:

       ## elif opt == 7:

       ## elif opt == 8:
        

        elif opt == 9:
            print(f"Logging out User: {full_name}")
            time.sleep(0.5)
            print("Shutting down")

            
    
        




def init_database():
    names = ["Picard" , "Riker" , "Data" , "Forge" , "Crusher"]
    ranks = ["Captain" , "Commander", "Lieutenant Commander" , "Lieutenant Commander" , "Commander"]
    divisions = ["Science" , "Operations" , "Other" , "Science" , "Operations" ]
    ids = ["1001" , "1002" , "1003" , "1004" , "1005"]

    return names, ranks, divisions, ids


def display_menu():

    

    

   
    
    print("\n--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Update rank")
    print("5. Find crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")

    print("9. Exit")
    opt = input("Select option: ")
    
    return opt



def add_member(names, ranks, divisions, ids):
    
            
    new_name = input("Name: ").strip().title()

    while True:
        new_rank = input("Rank: ").strip().title()

        found = valid_rank(new_rank)
        if found == True: 
            break
    while True:
        new_div = input("Division: ").strip().title()
        found = valid_division(new_div)
        if found == True:
            break

    while True:
        new_id = input("ID: ").strip()
        found = False

        for i in range(len(ids)):
            if new_id == ids[i]:
                found = True 
        
        if found == True:
            print("This id is already in use. Please Use another")
        else:
            break




    names.append(new_name)
    ranks.append(new_rank)
    divisions.append(new_div)
    ids.append(new_id)

    print(f"Crew member:  {ids[-1]} | {names[-1]} | {ranks[-1]} | {divisions[-1]}  has been succesfully added")




def print_list(list):

 
    x  =  ""
    for i in range(len(list)):
        if i == 0:
            x += list[i]
        else:
            x += " | " + list[i]
    print(f"{x}")



    
            
           
def display_roster (names, ranks, divisions, ids):


    print("ID                    |Name                   |Rank                   |Division             ")
    print("--------------------------------------------------------------------------------------------")

    for i in range(len(names)):
        name = column_align(names[i])
        rank = column_align(ranks[i])
        division = divisions[i]
        id = column_align(ids[i])

        print(f"{id}| {name}| {rank}| {division}")





def remove_member(names, ranks, divisions, ids):
    
   

    print("What crew member would you like to remove")
    idx = get_id(names, ranks, divisions, ids)
   
        
    print(f"Removing {ids[idx]} | {names[idx]} | {ranks[idx]} | {divisions[idx]}")
        
    ids.pop(idx)
    names.pop(idx)
    divisions.pop(idx)
    ranks.pop(idx)
    print("Crew Member has been removed")
    


def update_rank(names, ranks, divisions,ids): 
    
    print("Whos rank do you wish to change")
    idx = get_id(names, ranks, divisions, ids)

    print(f"{names[idx]} is currently a {ranks[idx]}")

    while True: 
        new_rank = input(f"Enter {names[idx]} new rank:  ")

        
        
        if valid_rank(new_rank) == True:
            ranks[idx] = new_rank
            print(f"Succesful.")
            print(f"{names[idx]} is now a {ranks[idx]} ")
            break
        
    
   




        
    



def column_align(word):
    column_length = 22
    spaces = column_length - len(word)
    if spaces < 0:
        return word
    for i in range(spaces):
        word += " "
    return word

main()




def valid_rank(rank):
    valid_ranks = ["Crewman", "Ensign" , "Jr Lieutenant", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Rear Admiral", "Vice Admiral", "Admiral"]
    for i in range(len(valid_ranks)):
            if rank == valid_ranks[i]:
                return True
            
    print("Invalid TNG Rank. Please try one below")
    print_list(valid_ranks)
    return False

    
        


def valid_division(division):
    valid_divs = ["Command", "Operations", "Sciences", "Civilian", "Other"]
    for i in range(len(valid_divs)):
        if division == valid_divs[i]:
            return True
    
    print("Invalid TNG Division. Please try one below")
    print_list(valid_divs)
    return False




def get_id(names, ranks, divisions, ids):
    while True:
        id_to_find = input("Enter Id: ").strip()
        found = False
        for i in range(len(ids)):
            if ids[i] == id_to_find:
                return i
        print(f"Error: ID '{id_to_find}' not found.")


        choice = input("Type list to view roster or Enter to try again")
        if choice == 'list':
            display_roster(names, ranks, divisions, ids)
    