members_list = []
while True:
    name = input("Enter name: ")
    
    iD = (input("Enter ID number: "))
    try:
        id_no=int(iD)
    except ValueError:
        id_no=input(print("Enter a valid ID number: "))
    
    
    Plot_no = input("Enter plot number: ")
    try:
        plot_no=int(Plot_no)
    except ValueError:
        plot_no=input(print("Enter a valid plot number: "))
    
    
    members_list.append((name,id_no,plot_no))
    more = None
    while True:
        more = input("Add another? (Y?N): ").upper()
        if more in ("Y", "N"):
            break
        print("Invalid input")
    if more == "N":
        break
    print("\n")
print(f"Name | id_no | plot_no\n {members_list}")
