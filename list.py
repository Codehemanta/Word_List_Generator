#!/usr/bin/env python3
import os,sys,time;


title = """
	
[+] Autor: hemanta gayen 
[+] Date: 18th jun 2020

"""
drigen = """
           ______________
      ,===:'.,            `-._
           `:.`---.__         `-._
             `:.     `--.         `.
               \.        `.         `.
       (,,(,    \.         `.   ____,-`.,
    (,'     `/   \.   ,--.___`.'
,  ,'  ,--.  `,   \.;'         `
 `{D, {    \  :    \;
   V,,'    /  /    //
   j;;    /  ,' ,-//.    ,---.      ,
   \;'   /  ,' /  _  \  /  _  \   ,'/
   /\     \   `'  / \  `'  / \  `.' /
  //\\\    `.___,'   `.__,'   `.__,' """



Auhtor ="""
 ///\\\\\\ Author by :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
//// \\\\\    \\\\\  \\\\\\\\\\\  \\\\\\        \\\\\         ///\\\  \\\\\\       \\\ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\    ///\\\\\   
\\\\\\\\\ \\\\\    \\\\\  \\\\      \\\\\ \\\\  \\\\ \\\\\       ///  \\\  \\\\\ \\\\    \\\       \\\         ///  \\\\\ 
 \\\\\\\\\ \\\\\\\\\\\\\\\\\\\  \\\\\\\    \\\\\\\  \\\   \\\\\     /////\\\\\\\  \\\\\   \\\\  \\\       \\\       /////\\\\\\\\\   
  \\\\\\\\\ \\\\\    \\\\\  \\\\      \\\\\        \\\\\   ///      \\\  \\\\\    \\\\ \\\       \\\     ///      \\\\\ 
   \\\\\\\\\ \\\\\    \\\\\  \\\\\\\\\\\  \\\\\        \\\\\ ///        \\\  \\\\\      \\\\\\       \\\   ///        \\\\\  
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""

print(drigen +  title)


def interactive():
  name = input("First Name: ").lower().strip()
  while not name:
    print("\n[-] You must enter a name at least!", file=sys.stderr)
    name = input("First Name: ").lower().strip()

  surname = input("Surname: ").lower()
  nick = input("Nickname: ").lower()

  birthdate = input("Birthdate (DDMMYYYY): ").strip()
  while len(birthdate) not in (0, 8):
    print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
    birthdate = input("Birthdate (DDMMYYYY): ").strip()
  
  #phone number
  phone = input("Phone Number: ").strip()
  while len(phone) not in (0, 10):
    print("\n[-] You must enter 12 digits for phone number!", file=sys.stderr)
    phone = input("Phone Number: ").strip()
  
  #Email
  email =input("Email Address(Example123@gmail.com): ").strip()

  print("\n")

  
  wife = input("Partner's name: ").lower()
  wifen = input("Partner's nickname: ").lower()
  wifeb = input("Partner's birthdate (DDMMYYYY): ").strip()
  while len(wifeb) not in (0, 8):
    print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
    wifeb = input("Partner's birthdate (DDMMYYYY): ").strip()

  print("\n")

  kid = input("Child's name: ").lower()
  kidn = input("Child's nickname: ").lower()
  kidb = input("Child's birthdate (DDMMYYYY): ").strip()
  while len(kidb) not in (0, 8):
    print("\n[-] You must enter 8 digits for birthday!", file=sys.stderr)
    kidb = input("Child's birthdate (DDMMYYYY): ").strip()

  print("\n")

  pet = input("Pet's name: ").lower().strip()
  company = input("Company name: ").lower().strip()

  print("\n")

  # Convert first letters to uppercase...
  nameup = name.title()
  surnameup = surname.title()
  nickup = nick.title()
  wifeup = wife.title()
  wifenup = wifen.title()
  kidup = kid.title()
  kidnup = kidn.title()
  petup = pet.title()
  companyup = company.title()
  
  # Year
  y1 = '2015'
  y2 = '2016'
  y3 = '2017'
  y4 = '2018'
  y5 = '2019'
  y6 = '2020'
  # Name + year
  y15 = name +'2015'
  y16 = name +'2016'
  y17 = name + '2017'
  y18 = name + '2018'
  y19 = name +'2019'
  y20 = name + '2020'

  #totalname
  ns = name + surname
  sn = surname + name
  

  # Number
  n2 = '12'
  n3 = '123'
  # Symbole
  saname = name + '@'
  shname  = name + '#'

  #phone var
  p1 = phone[0:2]
  p2 = phone[0:3]
  p3 = phone[0:4]
  p4 = phone[-2:]
  p5 = phone[-3:]
  p6 = phone[-4:]



  ##############################################################
  listing = (
    # Name+year
    name + n2, name + n3,
    y15, y16, y17, y18, y19, y20,
    y15 + n2, y16 + n2, y17 + n2, y18 + n2, y19 + n2, y20 + n2,
    y15 + n3, y16 + n3, y17 + n3, y18 + n3, y19 + n3, y20 + n3,
    

    # Name+surname+birth
    name + birthdate, name + birthdate[4:8], name + birthdate[0:2],
    ns + birthdate[4:8], ns + '@'+ birthdate[4:8], surname + birthdate, nameup + birthdate[4:8],
    saname +birthdate[4:8], shname + birthdate[4:5],nick + birthdate[4:8],
    shname + birthdate[4:5] + n2, shname + birthdate[4:5] + n3,
    shname + birthdate[4:5],

    # Name+surname
    ns + n2, ns + n3, ns + y1, ns + y2, ns + y3, ns + y3, ns + y4, ns + y5,


    # Surname
    surname + n2, surname + n3, surname + y1, surname + y2, surname + y3, surname + y4, surname + y5,

    # Revours
    sn + n2, sn + n3, sn + y1, sn + y2, sn + y3, sn + y3, sn + y4, sn + y5, 
    

    # Capital
    nameup + y1, nameup + y2, nameup + y3, nameup + y4, nameup + y5,
    surnameup + y1, surnameup + y2, surnameup + y3, surnameup + y4, surnameup + y5,

    #nick
    nick + n3, nick + n2, nick + y1, nick + y5, nick + y6, nick + y3, nick + y4,
    # Symbol
    saname + n2, saname + n3, saname + y1, saname + y2, saname + y3, saname + y4, saname + y5, saname + y6,
    shname + n2, shname + n3, shname + y1, shname + y2, shname + y3, shname + y4, shname + y5, shname + y6,

    #alternative
    name[0:1]+saname[0:1]+y2+n2,name[0:1]+saname[0:1]+y3+n2,name[0:1]+saname[0:1]+y4+n2,
    name[0:1]+saname[0:1]+y5+n2,name[0:1]+saname[0:1]+y6+n2,


    name[0:1]+saname[0:1]+y2+n3,name[0:1]+saname[0:1]+y3+n3,name[0:1]+saname[0:1]+y4+n3,
    name[0:1]+saname[0:1]+y5+n3,name[0:1]+saname[0:1]+y6+n3,
    
    name[0:1]+surname[0:1]+y2+n2,name[0:1]+surname[0:1]+y3+n2,name[0:1]+surname[0:1]+y4+n2,
    name[0:1]+saname[0:1]+y5+n2,name[0:1]+saname[0:1]+y6+n2,


    name[0:1]+surname[0:1]+y2+n3,name[0:1]+surname[0:1]+y3+n3,name[0:1]+surname[0:1]+y4+n3,
    name[0:1]+surname[0:1]+y5+n3,name[0:1]+surname[0:1]+y6+n3,

    
    nameup+y2+n3,nameup+y3+n3,nameup+y4+n3,nameup+y2+n3,nameup+y5+n3,nameup+y6+n3,
    nameup+y2+n2,nameup+y3+n2,nameup+y4+n2,nameup+y2+n2,nameup+y5+n2,nameup+y6+n2,
    
    surnameup+y2+n3,surnameup+y3+n3,surnameup+y4+n3,surnameup+y2+n3,surnameup+y5+n3,surnameup+y6+n3,
    surnameup+y2+n2,surnameup+y3+n2,surnameup+y4+n2,surnameup+y2+n2,surnameup+y5+n2,surnameup+y6+n2,

    #phone no
    phone,
    name + p1,name + p2,name + p3,name + p4,name + p5,name + p6,
    nameup + p1,nameup + p2,nameup + p3,nameup + p4,nameup + p5,nameup + p6,
    surname + p1,surname + p2,surname + p3,surname + p4,surname + p5,surname + p6,
    surnameup + p1,surnameup + p2,surnameup + p3,surnameup + p4,surnameup + p5,surnameup + p6,

    #emali
    email[0:-10],

    #wife
    wife + y1,wife + y2,wife + y3,wife + y4,wife + y5,wife + y6,
    wife + y1 + n3,wife + y2 + n3,wife + y3 + n3,wife + y4 + n3,wife + y5 + n3,wife + y6 +n3,
    wife + y1 + n2,wife + y2 + n2,wife + y3 + n2,wife + y4 + n2,wife + y5 + n2,wife + y6 +n2,
  
    wifeup + y1,wifeup + y2,wifeup + y3,wifeup + y4,wifeup + y5,wifeup + y6,
    wifeup + y1 + n3,wifeup + y2 + n3,wifeup + y3 + n3,wifeup + y4 + n3,wifeup + y5 + n3,wifeup + y6 +n3,
    wifeup + y1 + n2,wifeup + y2 + n2,wifeup + y3 + n2,wifeup + y4 + n2,wifeup + y5 + n2,wifeup + y6 +n2,

    #kid
    kid + y1,kid + y2,kid + y3,kid + y4,kid + y5,kid + y6,
    kid + y1 + n3,kid + y2+ n3,kid + y3+ n3,kid + y4+ n3,kid + y5+ n3,kid + y6 + n3, 
    kid + y1 + n2,kid + y2+ n2,kid + y3+ n2,kid + y4+ n2,kid + y5+ n2,kid + y6 + n2,

    
    #kidn
    kidn + y1,kidn + y2,kidn + y3,kidn + y4,kidn + y5,kidn + y6,
    kidn + y1 + n3,kidn + y2+ n3,kidn + y3+ n3,kidn + y4+ n3,kidn + y5+ n3,kidn + y6 + n3, 
    kidn + y1 + n2,kidn + y2+ n2,kidn + y3+ n2,kidn + y4+ n2,kidn + y5+ n2,kidn + y6 + n2,
    kidn + kidb,

    #pet
    pet + y1,pet + y2,pet + y3,pet + y4,pet + y5,pet + y6,
    kidn + y1 + n3,kidn + y2+ n3,kidn + y3+ n3,pet + y4+ n3,pet + y5+ n3,pet + y6 + n3, 
    pet + y1 + n2,pet + y2+ n2,pet + y3+ n2,pet + y4+ n2,pet + y5+ n2,pet + y6 + n2,

    #company
    company + y1,


    #working process.....................................................
  )

  f = open(name +'.txt', 'w') 
  f.write(os.linesep.join(listing))


if __name__ == "__main__":
  interactive()
  print(drigen + Auhtor)
  
    

    

