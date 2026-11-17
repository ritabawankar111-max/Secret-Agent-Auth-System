from datetime import datetime

for i in range(3):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    username = input("TYPE USERNAME:")
    secret_code = input("TYPE CODE:")    
    
    if secret_code == "ironman@$123":
        print("ACCESS GRANTED")
        print("WELCOME", username)
        with open("/storage/emulated/0/Download/secret_trap_log.txt", "a") as file:
            file.write(f"[{current_time}] login successfully by username: {username}\n")
        break

    elif secret_code == "admin@view":
        print("\n--- HEAD OFFICE SECRET LOGS ---")
        with open("/storage/emulated/0/Download/secret_trap_log.txt", "r") as file:
            print(file.read())
        break
      
    else:
        print("ACCESS_DENIED #_#")
       
else:
    with open("/storage/emulated/0/Download/secret_trap_log.txt", "a") as file:
        file.write(f"[{current_time}] ALERT! Intruder caught -> Username used: {username}\n")


