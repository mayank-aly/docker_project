import os                                                                              # os module for linux commands
from pyfiglet import Figlet                                                             #figlet library for banner fonts 


def render(text,style):
	f=Figlet(font=style)
	print('\n'*1)
	print(f.renderText(text))
os.system("clear")
os.system("tput setaf 3")
render('DOCKER PROJECT','epic')
os.system("tput setaf 7")

os.system("tput setaf 10")
render('\t by Mayank Varshney','digital')

os.system("tput setaf 2")
print("1. Enter MAIN MENU")
print("2. EXIT")
print("Enter Your Choice ", end=" : ")
x=input()

if int(x)==1:                                                                              #main menu
    while True:
        os.system("clear")
        os.system("tput setaf 10")
        render('                              MAIN MENU','bubble')
        os.system("tput setaf 33")
        print("""
            Press 1: Pull the image (Content Manegement System) (Choose and Install)
            Press 2: Pull the image (For the Database) (Choose and Install)
            Press 3: SetUp Your Environment.
            Press 4: Deploy Your Services.
            Press 5: Run Infrastructure using Docker-Compose
            Press 6: Exit
            """)
        os.system("tput setaf 33")
        print("Enter Your Choice: ",end=" ")
        ch=input()
        os.system("tput setaf 7")
        if int(ch)==1:                                                                      # content management system
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('CONTENT  MANAGEMENT SYSTEM','digital')
                os.system("tput setaf 33")

                print("""\t\t    Welcome To SetUp Your WebApp Images  
                 ------------Select the CMS---------------""")
                
                print("""
                    Press 1: Joomla
                    Press 2: WordPress
                    Press 3: Drupal
                    Press 4: Back
                    """)
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")

                if int(ch1)==1:
                    os.system("docker pull joomla")
                elif int(ch1)==2:
                    os.system("docker pull wordpress:5.1.1-php7.3-apache")
                elif int(ch1)==3:
                    os.system("docker pull drupal:latest")
                elif int(ch1)==4:
                    break
        if int(ch)==2:                                                                                  # database management system
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('DATABASE MANAGEMENT SYSTEM','digital')
                os.system("tput setaf 33")
                print("""
                    -----------------------Welcome To Setup Your DataBase----------------
                    """)
                
                print("""
                    Press 1: MySQL
                    Press 2: Mongo
                    Press 3: Back
                    """)
                
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")
                if int(ch1)==1:
                    os.system("docker pull mysql:5.7")
                elif int(ch1)==2:
                    os.system("docker pull mongo")
                elif int(ch1)==3:
                    break

        elif int(ch)==3:                                                # environment setup
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('ENVIRONMENT SETUP','bubble')
                os.system("tput setaf 33")
                print("""
                    ---------------Welcome To SetUp Your Environment----------------
                    """)
               
                print("""
                       Follow the Steps:
                       Step 1:Lets Create Our Own Network
                       Step 2:Create The Volume/Storage For the CMS and DATABASE
                       Step 3: Back
                    """)
                
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                if int(ch1)==1:
                    print("Enter The Name of Your Network: ",end=" ")
                    net_name=input()
                    os.system("tput setaf 3")
                    os.system("docker network create --driver bridge {0}".format(net_name))
                    print("""----->>>>Successfully You Have Created Your Network.<<<<<-------
                        These List of your Own Network: 
                        """)
                    
                    os.system("docker network list")
                    os.system("tput setaf 7")
                    input()
                elif int(ch1)==2:
                    os.system("tput setaf 3")
                    print("""
                        >>>> For making our environment as persistent/permanent we need make the storage
                             To collect the data from the server....
                             """)
                    print("Enter storage name for database",end=" : ")
                    dock_storage_name=input()
                    os.system("docker volume create {0}".format(dock_storage_name))   


                    print("Enter storage name for CMS",end=" : ")
                    dock_storage_cms=input()
                    os.system("docker volume create {0}".format(dock_storage_cms))               
                    print("List of storage created",end = " : ")
                    os.system("docker volume ls")
                    input()
                elif int(ch1)==3:
                    break
        
        elif int(ch)==4:                                                                # deploy  services
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('DEPLOY SERVICES','bubble')
                os.system("tput setaf 33")
                print("""
                    Press 1: First Deploy the Database to Store the data.
                    Press 2: Secondly Deploy the WebApp.
                    Press 3: Back
                    """)
                
                print("Enter the Choice: ",end=" ")
                ch1=input()
                
                if int(ch1)==1:
                    while True:
                        
                        print("""
                              Choose An Image For the Database: 
                              Press 1: MySQL
                              Press 2: Mongo
                              """)
                        print("Enter Your Choice: ",end=" ")
                        ch2=input()
                        os.system("tput setaf 3")
                        if int(ch2)==1:
                            print("Choose the Root Password and Enter Here: ",end=" ")
                            root_pass=input()
                            print("Enter the name of the USER: ",end=" ")
                            user_name=input()
                            print("Enter the Password for this USER: ",end=" ")
                            user_pass=input()
                            print("Give The name to your Database: ",end=" ")
                            db_name=input()
                            print("These are the Local Storage which you have made choose from here : ")
                            os.system("docker volume ls")
                            print("Enter the Name of Docker_storage:  ",end=" ")
                            db_os_name=input()
                            print("Give the name to your container(this name will be used to link): ",end=" ")
                            nam_cont=input()
                            os.system("docker run -dit -e MYSQL_ROOT_PASSWORD={0} -e MYSQL_USER={1} -e MYSQL_PASSWORD={2} -e MYSQL_DATABASE={3} -v {4}:/var/lib/mysql --name {5} mysql:5.7".format(root_pass,user_name,user_pass,db_name,db_os_name,nam_cont))
                            break
                        elif int(ch2)==2:	
                            print("Check That Here container is running or Not: ")
                            os.system("docker ps -a")
                            input()
                            break
                elif int(ch1)==2:
                    os.system("tput setaf 33")
                    while True:
                        print(""" 
                            Choose an image for the WebApp: 
                            Press 1: WordPress
                            Press 2: Joomla
                            Press 3: Drupal
                            """)
                        print("Enter Your Choice: ",end=" ")
                        ch2=input()
                        if int(ch2)==1:
                            os.system("tput setaf 3")
                            print("\t\t----IMPORTANT NOTE (Give The Informataion Same as the DATABASE IMAGE)",end="\n ")
                            print("Enter the Host Name: ",end=" ")
                            host_name=input()
                            print("Enter DB USER NAME: ",end=" ")
                            user_name=input()
                            print("Enter DB USER Password : ",end=" ")
                            user_pass=input()
                            print("Enter DB name: ",end=" ")
                            db_name=input()
                            print("These are the Local Storage which you have made choose from here : ")
                            os.system("docker volume ls")
                            print("Storage Name For this WebApp Image: ",end=" ")
                            dock_storage_name=input()
                            print("Give the name to for this image: ",end=" ")
                            db_os_name=input()
                            
                            os.system("docker run -dit -e WORDPRESS_DB_HOST={0} -e WORDPRESS_DB_USER={1} -e WORDPRESS_DB_PASSWORD={2} -e WORDPRESS_DB_NAME={3} -v {4}:/var/www/html --link {0} -p 8080:80 --name {5} wordpress:5.1.1-php7.3-apache".format(host_name,user_name,user_pass,db_name,db_os_name,db_os_name))
                            input()
                            break

                    '''Now, As we SetUp Everything. Lets See the Steps ......................
                               (How our Client Can Acess these Services ?) 
                    Now, These Whole Scenerio we made on The Load Balancer.........
                      Client Should be the Part Of this Network for this Type Scenerio.
                      Now, Client Have Choic to access by: 
                         ------>>> By the Alias Name
                         ------>>> By the Host Name(Container Name)
                         ------>>> By the IP:Port Number
                    '''

                elif int(ch1)==3:
                    break
        elif int(ch)==5:                      # docker compose 
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('DOCKER COMPOSE','bubble')
                os.system("tput setaf 33")
                
                print("Press 1. Run wordpress infrastructure(docker-compose)")
                print("Press 2. Stop docker-compose")
                print("Press 3. Start docker-compose")
                print("Press 4. Remove complete infrastructure")
                print("Press 5. BACK")
                print("Enter Your Choice: ",end=" ")
                ch2=input()
                os.system("tput setaf 3")
                
                if int(ch2)==1:
                     os.system("docker-compose up -d")
                     print("Infrastructure Setup Complete.....")
                     input()
                     

                elif int(ch2)==2:
                     os.system("docker-compose stop")
                     print("Stopped.....")
                     input()
                     

                elif int(ch2)==3:
                     os.system("docker-compose start")
                     print("Started.....")
                     input()
                     
                elif int(ch2)==4:
                     os.system("docker-compose rm")
                     print("Removed.....")
                     input()
                     

                elif int(ch2)==5:
                     break

        elif int(ch)==6:
            os.system("clear")
            os.system("tput setaf 3")
            render('THANK YOU','epic')
            os.system("tput setaf 7")
            break
        
   
else :
    os.system("clear")
    os.system("tput setaf 3")
    render('THANK YOU','epic')
    os.system("exit")
    os.system("tput setaf 7")
 
