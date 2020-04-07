# 677 Lab 2

*How To Run The System*

1. Create a public-private key pair.
On the client (local) machine, run the following command:
ssh-keygen -t rsa
2. After this, you will be given the following prompt:
Enter file in which to save the key (/home/demo/.ssh/id_rsa):
Press Enter here.
3. After this you will be given the following prompt:
Enter passphrase (empty for no passphrase):
Press Enter here.
4. Copy the public key to the remote machine. For this you will need the ssh-copy-id command. It is installed by default in most linux variants. It won’t be installed on a Mac. Use the following command to install it if you are on a Mac:
    brew install ssh-copy-id
5. Copy the public key using the following command:
ssh-copy-id username@elnux.cs.umass.edu
Where username is your edlab username. Alternatively, you can also use the following command to paste the key:
cat ~/.ssh/id_rsa.pub | ssh username@elnux.cs.umass.edu "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >>  ~/.ssh/authorized_keys"
6. Enter your password, if prompted.
7. Now you should be able to login without using a password. Please test that you are able to do so before running the application.
8. Clone the git repo on on your edlab machine as well as your local machine
9. In the run_pygmy.sh script, make the following changes:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. In the user variable, assign your edlab username.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. In the remote_path give the remote directory where you cloned the repo. This can be done using the pwd command. Make sure to give a ‘/’ at the end of the path.
Example: /nfs/elsrv4/users1/grad/aayushgupta/cs677/
12. Run the script run_pygmy.sh on your local machine using the following commands:
	chmod +x run_pygmy.sh
	./run_pygmy.sh

This will spawn:  
The front end server on http://elnux3.cs.umass.edu:34600  
The order server on http://elnux2.cs.umass.edu:34601  
The catalog server on http://elnux1.cs.umass.edu:34602  
The client on your local machine.  
Once the tests are complete, you will be able to view the output and performance metric files for all the clients on your local machine, and the server logs will be stored under ‘front_end_server.txt’, ‘order_server.txt’ and ‘catalog_server.txt’ on your edLab machine in the src sub directory
