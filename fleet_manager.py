
import time


def main():
    print("BOOTING SYSTEM...")
    print("...")
    

    names, ranks, divisions, ids = init_database()
    opt = int(display_menu())
    if opt == 1:
        display_roster(names, ranks, divisions, ids)
    elif opt == 2:
        add_member(names, ranks, divisions, ids)
    elif opt == 3:
        remove_member(names, ranks, divisions, ids)
    
        




def init_database():
    names = ["Picard" , "Riker" , "Data" , "Forge" , "Crusher"]
    ranks = ["Captain" , "Commander", "Lieutenant Commander" , "Lieutenant Commander" , "Commander"]
    divisions = ["Science" , "Operations" , "Other" , "Science" , "Operations" ]
    ids = ["1001" , "1002" , "1003" , "1004" , "1005"]

    return names, ranks, divisions, ids


def display_menu():

    full_name = input("Enter your full name: ").strip().title()

    

    print(f"Logging in: {full_name} ")
    print("...")
    print(f"Student: {full_name} is now logged in")
    print("WELCOME TO FLEET COMMAND")
    print("\n--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("5. Exit")
    opt = input("Select option: ")
    
    return opt



def add_member(names, ranks, divisions, ids):
    valid_ranks = ["Crewman", "Ensign" , "Jr Lieutenant", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Rear Admiral", "Vice Admiral", "Admiral"]
            
    new_name = input("Name: ").strip().title()

    while True:
        new_rank = input("Rank: ").strip().title()

        found = False
        for i in range(len(valid_ranks)):
            if new_rank == valid_ranks[i]:
                found = True
        
        if found == True: 
            break
        else:
            print("Rank cannot be found. Please use a valid TNG rank listed below")
            print_list(valid_ranks)
        
    new_div = input("Division: ").strip().title()

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



# prints list on a single line with no extra formatting 
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
    
    id_to_find = input("Enter the ID of the member you want to remove: ")

    found = False 
    idx = -1
    for i in range(len(ids)):
        if id_to_find == ids[i]:
            found = True
            idx = i
    if found == True:
        
        print(f"Removing {ids[idx]} | {names[idx]} | {ranks[idx]} | {divisions[idx]}")
        
        ids.pop(idx)
        names.pop(idx)
        divisions.pop(idx)
        ranks.pop(idx)
        print("Crew Member has been removed")
    else:
        print(f"Id not found")
        
    



def column_align(word):
    column_length = 22
    spaces = column_length - len(word)
    if spaces < 0:
        return word
    for i in range(spaces):
        word += " "
    return word

main()



