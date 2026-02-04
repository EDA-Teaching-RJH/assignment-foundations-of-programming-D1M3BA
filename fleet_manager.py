

def main():
    print("BOOTING SYSTEM...")
    print("...")
    

    init_database()
    display_menu()




def init_database():
    names = ["Spock" , "Data" , "Garak" , "EMH" , "Tuvok"]
    ranks = ["First Officer" , "Operations Officer", "Medical Officer" , "Recurrent" , "Security"]
    divisions = ["Science" , "Operations" , "Other" , "Science" , "Operations" ]
    id = ["1001" , "1002" , "1003" , "1004" , "1005"]

    return names, ranks, divisions, id


def display_menu():

    full_name = input("Enter your full name: ").strip().title()

    print("\n--- MENU ---")

    print(f"Logging in: {full_name} ")
    print(f"Student: {full_name} is now logged in")
    print("WELCOME TO FLEET COMMAND")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("5. Exit")
    opt = input("Select option: ")
    
    return opt








main()



