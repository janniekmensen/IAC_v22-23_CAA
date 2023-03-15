import os
import sys
import subprocess

def menu():
    ''' Main menu '''
    
    chosen_element = 0
    
    print("#############################################################################")
    print("########                                                             ########")
    print("########                 Mijn Self Service Portal                    ########")
    print("######## ----------------------------------------------------------- ########")
    print("########             Doe iets met Vagrant en Ansible files           ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Kies een optie :                         ########")
    print("########                                                             ########")
    print("########             1) Klant1     |  2) Klant 2                     ########")
    print("########             3) Klant3     |                                 ########")
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Geef een nummer van 1 tot 5: ")

    if int(chosen_element) == 1:
        def menu1():
            ''' Klant1 menu '''
    
            chosen_element = 0
    
            print("#############################################################################")
            print("########                                                             ########")
            print("########                 Mijn Self Service Portal                    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########             Doe iets met Vagrant en Ansible files           ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Productie  |  2) Test                        ########")
            print("########                                                             ########")
            print("########      3) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 3: ")
        menu1()
        if int(chosen_element) == 1:
            def menu11():
               ''' Klant1 productie menu '''

            chosen_element = 0
    
            print("#############################################################################")
            print("########                                                             ########")
            print("########                 Mijn Self Service Portal                    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########             Doe iets met Vagrant en Ansible files           ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Web            |  2) Database                ########")
            print("########             3) Loadbalancer   |  4) Time                    ########")
            print("########                                                             ########")
            print("########      5) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 5: ")
        menu11()
        if int(chosen_element) == 1:
                    print('Deploy Klant1 Web in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    os.chdir('UbuntuWEB_VM')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "11.")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
    elif int(chosen_element) == 2:
        print('Deploy Klant 2VM')
    elif int(chosen_element) == 3:
        print('Deploy Klant 3VM')
    elif int(chosen_element) == 4:
        print('Deploy Klant 4VM')
    elif int(chosen_element) == 5:
        sys.exit()
    else:
        print('Sorry, de waarde moet tussen 1 en 5 zijn')

if __name__ == '__main__':
    ''' Python script main function '''
    
    menu()
