## Task 1
Using either your host computer or a VM, configure secure SSH using a certificate generated to authenticate to lst1. Disable password authentication for SSH on lst1.

Turn in a screenshot of your `~/.ssh/authorized_keys` file on lst1 showing that the public key was added and a screenshot of your modified `sshd` configuration showing password authentication is disabled.

## Task 2
Allow a banner in `/etc/ssh/sshd_config`.
"Banner file-to-store-message"
Create a banner file in `/etc` and include:
"RESTRICTED SYSTEM AUTHORIZED USERS ONLY" and your name.

After logging in, submit a screenshot of the warning.

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