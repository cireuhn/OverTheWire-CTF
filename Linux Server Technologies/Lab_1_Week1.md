# Lab 1 

## Part 1. Change the VM’s IP address and hostname to lst1 

1. Create a new file for netplan.
- I created a file called static.yaml
- Format for a Static IP address is as follows in netplan :
```
network:
  ethernets:
    ens33:
      dhcp4: false
      addresses: [192.168.10.201/24]
      nameservers:
        addresses: [192.168.10.1]
      routes:
      - to: default
        via: 192.168.10.1
  version: 2
```
2. Apply new file by performing ``` sudo netplan appply ```  

Submit a screenshot displaying the netplan yaml file and that the IP address was changed.  
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-1.png)

3. Change hostname of the device

- Verify by performing ```hostnamectl```

- Set a new hostname:
``` sudo hostnamectl set-hostname lst1```

Submit a screenshot displaying the new hostname.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-2.png)  
## Part 2. Install stress-ng

- Verify if it exist by performing ``` apt list | grep stress-ng```
- Install by performing ``` apt install stress-ng```

Submit a screenshot showing that stress-ng is installed.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-3.png)
## Part 3. Create a bob and alice account. Create an adminjr group.

1. Create user bob and alice
- Perform:
```sudo adduser bob```
```sudo adduser alice```
```sudo groupadd adminjr```

Login as bob and attempt to change alice’s password.
Submit a screenshot of bob’s failed attempt to change alice’s password.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-4.png)  

Configure the adminjr group to change passwords.

2. Edit the sudoers file:
 - Add ```%adminjr ALL=(ALL) /usr/bin/passwd``` to the end of the file

Add bob to the adminjr group.

3. ```sudo usermod -aG adminjr bob```
- Verify `groups bob`
Submit a screenshot of bob changing alice’s passwd.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-5.png)  

## Part 4. Install SAR execute the cpubusy script and show CPU stress

Install sysstat. Verify installation

4. `apt install stasstat`

Download cpubusy.py

- Download this file from the repository from the instructor.
- Transfer over from local machine to VM using WinSCP
- Swap File protocol to `SCP`
- Host name field should be IP address of Destination (VM)
- Using port 22 to leverage SSH
- Drag file from local machine to VM

![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-6.png)

Using sar demonstrate that the CPU performance is degraded when executing the spubus.py script.

5. Run the cpubusy.py script on the VM machine
- `./cpybusy.py`
- Open another terminal to perform sar to see CPU degradation
- When the VM is running the script, you will not be able to perform any additional actions on the VM

Submit a screenshot of the CPU’s degraded performance
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-7.png)
## Part 5. Install cockpit

- `sudo apt update`
- `sudo apt install cockpit`
- `sudo systemctl enable --now cockpit.socket`

- On another computer on the same network (192.168.10.0/24 in my example), open a web browser and go to https://<VM IP>:9090
Submit a screenshot with the cockpit login screen.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-8.png)

## Part 6. Restrict access to SSH

Modify your server’s SSH configuration to allow only the RemoteUsers group to use the SSH services.
Add Bob to the RemoteUsers group. 
1. Create the "RemoteUsers" group:
- `sudo groupadd RemoteUsers`
2. Add bob to the "RemoteUsers" group:
- `sudo usermod -aG RemoteUsers bob`
3. Edit the SSH configuration file:
- `sudo nano /etc/ssh/sshd_config`
4. Added a `AllowGroups` line and added "RemoteUsers" to it
- `AllowGroups RemoteUsers`
5. Restart the SSH service:
- `sudo systemctl restart sshd`

Submit a screenshot of Bob and Alice's attempt to SSH to the lst1 server.
- Bob successfully SSH to lst1  
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-9.png)
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab1-10.png)
- Alice is unsuccessful even with the correct password
![alt text](image.png)