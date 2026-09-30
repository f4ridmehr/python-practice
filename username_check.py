users = ['ali', 'sara', 'reza']
new_user = 'Sara'

if new_user.lower() in users:
    print(f"{new_user} is already taken.")
else:
    print(f"{new_user} is available.")
