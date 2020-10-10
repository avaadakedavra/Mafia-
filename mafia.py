import os
import smtplib
import random
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')



print("Welcome, members of the 7/54 Meeks St Clan!")
print("Let's play Mafia!")
input("Press ENTER you're ready!\n")

#print("RULES:")
#print("Once the moderator is assigned, he/she must be the only person interacting with the screen.")
# people = {"Sreejith":"sreejithmohan936@gmail.com","Prakriti":"pshahdeo5@gmail.com","Nakul":"nakul9597@gmail.com","Juhi":"juuhhiii17@gmail.com","Savitha":"Savithasrinivas2010@gmail.com","Kaushik":"kaushikmechian@gmail.com","Tarun":"tarun.jacob.au@gmail.com","Joel":"joeljbraganza@gmail.com","Havish":"havishkrish@hotmail.com","Shreya":"shreya.12@hotmail.com"}

people = {"Suharsh":"suharsh829@gmail.com","Savitha":"Savithasrinivas2010@gmail.com","Shreya":"shreya.12@hotmail.com","Nehal":"yathamnehal1@gmail.com","Joel":"joeljbraganza@gmail.com"}
#print(len(people))

mod = random.choice(list(people))

people.pop(mod)

print("Your moderator is", mod.upper())

input("Press ENTER when you're ready! \n")

print("Hey",mod)
print("From now on it's just you and me ;)")
#print("Once you have the roles of each person in the game, you will have the send them a message of their role\n")

mafia = random.choice(list(people))
print("Mafia:",mafia.upper())

Mafiamsg = EmailMessage()
Mafiamsg['Subject'] = 'Welcome to Mafia'
Mafiamsg['From'] = EMAIL_ADDRESS
Mafiamsg['To'] = people[mafia]
Mafiamsg.set_content('You are the Mafia! Enjoy!')

people.pop(mafia)








doctor = random.choice(list(people))
print("Doctor:",doctor.upper())


Docmsg = EmailMessage()
Docmsg['Subject'] = 'Welcome to Mafia'
Docmsg['From'] = EMAIL_ADDRESS
Docmsg['To'] = people[doctor]
Docmsg.set_content('You are the Doctor ! Have fun !')

people.pop((doctor))




    




with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(Mafiamsg)
    smtp.send_message(Docmsg)

    for i in range(0,2):
        cit = random.choice(list(people))
        print("Citizen:",cit.upper())
        Citmsg = EmailMessage()
        Citmsg['Subject'] = 'Welcome to Mafia'
        Citmsg['From'] = EMAIL_ADDRESS
        Citmsg.set_content('You are a Citizen ! Good Luck !')
        Citmsg['To'] = people[cit]
        people.pop(cit)
        smtp.send_message(Citmsg)

    
