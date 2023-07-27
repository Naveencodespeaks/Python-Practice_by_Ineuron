# collect email from the user
# split the email using the @, the first part as the username, the second part is gonna be  saved as domain
# EX:-sainaveen@gmail.com
# split domain using .,



def main():
    print("Welcome to the email slicer")
    print(" ")

    email_input = input("Input your email adress: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username : ", username)
    print("domain : ", domain)
    print("extension : ", extension)

while True:
    main()