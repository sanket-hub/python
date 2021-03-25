import os;
import getpass;

password=getpass.getpass("Enter your password : ");

if password!='123':
	os.system("tput setaf 1");
	print("Wrong Password");
	os.system("tput setaf 7");	
	exit();

"""print("Where you want to run this menu ? ");
print("Press 1 : Local");
print("Press 2 : Remote");
loc=int(input("Eneter your choice : "));"""


def main_menu():
 print("\t\t\t---------------------");
 os.system("tput setaf 3");
 print("\t\t\tWelcome To Main Menu !!");
 os.system("tput setaf 7");
 print("\t\t\t---------------------");
 print("""
	1: Basic Linux Commands
	2: Docker
	3: AWS
	4: Hadoop	
	6: configure web server
	7: Exit
	""")

def linux():
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 3")
	print("\t\t\tWELCOME TO Linux OS")
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 7")
	login=input("you want to login local/remote :-")
	
	while True:
		#os.system("clear");
		if login=="local":
			print("""
			Select Option
			1. See Date
			2. See Calendor
			3. Show Partition
			4. Show System Info
			5. Show Memory Status
			6. Show All Mounted Devices
			7. Show IP Address
			8. Go To Main Menu
			""")
			input_user=input("Enter your choice:-")
			if int(input_user)==1:
				os.system("date")
			elif int(input_user)==2:
				os.system("cal")
			elif int(input_user)==3:
				os.system("fdisk -l")
			elif int(input_user)==4:
				os.system("lscpu")
			elif int(input_user)==5:
				os.system("free -m");
			elif int(input_user)==6:
				os.system("df -h")
			elif int(input_user)==7:
				os.system("ifconfig")
			elif int(input_user)==8:
				return;
			else:
				os.system("tput setaf 1")
				print("\t\t\tinvalid choice")
				os.system("tput setaf 7")
			#os.system("clear");
                      

def docker(): 
    os.system("tput setaf 2")
    print("********************************************************************************")
    os.system("tput setaf 3")
    print("\t\t\tWELCOME TO DOCKER SETUP")
    os.system("tput setaf 2")
    print("********************************************************************************")
    os.system("tput setaf 7")
    login=input("you want to login local/remote:-")
	
    os.system("clear")
    while True:

        os.system("tput setaf 1")
        print("\t\tDOCKER Set-Up\n")
        os.system("tput setaf 7")
        print('''1. Check Docker install or not
		 2. If not, Then Install Docker
		 3. Start the docker service 
		 4. Check Info about Docker
            	 5. Show How many Docker Image have
                 6. Download Docker Image
		 7. Check How many Containers are running or stopped
		 8. Launch New Container 
		 9. Go Inside the Container 
		10. Shut down Container 
		11. Start the Container 
		12. Back to main menu''')


        
        i = input("Enter Options : ")
        if int(i)==1:
            os.system("docker version")
        elif int(i)==2:
            os.system("yum install docker-ce --nobest")
        elif int(i)==3:
            os.system("systemctl start docker")
        elif int(i)==4:
            os.system("docker info")
        elif int(i)==5:
            os.system("docker images")
        elif int(i)==6:
            print("First, Search the OS Image ....")
            s = input("Write Image name for searching: ")
            os.system("docker search {}".format(s))
            print("Now, Go for Download the Image....")
            d = input("Write the Image name: ")
            v = input("Type Image Version name: ")
            os.system("docker pull {0}:{1}".format(d,v))
        elif int(i)==7:
            os.system("docker ps -a")
        elif int(i)==8:
            n = input("Type Container name: ")
            m = input("Type Image name: ")
            v = input("Type Image Version name: ")
            os.system("docker run -dit --name {0} {1}:{2}".format(n,m,v))
        elif int(i)==9:
            n = input("Type Container name: ")
            os.system("docker attach {}".format(n))
        elif int(i)==10:
            n = input("Type Container name: ")
            os.system("docker stop {}".format(n))
        elif int(i)==11:
            n = input("Type Container name: ")
            os.system("docker start {}".format(n))
        elif int(i)==12:
            break
        else:
            os.system("tput setaf 1")
            print("Please Enter only valid options")
            os.system("tput setaf 7")


