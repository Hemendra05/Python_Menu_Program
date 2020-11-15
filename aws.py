import os
def AWS_Menu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t -----------------------")    
        print("\t\t\t Welcome To AWS Services")
        print("\t\t\t -----------------------")
        os.system("tput setaf 7")
        os.system("tput setaf 2")
        print("""
            Press 1: To Configure AWS 
            Press 2: To Create a Key Pair
            Press 3: To Create a Security Group 
            Press 4: To Launch an EC2 Instance
            Press 5: To Stop an EC2 Instance
            Press 6: To Create an EBS Volume
            Press 7: To Attach the EBS volume to an EC2 Instance
            Press 8: To Create an S3 Bucket
            Press 9: To Delete an S3 Bucket
            Press 10: Exit
            """)
        print()
        os.system("tput setaf 3")
        ch = int(input("Enter your choice:- "))
        os.system("tput setaf 7")
        if ch == 1:
            print()
            os.system("aws configure")
            os.system("tput setaf 3")
            input("Press enter to continue")
            os.system("tput setaf 7")
        elif ch == 2:
            os.system("tput setaf 3")
            KeyName = input("Enter key-pait name: ")
            os.system("tput setaf 7")
            os.system("aws ec2 create-key-pair --keyname {}".format(KeyName))
            os.system("tput setaf 3")
            input("Press enter to continue")
            os.system("tput setaf 7")
        elif ch == 3:
            print()
            os.system("tput setaf 3")
            sg_name = input("Enter Security Group Name: ")
            sg_desc = input("Enter the description: ")
            os.system("aws ec2 create-security-group --group-name {0} --description {1} ".format(sg_name,sg_desc))
            print("Add rule to the security group")
            protocol = input("Enter the protocol: ")
            port = input("Enter the port number: ")
            cidr = input("Enter the CIDR: ")
            os.system("aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}".format(sg_name,protocol,port,cidr))
            input("Press enter to continue")
        elif ch == 4:
            print()
			ami = input('Enter AMI id to Launch Instance : ')
			itype = input("Enter Instance type : ")
			count = input('Enter Number of Instances to launch : ')
			sg_id = input('Enter Security Group Id to attach to the Instance : ')
			key_name = input('Enter Key to attach to ec2 Instance : ')
			os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {} --region us-east-1 '.format(ami , itype , count , sg_id , key_name))
			print()
			print('Instance Successfully Launched ')
			print()
        elif ch == 5:
            print()
			ec2_id = input("Enter Instance Id to stop Instance")
			os.system('aws ec2 stop-instances --instance-ids {}  --region us-east-1'.format(id))
			print()
			print('Instance Successfully Stopped ')
			print()
        elif ch == 6:
            print()
			az = input('Enter the Availablity Zone to Create EBS Volume : ')
			size = input('Enter the Size of EBS Volume : ')
			os.system('aws ec2 create-volume --availability-zone {} --size {} --region us-east-1'.format(az , size))
			print()
			print('EBS Volume Created. Keep the volume ID for future references ')
			print()
        elif ch == 7:
            print()
			ebs_id = input('Enter EBS Volume ID to Attach to EC2 Instance : ')
			instance_id = input('Enter EC2 Instance ID to attach EBS Volume : ')
			os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf --region us-east-1'.format(ebs_id , instance_id))
			print()
			print('EBS Volume Attached ')
			print()
        elif ch == 8:
            print()
			s3_bucket_name = input("Enter S3 bucket name : ")
			os.system('aws s3api create-bucket --bucket {} --region us-east-1 '.format(s3_bucket_name))	
			print()
			print('S3 Bucket Created Successfully ')
			print()
        elif ch == 9:
            print()
			s3_bucket_name = input("\t\tEnter S3 bucket name to delete : ")
			os.system('aws s3 rm --recursive s3://{}'.format(s3_name))
			os.system('aws s3api delete-bucket --bucket {} --region us-east-1'.format(s3_bucket_name))
			print()
			print('Bucket Deleted Successfully ')
			print()
        elif ch == 10:
            break
        else:
            print("Invalid Choice")
            print()




