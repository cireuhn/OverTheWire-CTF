# Instructions

## Case Scenario 
In the User Management challenge lab, you were tasked with creating users and groups. Using the commands one at a time from the command line can be a tedious process and could lead to potential errors in syntax. It is your duty, as an administrator, to make the process as seamless and efficient as possible.

## Objectives
Create a bash script to perform user management tasks as outlined below:

Create a new group. Each group must have a unique name. The script must check to ensure that no duplicate group names exist on the system. If a duplicate is found, an error needs to be reported, and the administrator must try another group name.
Create a new user. Each user must have a unique name. The script must check to ensure that no duplicate usernames exist on the system. If a duplicate is found, an error needs to be reported and the administrator must try another username. The user will have a Bash login shell and belong to the group that was created in the previous step.
Create a password for each user that is created.
Ensure that the new user created is a member of the new group created.
Create a directory at the root / of the file system with same name as the user created.
Set the ownership of the directory to the user and group created.
Set the permissions of the directory to full control for the owner and full control for the group created.
Set the permissions to ensure that only the owner of a file can delete it from the directory.
Ensure that the script is executable.
This script should be designed to accept any username and any group name. DO NOT hardcode commands to create specific usernames and group names.
Hints
Logical order is important.
There is a special wildcard that can be used to determine if the previous command is successful or not. This will be useful for this script.

Deliverables

- Execute the script for the instructor. Create a new unique user and new unique group.
- Execute the script for the instructor. Show the error when a duplicate user or duplicate group are created.

# Solution

```
#!/bin/bash

# Function to check if a group exists
group_exists() {
  getent group "$1" > /dev/null 2>&1
}

# Function to check if a user exists
user_exists() {
  getent passwd "$1" > /dev/null 2>&1
}

# Get group name from user input
while true; do
  read -p "Enter a new group name: " group_name
  if ! group_exists "$group_name"; then
    break
  else
    echo "Error: Group '$group_name' already exists. Please choose another name."
  fi
done

# Create the group
groupadd "$group_name"

# Get username from user input
while true; do
  read -p "Enter a new username: " username
  if ! user_exists "$username"; then
    break
  else
    echo "Error: User '$username' already exists. Please choose another name."
  fi
done

# Create the user with bash shell and assign to the group
useradd -m -d "/$username" -s /bin/bash -G "$group_name" "$username"

# Set a password for the user
passwd "$username"

# Set ownership and permissions for the user directory
chown "$username:$group_name" "/$username"
chmod 770 "/$username"

# Set sticky bit to prevent file deletion by others
chmod +t "/$username"

echo "User '$username' and group '$group_name' created successfully."
```

