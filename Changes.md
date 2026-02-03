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