def aws():
	
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 3")
	print("\t\t\tWELCOME TO AWS SETUP")
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 7")
	login=input("you want to login local/remote:-")
	while True:
		if login=="local":
			print("""\n
			press0 : To install AWS CLI in linux
			press1 : aws configuration
			press2 : create key pair
			press3 ; create security group
			press4 : autherize security group
			press5 : launch instance
			press6 : create EBS volume
			press7 : attach EBS volume to Ec2
			press8 : Detach volume
			press9 : Delete instance
			press10 : exit
					""")
			ch=input("Enter your choice:-")
			if int(ch) ==0:
				os.system("pip3 install awscli --upgrade --user")
				os.system("export PATH=~/.local/bin:$PATH")
				os.system("source ~/.bash_profile")
			
			if int(ch) == 1:
		
				os.system("aws configure")
				akey = input("enter access key-id : ")
				skey = input("enter secret key-id : ")
				nm = input("enter region-name : ")
				frmt = input("enter output format-type : ")
				os.system("{}".format(akey))
				os.system("{}".format(skey))
				os.system("{}".format(nm))
				os.system("{}".format(frmt))
		
			if int(ch) == 2:
				name = input("enter key name:- ")
				os.system("aws ec2 create-key-pair --key-name {}".format(name))
			if int(ch) == 3:
	
				sgname = input("enter security group name : ")
				os.system("aws ec2 create-security-group --group-name {} --description menuSG".format(sgname))
	
			if int(ch) == 4:
				sgid = input("enter your created security group-id : ")
				p = input("give protocol value : ")
				os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port 22 --cidr 0.0.0.0/0".format(sgid,p))
		
			if int(ch) == 5:
				imid = input("enter image-id : ")
				itype = input("enter instance-type : ")
				count = input("enter how many instance you want to install : ")
				subnet = input("enter subnet-id : ")
				sgid = input("enter your created security group id : ")
				name = input("enter your created key-name : ")
				os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name{}".format(imid,itype,count,subnet,sgid,name))    

			if int(ch) == 6:
				vtype = input("enter volume-type : ")
				vsize = input("enter size of the volume : ")
				vazone = input("enter availability zone : ")
				os.system("aws ec2 create-volume --volume-type {} --size {} availability-zone {}".format(vtype,vsize,vazone))
	
			if int(ch) == 7:
				inid = input("enter instance-id : ")
				vid = input("enter volume-id : " )
				dtype = input("enter device-type : ")
				os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(inid,vid,dtype))
	
			if int(ch) == 8:
				vid = input("enter volume-id : ")
				os.system("aws ec2 detach-volume --volume-id {}".format(vid))

			if int(ch) == 9:
				inid = input("enter instance-id : ")
				os.system("aws ec2 terminate-instances --instance-id {}".format(inid))
			if int(ch) == 10:
				break
		
			else:
				print("Please Enter only valid options")
            	
		if login=="remote":
			ip=input("enter remote ip:-")
			print("ip")
			print("""\n
			press0 : To install AWS CLI in linux
			press1 : aws configuration
			press2 : create key pair
			press3 ; create security group
			press4 : autherize security group
			press5 : launch instance
			press6 : create EBS volume
			press7 : attach EBS volume to Ec2
			press8 : Detach volume
			press9 : Delete instance
			press10 : exit
					""")
			ch=input("Enter your choice")
			if int(ch) ==0:
				os.system("pip3 install awscli --upgrade --user")
				os.system("export PATH=~/.local/bin:$PATH")
				os.system("source ~/.bash_profile")
			if int(ch) == 1:
		
				os.system("aws configure")
				akey = input("enter access key-id : ")
				skey = input("enter secret key-id : ")
				nm = input("enter region-name : ")
				frmt = input("enter output format-type : ")
				os.system("{}".format(akey))
				os.system("{}".format(skey))
				os.system("{}".format(nm))
				os.system("{}".format(frmt))
		
			elif int(ch) == 2:
				name = input("enter key name : ")
				os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(ip,name))
			elif int(ch) == 3:

				sgname = input("enter security group name : ")
				os.system("ssh {} aws ec2 create-security-group --group-name {} --description menuSG".format(ip,sgname))

			elif int(ch) == 4:
				sgid = input("enter your created security group-id : ")
				p = input("give protocol value : ")
				os.system("ssh {} aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port 22 --cidr 0.0.0.0/0".format(ip,sgid,p))
		
			elif int(ch) == 5:
				imid = input("enter image-id : ")
				itype = input("enter instance-type : ")
				count = input("enter how many instance you want to install : ")
				subnet = input("enter subnet-id : ")
				sgid = input("enter your created security group id : ")
				name = input("enter your created key-name : ")
				os.system("ssh {} aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name  {}".format(ip,imid,itype,count,subnet,sgid,name))    

			elif int(ch) == 6:
				vtype = input("enter volume-type : ")
				vsize = input("enter size of the volume : ")
				vazone = input("enter availability zone : ")
				os.system("ssh {} aws ec2 create-volume --volume-type {} --size {} availability-zone {}".format(ip,vtype,vsize,vazone))
	
			elif int(ch) == 7:
				inid = input("enter instance-id : ")
				vid = input("enter volume-id : " )
				dtype = input("enter device-type : ")
				os.system("ssh {} aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(ip,inid,vid,dtype))

			elif int(ch) == 8:
				vid = input("enter volume-id : ")
				os.system("ssh {} aws ec2 detach-volume --volume-id {}".format(ip,vid))

			elif int(ch) == 9:
				inid = input("enter instance-id : ")
				os.system("ssh {} aws ec2 terminate-instances --instance-id {}".format(ip,inid))
			elif int(ch) ==10:
				break
		
			else:
            			os.system("tput setaf 1")
            			print("Please Enter only valid options")
            			os.system("tput setaf 7")
		
def hadoop():
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 3")
	print("\t\t\tWELCOME TO HADOOP SETUP")
	os.system("tput setaf 2")
	print("********************************************************************************")
	os.system("tput setaf 7")
	login=input("you want to login local/remote:-")
	
	while True:
		if login=="local":
			print("""
			1. Download jdk software
			2. install jdk software
			3. Download Hadoop software
			4. install Hadoop software
			5. Set-up Namenode
			6. Set-up Datanode
			7. Start Namenode
			8. Start Datanode
			9. Set-up Client
			10. Go back to main menu
				""")
			input_user=input("Enter your choice:-")
			if int(input_user)==1:
				os.system("https://download.oracle.com/otn/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.rpm")
			elif int(input_user)==2:
				os.system(" rpm -i jdk-8u171-linux-x64.rpm")
			elif int(input_user)==3:
				os.system("wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
			elif int(input_user)==4:
				os.system(" rpm -i  hadoop-1.2.1-1.x86_64.rpm --force")
			elif int(input_user)==5:
				print("\t\t\tGive details about namenode:")
				nn_ip= input("\t\tGive IP that u want to configure as nn:-")
			
				nn_folder= input("folder name of namenode:-")
				os.system("mkdir /{}".format(nn_folder))
				hdfs = open("/etc/hadoop/hdfs-site.xml","w")
				hdfs_data = """ <?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n""".format(nn_folder)
				hdfs.write(hdfs_data)
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name></name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
				
			elif int(input_user)==6:
				print("\t\t\tGive details about Datanode:")
				nn_ip= input("\t\tGive IP that u want to configure as nn:-")
				dn_folder= input("folder name of datanode:-")
				os.system("mkdir /{}".format(dn_folder))
				hdfs = open("/etc/hadoop/hdfs-site.xml","w")
				hdfs_data = """ <?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n""".format(dn_folder)
				hdfs.write(hdfs_data)
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
			elif int(input_user)==7:
				os.system("hadoop-daemon.sh start namenode")
				os.system("jps")
			elif int(input_user)==8:
				os.system("hadoop-daemon.sh start datanode")
				os.system("jps")
			elif int(input_user)==9:
				print("\t\t\tGive details of Client:")
				nn_ip= input("\t\t IP of Namenode:-")		
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
			elif int(input_user)==10:
				break
			else:
				os.system("tput setaf 1")
				print("Please Enter only valid options")
				os.system("tput setaf 7")
		elif login=="remote":
			ip = input("enter remote-ip : ")
			print(ip)		
			print("""
			1. Download jdk software
			2. install jdk software
			3. Download Hadoop software
			4. install Hadoop software
			5. Set-up Namenode
			6. Set-up Datanode
			7. Start Namenode
			8. Start Datanode
			9. Set-up Client
			10. Go back to main menu
				""")
			input_user=input("Enter ur choice:-") 
			
			if int(input_user)==1:
				os.system("ssh {} https://download.oracle.com/otn/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.rpm".format(ip))
			elif int(input_user)==2:
				os.system("ssh {} rpm -i jdk-8u171-linux-x64.rpm".format(ip))
			elif int(input_user)==3:
				os.system("ssh {} wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm".format(ip))
			elif int(input_user)==4:
				os.system("ssh {} rpm -i  hadoop-1.2.1-1.x86_64.rpm --force".format(ip))
			elif int(input_user)==5:
				print("\t\t\tGive details about namenode:")
				nn_ip= input("\t\tGive IP that u want to configure as nn:-")
			
				nn_folder= input("folder name of namenode:-")
				os.system("ssh {} mkdir /{}".format(ip,nn_folder))
				hdfs = open("/etc/hadoop/hdfs-site.xml","w")
				hdfs_data = """ <?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n""".format(nn_folder)
				hdfs.write(hdfs_data)
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name></name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
				
		
			elif int(input_user)==6:
				print("\t\t\tGive details about Datanode:")
				nn_ip= input("\t\tGive IP that u want to configure as nn:-")
				dn_folder= input("folder name of datanode:-")
				os.system("ssh {} mkdir /{}".format(ip,dn_folder))
				hdfs = open("/etc/hadoop/hdfs-site.xml","w")
				hdfs_data = """ <?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n""".format(dn_folder)
				hdfs.write(hdfs_data)
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
			elif int(input_user)==7:
				os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
				os.system("ssh {} jps".format(ip))
			elif int(input_user)==8:
				os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
				os.system("ssh {} jps".format(ip))
			elif int(input_user)==9:
				print("\t\t\tGive details of Client:")
				nn_ip= input("\t\t IP of Namenode:-")		
				core=open("/etc/hadoop/core-site.xml","w")
				core_data="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xs1" href="configuration.xs1"?>
<!-- put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>\n""".format(nn_ip)
				core.write(core_data)
		


			elif int(input_user)==10:
				break
        	
			else:
				os.system("ssh {} tput setaf 1".format(ip))
				print("Please Enter only valid options")
				os.system("ssh {} tput setaf 7".format(ip))


def webserver():
	login=input("You want to configure webserver remote/local")
	if login=="local":
		os.system("yum install httpd")
		os.system("systemctl start httpd")
		os.system("systemctl enable httpd")
		os.system("systemctl status httpd")
	if login=="remote":
				
		ip=input("Enter your remote IP")
		print('ip')		
		os.system("ssh {} yum install httpd".format(ip))
		os.system(" ssh {} systemctl start httpd".format(ip))
		os.system("ssh {} systemctl enable httpd".format(ip))




while True:

	os.system("clear") 
	main_menu()
	user_input = int(input("Enter your choice : "))
	
	if user_input==1:
		linux();
	if user_input==2:
		docker();
	elif user_input==3:
		aws()
	elif user_input==4:
		hadoop()
	elif user_input==6:
		webserver()
	elif user_input==7:
		break
	else:
		os.system("tput setaf 3")
		print("\t\t\tinvalid choice")
		os.system("tput setaf 7")
