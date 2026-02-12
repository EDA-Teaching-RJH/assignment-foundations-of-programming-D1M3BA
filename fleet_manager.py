import time


def main():
    print("=" * 50)
    print("BOOTING SYSTEM...")
    print("=" * 50)
    time.sleep(0.5)
    
    print("\n[SYSTEM] Initializing database...")
    names, ranks, divisions, ids = init_database()
    time.sleep(0.3)
    print("[SYSTEM] Database loaded successfully")
    time.sleep(0.5)

    print("\n" + "-" * 50)
    full_name = input("Enter your full name: ").strip().title()
    print(f"[AUTH] Logging in: {full_name}...")
    time.sleep(0.5)
    print(f"[AUTH] Welcome, {full_name}")
    time.sleep(0.3)
    print("-" * 50)
    
    print("\n" + "=" * 50)
    print("     WELCOME TO FLEET COMMAND")
    print("=" * 50)

    while True:
        opt = display_menu(full_name)
        
        if opt == "1":
            print("\n[SYSTEM] Loading crew roster...")
            time.sleep(0.3)
            display_roster(names, ranks, divisions, ids)
            
        elif opt == "2":
            print("\n[SYSTEM] Add crew member module activated")
            time.sleep(0.3)
            add_member(names, ranks, divisions, ids)
            
        elif opt == "3":
            print("\n[SYSTEM] Remove crew member module activated")
            time.sleep(0.3)
            remove_member(names, ranks, divisions, ids)
            
        elif opt == "4":
            print("\n[SYSTEM] Rank update module activated")
            time.sleep(0.3)
            update_rank(names, ranks, divisions, ids)
            
        elif opt == "5":
            print("\n[SYSTEM] Searching crew database...")
            time.sleep(0.3)
            search_crew(names, ranks, divisions, ids)
            
        elif opt == "6":
            print("\n[SYSTEM] Filtering by division...")
            time.sleep(0.3)
            filter_by_division(names, ranks, divisions, ids)

        elif opt == "7":
            print("\n[SYSTEM] Calculating payroll...")
            time.sleep(0.3)
            total = calculate_payroll(ranks)
            print(f"[FINANCE] Total monthly payroll: {total} Credits")
            
        elif opt == "8":
            print("\n[SYSTEM] Analyzing officer count...")
            time.sleep(0.3)
            officer_count = count_officers(ranks)
            print(f"[ANALYSIS] Total high-ranking officers: {officer_count}")
        
        elif opt == "9":
            print("\n" + "=" * 50)
            print(f"[AUTH] Logging out user: {full_name}")
            time.sleep(0.5)
            print("[SYSTEM] Shutting down...")
            time.sleep(0.5)
            print("=" * 50)
            break
            
        else:
            print("\n[ERROR] Invalid option. Enter the number next to the associated action")

            
    
        




def init_database():
    names = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant Commander", "Commander"]
    divisions = ["Science", "Operations", "Other", "Science", "Operations"]
    ids = ["1001", "1002", "1003", "1004", "1005"]

    return names, ranks, divisions, ids


def display_menu(full_name):
    print("\n" + "-" * 50)
    print(f"  Logged in as: {full_name}")
    print("-" * 50)
    print("--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Update rank")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")
    print("9. Exit")
    print("-" * 50)
    opt = input("Select option: ").strip()
    
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
        if found != -1:
            break

    while True:
        new_id = input("ID: ").strip()
        found = False

        for i in range(len(ids)):
            if new_id == ids[i]:
                found = True 
        
        if found == True:
            print("[ERROR] This ID is already in use. Please use another")
        else:
            break

    names.append(new_name)
    ranks.append(new_rank)
    divisions.append(new_div)
    ids.append(new_id)

    print(f"\n[SUCCESS] Crew member added:")
    time.sleep(0.3)
    print(f"  ID: {ids[-1]} | Name: {names[-1]} | Rank: {ranks[-1]} | Division: {divisions[-1]}")




def print_list(list):
    x = ""
    for i in range(len(list)):
        if i == 0:
            x += list[i]
        else:
            x += " | " + list[i]
    print(f"{x}")



    
            
           
def display_roster(names, ranks, divisions, ids):
    print("\n" + "=" * 90)
    print("ID                    |Name                   |Rank                   |Division             ")
    print("=" * 90)

    for i in range(len(names)):
        name = column_align(names[i])
        rank = column_align(ranks[i])
        division = divisions[i]
        id = column_align(ids[i])

        print(f"{id}| {name}| {rank}| {division}")
    
    print("=" * 90)





