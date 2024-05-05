# Lab 1 

## Part 1. Change the VM’s IP address and hostname to lst1 

1. **Create a new file for netplan.**
    - Created a file called `static.yaml`.
    - Format for a Static IP address in netplan:
    ```yaml
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
    - Apply new file: `sudo netplan apply`  

    ![Netplan yaml file and IP address change](/Linux%20Server%20Technologies/Lab_Images/lab1-1.png)

2. **Change hostname of the device**
    - Verify with `hostnamectl`.
    - Set a new hostname: `sudo hostnamectl set-hostname lst1`.

    ![New hostname](/Linux%20Server%20Technologies/Lab_Images/lab1-2.png)

## Part 2. Install stress-ng

- Verify if it exists: `apt list | grep stress-ng`.
- Install: `apt install stress-ng`.

![stress-ng installation](/Linux%20Server%20Technologies/Lab_Images/lab1-3.png)

## Part 3. Create a bob and alice account. Create an adminjr group.

1. **Create user bob and alice**
    - Commands:
    ```bash
    sudo adduser bob
    sudo adduser alice
    sudo groupadd adminjr
    ```

    ![Failed attempt to change password](/Linux%20Server%20Technologies/Lab_Images/lab1-4.png)

2. **Configure the adminjr group to change passwords**
    - Edit the sudoers file: Add `%adminjr ALL=(ALL) /usr/bin/passwd` to the end of the file.

3. **Add bob to the adminjr group**
    - Command: `sudo usermod -aG adminjr bob`.
    - Verify with `groups bob`.

    ![Bob changing Alice's password](/Linux%20Server%20Technologies/Lab_Images/lab1-5.png)

## Part 4. Install SAR, execute the cpubusy script, and show CPU stress

1. **Install sysstat**
    - Verify if it exists: `apt list | grep sysstat`.
    - Install: `apt install sysstat`.


2. **Download cpubusy.py**
    - Download this file from the repository provided by the instructor.
    - Download and install WinSCP
    - Transfer the file from your local machine to the VM using WinSCP.
    - Change the File protocol to `SCP` in WinSCP settings.

    ![WinSCP Settings](/Linux%20Server%20Technologies/Lab_Images/lab1-6.png)

3. **Execute cpubusy script and show CPU stress**
    - Run the script: `python3 cpubusy.py`.
    - Monitor CPU performance using SAR: `sar -u 1 20`.

    ![CPU stress](/Linux%20Server%20Technologies/Lab_Images/lab1-7.png)

## Part 5. Install Cockpit

1. **Update the package list**
    - Command: `sudo apt update`.

2. **Install Cockpit**
    - Command: `sudo apt install cockpit`.

3. **Enable Cockpit**
    - Command: `sudo systemctl enable --now cockpit.socket`.

4. **Access Cockpit**
    - On another computer on the same network (192.168.10.0/24 in my example), open a web browser and go to `https://<VM IP>:9090`.

    ![Cockpit login screen](/Linux%20Server%20Technologies/Lab_Images/lab1-8.png)

## Part 6. Restrict access to SSH

**Objective:** Modify your server’s SSH configuration to allow only the RemoteUsers group to use the SSH services.

1. **Create the "RemoteUsers" group**
    - Command: `sudo groupadd RemoteUsers`.

2. **Add bob to the "RemoteUsers" group**
    - Command: `sudo usermod -aG RemoteUsers bob`.

3. **Modify SSH configuration**
    - Open the SSH configuration file: `sudo nano /etc/ssh/sshd_config`.
    - Add an `AllowGroups` line and include "RemoteUsers" in it: `AllowGroups RemoteUsers`.

4. **Restart the SSH service**
    - Command: `sudo systemctl restart ssh`.

5. **Test SSH access**
    - Bob should be able to SSH to lst1.
    - Alice should not be able to SSH to lst1, even with the correct password.

    ![Bob's successful SSH](/Linux%20Server%20Technologies/Lab_Images/lab1-10.png)  
    ![Alice's unsuccessful SSH](/Linux%20Server%20Technologies/Lab_Images/lab1-11.png)