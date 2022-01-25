def replace_domain (email,new_domain,old_domain = 'sheba.xyz') :
    if old_domain == "sheba.xyz":
        print('Unchanged:',email)
    else :
        new_email = ""
        first_part = email.index('@') + 1
        for i in range(first_part):
            new_email += email[i]
        new_email +=new_domain
        print("Changed:", new_email)

email = input()
new_domain = input()
old_domain = input()
if old_domain == "" :
    replace_domain(email,new_domain)
else :
    replace_domain(email,new_domain,old_domain)