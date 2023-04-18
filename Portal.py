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
    print("########                        Hoofdmenu                            ########")
    print("######## ----------------------------------------------------------- ########")
    print("########                                                             ########")
    print("########                    Kies een optie :                         ########")
    print("########                                                             ########")
    print("########             1) Klant1     |  2) Klant2                      ########")
    print("########                                                             ########")
    print("########      3) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Geef een nummer van 1 tot 3: ")

    if int(chosen_element) == 1:
        def menu1():
            ''' Klant1 menu '''
    
        chosen_element = 0
    
        print("#############################################################################")
        print("########                                                             ########")
        print("########                 Mijn Self Service Portal                    ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                      Klant1 menu                            ########")
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
            print("########                  Klant 1 Productie menu                     ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Web            |  2) Database                ########")
            print("########             3) Loadbalancer   |                             ########")
            print("########                                                             ########")
            print("########      4) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 4: ")
            menu11()
            if int(chosen_element) == 1:
                    print('Deploy Klant1 Web in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    server = input("Welke database server wil je mee verbinden? Voer IP in van de server ")
                    loadbalance = input("Wil je deze toevoegen aan de loadbalancer om te scalen? ")
                    os.chdir('UbuntuWEB_VM')
                    os.chdir('files')
                    with open("index.php.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", server)
                    with open("index.php", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "11")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
                    if loadbalance == "ja":
                            os.chdir('..')
                            os.chdir('UbuntuLOAD_VM/files')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            with open ("haproxy.cfg", "a") as f:
                                fullip = "192.168.11.{}".format(ip)
                                f.write("\n")
                                f.write("    server web3 {}:80 check".format(fullip))
                            os.chdir('..')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            subprocess.call("ansible-playbook -i inventory.ini playbook.yml -Kk -u vagrant", shell=True)
            elif int(chosen_element) == 2:
                    print('Deploy Klant1 DB in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    os.chdir('UbuntuDB_VM')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "11")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 3:
                    print('Deploy Klant1 Load balancer in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    web1 = input("Welke webserver wil je loadbalancen? Voer IP in van server 1 ")
                    web2 = input("Welke webserver wil je loadbalancen? Voer IP in van server 2 ")
                    os.chdir('UbuntuLOAD_VM')
                    os.chdir('files')
                    with open("haproxy.cfg.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", web1)
                        template = template.replace("{{ web2 }}", web2)
                    with open("haproxy.cfg", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "11")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 4:
                 sys.exit()
            else:
                print('Sorry, de waarde moet tussen 1 en 4 zijn')
        elif int(chosen_element) == 2:
            def menu11():
               ''' Klant1 test menu '''

            chosen_element = 0
    
            print("#############################################################################")
            print("########                                                             ########")
            print("########                 Mijn Self Service Portal                    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                    Klant 1 Test menu                        ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Web            |  2) Database                ########")
            print("########             3) Loadbalancer   |                             ########")
            print("########                                                             ########")
            print("########      4) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 4: ")
            menu11()
            if int(chosen_element) == 1:
                    print('Deploy Klant1 Web in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    server = input("Welke database server wil je mee verbinden? Voer IP in van de server ")
                    os.chdir('UbuntuWEB_VM')
                    os.chdir('files')
                    with open("index.php.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", server)
                    with open("index.php", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "10")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
                    if loadbalance == "ja":
                            os.chdir('..')
                            os.chdir('UbuntuLOAD_VM/files')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            with open ("haproxy.cfg", "a") as f:
                                fullip = "192.168.10.{}".format(ip)
                                f.write("\n")
                                f.write("    server web3 {}:80 check".format(fullip))
                            os.chdir('..')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            subprocess.call("ansible-playbook -i inventory.ini playbook.yml -Kk -u vagrant", shell=True)
            elif int(chosen_element) == 2:
                    print('Deploy Klant1 DB in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    os.chdir('UbuntuDB_VM')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "10")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 3:
                    print('Deploy Klant1 Load balancer in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    web1 = input("Welke webserver wil je loadbalancen? Voer IP in van server 1 ")
                    web2 = input("Welke webserver wil je loadbalancen? Voer IP in van server 2 ")
                    os.chdir('UbuntuLOAD_VM')
                    os.chdir('files')
                    with open("haproxy.cfg.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", web1)
                        template = template.replace("{{ web2 }}", web2)
                    with open("haproxy.cfg", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "10")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL1TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 4:
                 sys.exit()
            else:
                print('Sorry, de waarde moet tussen 1 en 4 zijn')
    elif int(chosen_element) == 2:
        def menu1():
            ''' Klant2 menu '''
    
        chosen_element = 0
    
        print("#############################################################################")
        print("########                                                             ########")
        print("########                 Mijn Self Service Portal                    ########")
        print("######## ----------------------------------------------------------- ########")
        print("########                      Klant2 menu                            ########")
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
               ''' Klant2 productie menu '''

            chosen_element = 0
    
            print("#############################################################################")
            print("########                                                             ########")
            print("########                 Mijn Self Service Portal                    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                  Klant 2 Productie menu                     ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Web            |  2) Database                ########")
            print("########             3) Loadbalancer   |                             ########")
            print("########                                                             ########")
            print("########      4) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 4: ")
            menu11()
            if int(chosen_element) == 1:
                    print('Deploy Klant2 Web in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    server = input("Welke database server wil je mee verbinden? Voer IP in van de server ")
                    os.chdir('UbuntuWEB_VM')
                    os.chdir('files')
                    with open("index.php.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", server)
                    with open("index.php", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "21")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
                    if loadbalance == "ja":
                            os.chdir('..')
                            os.chdir('UbuntuLOAD_VM/files')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            with open ("haproxy.cfg", "a") as f:
                                fullip = "192.168.21.{}".format(ip)
                                f.write("\n")
                                f.write("    server web3 {}:80 check".format(fullip))
                            os.chdir('..')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            subprocess.call("ansible-playbook -i inventory.ini playbook.yml -Kk -u vagrant", shell=True)
            elif int(chosen_element) == 2:
                    print('Deploy Klant2 DB in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    os.chdir('UbuntuDB_VM')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "21")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 3:
                    print('Deploy Klant2 Load balancer in Productieomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    web1 = input("Welke webserver wil je loadbalancen? Voer IP in van server 1 ")
                    web2 = input("Welke webserver wil je loadbalancen? Voer IP in van server 2 ")
                    os.chdir('UbuntuLOAD_VM')
                    os.chdir('files')
                    with open("haproxy.cfg.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", web1)
                        template = template.replace("{{ web2 }}", web2)
                    with open("haproxy.cfg", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "21")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2PROD")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 4:
                 sys.exit()
            else:
                print('Sorry, de waarde moet tussen 1 en 4 zijn')
        elif int(chosen_element) == 2:
            def menu11():
               ''' Klant2 test menu '''

            chosen_element = 0
    
            print("#############################################################################")
            print("########                                                             ########")
            print("########                 Mijn Self Service Portal                    ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                    Klant 2 Test menu                        ########")
            print("######## ----------------------------------------------------------- ########")
            print("########                                                             ########")
            print("########                    Kies een optie :                         ########")
            print("########                                                             ########")
            print("########             1) Web            |  2) Database                ########")
            print("########             3) Loadbalancer   |                             ########")
            print("########                                                             ########")
            print("########      4) Exit                                                ########")
            print("########                                                             ########")
            print("#############################################################################")
            chosen_element = input("Geef een nummer van 1 tot 4: ")
            menu11()
            if int(chosen_element) == 1:
                    print('Deploy Klant2 Web in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    server = input("Welke database server wil je mee verbinden? Voer IP in van de server ")
                    os.chdir('UbuntuWEB_VM')
                    os.chdir('files')
                    with open("index.php.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", server)
                    with open("index.php", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "20")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
                    if loadbalance == "ja":
                            os.chdir('..')
                            os.chdir('UbuntuLOAD_VM/files')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            with open ("haproxy.cfg", "a") as f:
                                fullip = "192.168.20.{}".format(ip)
                                f.write("\n")
                                f.write("    server web3 {}:80 check".format(fullip))
                            os.chdir('..')
                            currentdir = os.getcwd()
                            print("Current directory %s" % currentdir)
                            subprocess.call("ansible-playbook -i inventory.ini playbook.yml -Kk -u vagrant", shell=True)
            elif int(chosen_element) == 2:
                    print('Deploy Klant2 DB in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    os.chdir('UbuntuDB_VM')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "20")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 3:
                    print('Deploy Klant2 Load balancer in Testomgeving')
                    naam = input("Hoe moet de VM heten? ")
                    ip = input("Welk nummer moet het IP krijgen in de host ID? ")
                    web1 = input("Welke webserver wil je loadbalancen? Voer IP in van server 1 ")
                    web2 = input("Welke webserver wil je loadbalancen? Voer IP in van server 2 ")
                    os.chdir('UbuntuLOAD_VM')
                    os.chdir('files')
                    with open("haproxy.cfg.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ web1 }}", web1)
                        template = template.replace("{{ web2 }}", web2)
                    with open("haproxy.cfg", "w") as f:
                         f.write(template)
                    os.chdir('..')
                    with open("Vagrantfile.template", "r") as f:
                        template = f.read()
                        template = template.replace("{{ define }}", naam)
                        template = template.replace("{{ hostname }}", naam)
                        template = template.replace("{{ subnet }}", "20")
                        template = template.replace("{{ host }}", ip)
                        template = template.replace("{{ VMNET }}", "VMNETKL2TEST")
                    with open("Vagrantfile", "w") as f:
                        f.write(template)
                    subprocess.call("vagrant up", shell=True)
            elif int(chosen_element) == 4:
                 sys.exit()
            else:
                print('Sorry, de waarde moet tussen 1 en 4 zijn')
        elif int(chosen_element) == 3:
             sys.exit()
    elif int(chosen_element) == 3:
        sys.exit()
    else:
        print('Sorry, de waarde moet tussen 1 en 3 zijn')

if __name__ == '__main__':
    ''' Python script main function '''
    
    menu()
