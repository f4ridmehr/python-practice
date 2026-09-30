email = 'Ali@Gmail.COM'
clean_email = email.lower()
print(clean_email)
if '@gmail.com' in clean_email:
    print('This is a Gmail address.')
else:
    print('This is not a Gmail address.')
