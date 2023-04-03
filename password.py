def main():
    with open('users.txt', 'r+') as f:
        userlist = (f.read()).split()

        validuser = False
        while validuser==False:

            username = input('username: ')
            if username not in userlist:
                if username == 'new':
                    #creating new user account,
                    print('Thank you for deciding to register.')
                    newusername = input('set username:')
                    newpassword = input('set password:')

                    print('\''+newusername+'\''+' is your new username')
                    print('\''+newpassword+'\''+' is your new password')
                    username = newusername
                    password = newpassword
                    print(newusername, file=f)
                    #print(newpassword, file=f)
                    t = open(str(username), 'w+')
                    print(newpassword, file=t)
                    f.close()
                    main()

                print('\'' + username + '\', is not a registered user.\n' + \
                'Type \'new\' to create an account.')
            else:
                validuser=True

                with open(str(username), 'r') as v:
                    info = (v.read())
                    infolist = info.split()
                    passwordattempt = input('password: ')
                    if passwordattempt == infolist[0]:
                        print('Welcome, YOU GOT IN')



























main()



#users.txt, contains just usernames of users that exist. If the username does not exist, a new file will be created,
##and the new username will be added to users.txt
#(username).txt contains the information of said user.