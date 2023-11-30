# WAP that scans an email address and forms a tuple of user name and domain
def parse_email(email):
    user_name, domain = email.split("@")
    return (user_name,domain)

email_address = input("Enter your gmail:")
parsed_tuple = parse_email(email_address)
print(parsed_tuple)     
