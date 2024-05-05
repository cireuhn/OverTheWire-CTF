## TASK #1

1. From another VM, use `ncat` to listen on port 4455.
2. Using `ncat` on `lst1`, call the other VM with the `-e /bin/bash` option.
3. Using `tshark` on `lst1`, in another shell, capture packets on port 4455 or use a filter. Use the pcapng format for the file.

Submit screenshots of:
- Your listening and calling sessions for `ncat`.
- Your `tshark` trace file of the first 10 packets.

## TASK #2

Transfer the trace file on `lst1` to Wireshark on another VM or host machine with Wireshark installed. Open the trace file. Click on the first packet and display the Transmission Control Protocol layer.

- Install WireShark on another VM/host machine
- Use WinSCP to transfer the file over to another VM/host machine

Submit a screenshot of the TCP layer detail in Wireshark.

![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-1.png)

## TASK #3

Enable SSH and Cockpit ports on `lst1` using UFW. You will have to enable UFW. Increase logging to high. Using `netcat` or `telnet`, try to access `lst1` TCP port 25.

- Enable UFW by performing `sudo ufw enable`
- The default policy is to deny all incoming traffic and allow all outbound traffic
- Allow SSH `sudo ufw allow 22`
- Allow Cockpit `sudo ufw allow 9090`
- Verify UFW rules `sudo ufw status numbered`

- Set UFW logging to high `sudo ufw logging high`
- Verify logging was set to high `sudo ufw status verbose`

- View UFW logs `cat /var/log/ufw.log | tail`

Submit screenshots of:
- The UFW log showing the packets attempting to use port 25.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-2.png)

- The current rules in verbose mode for UFW.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-3.png)

## TASK #4

Configure DHCP on `lst1` for the bottom half of the network block for your subnet. IP addresses below 128. Please account for your gateway and host network IP addresses (usually 1 and 2 for VMWare). Your `lst1` server should have been configured with a static address using .201. Use another VM, server, or desktop to receive a dynamic DHCP address.

Submit screenshots of:
- Your DHCP configuration on `lst1`.
- The DHCP leases file showing that the IP address was issued.
- The DHCP address on your client VM.