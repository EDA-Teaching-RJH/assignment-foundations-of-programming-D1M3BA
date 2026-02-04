

def main():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")

    init_database()
    




def init_database():
    names = ["Spock" , "Data" , "Garak" , "EMH" , "Tuvok"]
    ranks = ["First Officer" , "Operations Officer", "Medical Officer" , "Recurrent" , "Security"]
    divisions = ["Science" , "Operations" , "Other" , "Science" , "Operations" ]
    id = ["1001" , "1002" , "1003" , "1004" , "1005"]

    return names, ranks, divisions, id





main()



