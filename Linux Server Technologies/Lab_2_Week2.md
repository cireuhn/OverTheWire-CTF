## Task 1
Using either your host computer or a VM, configure secure SSH using a certificate generated to authenticate to lst1. Disable password authentication for SSH on lst1.

1. Generate a key for the server
- `ssh-keygen -t ed25519 -C "lst2"
- The -C "lst2" adds a lst2 comment to the key

2. Verify the public and private keys were created

- `ls -l .ssh`

![alt text](/Linux%20Server%20Technologies/Lab_Images/lab2-1.png)
3. Copy the key to the target system

- `ssh-copy-id <user>@<Target VM IP>`
- In my case it will be `ssh-copy-id dev@192.168.10.201`
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab2-2.png)

Turn in a screenshot of your `~/.ssh/authorized_keys` file on lst1 showing that the public key was added and a screenshot of your modified `sshd` configuration showing password authentication is disabled.

- Here is a screencap of the pub key of lst2 added to lst1
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab2-3.png)

Disable Password authentication and enable Certificate-based Authentication
Edit /etc/ssh/sshd_config
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab2-4.png)

## Task 2
Allow a banner in `/etc/ssh/sshd_config`.
"Banner file-to-store-message"
Create a banner file in `/etc` and include:
"RESTRICTED SYSTEM AUTHORIZED USERS ONLY" and your name.

- Create a banner file in `/etc`
- I created a file called `/etc/issue.net`
- `nano /etc/issue.net` and add in "RESTRICTED SYSTEM AUTHORIZED USERS ONLY" and your name.
- Go to `/etc/ssh/sshd_config` and place the banner default path
- `Banner /etc/issue.net`

![Banner path in /etc/ssh/sshd_config](/Linux%20Server%20Technologies/Lab_Images/lab2-5.png)
After logging in, submit a screenshot of the warning.

Successful login to lst1 using certificate-based authentication
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab2-6.png)

## Task 3
Install the `at` service. Your output should include the service is active and running.

Submit a screenshot using `systemctl` with the status of the `atd` service.

## Task 4
Submit a screenshot using `systemctl status` of the `atd` server before stopping the `atd` service and another after stopping the service.

## Task 5
Mask the `atd` service. Submit a screenshot proving that the `atd` service is masked.

## Task 6
Install Apache. Change the Apache unit and use the override feature with "Linux is Awesome" and your name.

Submit a screenshot of the service with your custom description.

## Task 7
Use `journalctl` to display messages from `sysstat.service` and output them to a JSON file.

Submit a screenshot of your JSON file (use `head`).