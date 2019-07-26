import os
import time

exit = 1
status = 0

while exit == 1:
    os.system("clear")
    if status == 0:
        print ("Check The README.md")
        print
        os.system("clear")
    print ("\033[1;32;40m Welcome To Domain_info_snagger")
    print ("")
    print ("\033[1;31;40m [1] " + "\033[1;32;40m EU Websites Lookup")
    print ("\033[1;31;40m [2] " + "\033[1;32;40m UK Websites Lookup")
    print ("\033[1;31;40m [99] " + "\033[1;32;40m Exit")
    print ("")
    choose = int(input('> '))
    if choose == 1:
        os.system("clear")
        print ("\033[1;31;40m [*] " + "\033[1;32;40m Launching The Eu Websites Lookup script...")
        time.sleep(4)
        os.system("clear")
        os.system("sudo python DomainLookUp_EU.py")

    else:
        if choose == 2:
            os.system("clear")
            print ("\033[1;31;40m [*] " + "\033[1;32;40m Launching The Uk Websites Lookup script...")
            time.sleep(4)
            os.system("clear")
            os.system("sudo python DomainLookUp_UK.py")

        else:
            if choose == 99:
                os.system("clear")
                print ("\033[1;31;40m [!] " + "\033[1;32;40m Exiting The Script and shutting everything down...")
