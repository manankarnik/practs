class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

users = [User("alice", "admin"), User("bob", "user")]

confidential_data = "SECRET"
public_data = "PUBLIC"

while True:
    print("\n1. Login")
    print("2. Quit")
    action = int(input("\nEnter action: "))
    if action == 2: exit()
    if action != 1: 
        print("Invalid action")
        continue
    username = input("\nEnter username: ")
    if len([u for u in users if u.name == username]) == 1:
        logged_in = True
        current_user = [u for u in users if u.name == username][0]
        print(f"Logged in as {current_user.name} with role {current_user.role}")
        while logged_in:
            print("\n1. View data")
            print("2. Update data")
            print("3. Logout")
            print("4. Quit")
            action = int(input("\nEnter action: "))
            match action:
                case 1:
                    print()
                    if current_user.role == "admin": print("Confidential:", confidential_data)
                    print("Public:", public_data)
                case 2:
                    if current_user.role == "admin": confidential_data = input("Enter confidential data: ")
                    public_data = input("Enter public data: ")
                    print("Data updated")
                case 3:
                    logged_in = False
                case 4:
                    exit()
    else:
        print("User does not exist")