def remove_member(names, ranks, divisions, ids):
    print("What crew member would you like to remove?")
    idx = get_id(names, ranks, divisions, ids)
   
    print(f"\n[CONFIRM] Removing: {ids[idx]} | {names[idx]} | {ranks[idx]} | {divisions[idx]}")
    time.sleep(0.3)
        
    ids.pop(idx)
    names.pop(idx)
    divisions.pop(idx)
    ranks.pop(idx)
    
    print("[SUCCESS] Crew member has been removed")
    


def update_rank(names, ranks, divisions, ids): 
    print("Whose rank do you wish to change?")
    idx = get_id(names, ranks, divisions, ids)

    print(f"\n[INFO] {names[idx]} is currently a {ranks[idx]}")

    while True: 
        new_rank = input(f"Enter {names[idx]}'s new rank: ").strip().title()
        
        if valid_rank(new_rank) == True:
            ranks[idx] = new_rank
            print(f"\n[SUCCESS] Rank updated")
            time.sleep(0.3)
            print(f"[INFO] {names[idx]} is now a {ranks[idx]}")
            break
        
    
   




        
    



def column_align(word):
    column_length = 22
    spaces = column_length - len(word)
    if spaces < 0:
        return word
    for i in range(spaces):
        word += " "
    return word






def valid_rank(rank):
    valid_ranks = ["Crewman", "Ensign", "Jr Lieutenant", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Rear Admiral", "Vice Admiral", "Admiral"]
    for i in range(len(valid_ranks)):
        if rank == valid_ranks[i]:
            return True
            
    print("[ERROR] Invalid TNG Rank. Please try one below:")
    print_list(valid_ranks)
    return False

    
        


def valid_division(division):
    valid_divs = ["Command", "Operations", "Science", "Civilian", "Other"]
    for i in range(len(valid_divs)):
        if division == valid_divs[i]:
            return i
    
    print("[ERROR] Invalid TNG Division. Please try one below:")
    print_list(valid_divs)
    return -1




def get_id(names, ranks, divisions, ids):
    while True:
        id_to_find = input("Enter ID: ").strip()
        found = False
        for i in range(len(ids)):
            if ids[i] == id_to_find:
                return i
        print(f"[ERROR] ID '{id_to_find}' not found.")

        choice = input("Type 'list' to view roster or press Enter to try again: ").strip().lower()
        if choice == 'list':
            display_roster(names, ranks, divisions, ids)
    

def search_crew(names, ranks, divisions, ids):
    search_term = input("Enter a search term: ").strip().lower()
    found = False
    
    print(f"\n[SEARCH] Searching for '{search_term}'...")
    time.sleep(0.3)
    
    for i in range(len(names)):
        if search_term in names[i].lower():
            print(f"[FOUND] {ids[i]} | {names[i]} | {ranks[i]} | {divisions[i]}")
            found = True
    
    if found == False:
        print(f"[SEARCH] No matching crew members for '{search_term}'")


def filter_by_division(names, ranks, divisions, ids):
    while True:
        check_div = input("What division would you like to check? ").strip().title()
        idx = valid_division(check_div)
        if idx != -1:
            print_by_division(idx, names, ranks, divisions, ids)
            break
        
        
            

                

def print_by_division(div, names, ranks, divisions, ids):
    valid_divs = ["Command", "Operations", "Science", "Civilian", "Other"]
    print("\n" + "=" * 50)
    print(f"  Members of {valid_divs[div]} Division")
    print("=" * 50)
    
    found = False
    for i in range(len(divisions)):
        if valid_divs[div] in divisions[i]:
            print(f"{ids[i]} | {names[i]} | {ranks[i]}")
            found = True
            
    if found == False:
        print("[INFO] No members found")
    
    print("=" * 50)



def calculate_payroll(ranks):
    total_budget = 0
    for i in range(len(ranks)):
        rank = ranks[i]
        if rank == "Admiral":
            total_budget += 10000
        elif rank == "Vice Admiral":
            total_budget += 5000
        elif rank == "Rear Admiral":
            total_budget += 2000
        elif rank == "Captain":
            total_budget += 1000
        elif rank == "Commander":
            total_budget += 800
        elif rank == "Lieutenant Commander":
            total_budget += 700
        elif rank == "Lieutenant":
            total_budget += 600
        elif rank == "Ensign":
            total_budget += 500
        elif rank == "Civilian":
            continue
        else:
            total_budget += 200
    
    return total_budget


def count_officers(ranks):
    count = 0
    for i in range(len(ranks)):
        if ranks[i] == "Captain" or ranks[i] == "Commander" or ranks[i] == "Rear Admiral" or ranks[i] == "Vice Admiral" or ranks[i] == "Admiral":
            count += 1

    return count


   
        





main()