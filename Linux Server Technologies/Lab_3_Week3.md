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

- Update and Upgrade the server software `sudo apt update -y && sudo apt upgrade -y`
- Install DHCP service `sudo apt install isc-dhcp-server`
- Verify DHCP service `systemctl status isc-dhcp-service`
- Status may be Active: failed because the isc-dhcp-service does not have valid configurations after being installed
- Stop the service to configure it `sudo systemctl stop isc-dhcp-server`
- Create a backup configuration of the original file before we do changes `sudo cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.bak`

- Configurations of dhcpd.conf
```
ddns-update-style none;
authoritative;
# A slightly different configuration for an internal subnet.
subnet 192.168.10.0 netmask 255.255.255.0 {
  range 192.168.10.10 192.168.10.127;
  option domain-name-servers 192.168.10.1, 8.8.8.8, 8.8.4.4;
  option domain-name "lst1.lan";
  option subnet-mask 255.255.255.0;
  option routers 192.168.10.1;
  option broadcast-address 192.168.10.255;
  default-lease-time 43200;
  max-lease-time 86400;
}
```
- Assign an interface for DHCP traffic
- Edit `sudo nano /etc/default/isc-dhcp-server`
- Add your network inferface in the file. Example `INTERFACESv4="ens33"`
- This restricts DHCP server to the specified interface

- Enable the DHCP service `sudo systemctl enable isc-dhcp-server`
- May have to restart the service it is still not running `sudo systemctl restart isc-dhcp-server`

- Set up on a second VM host (Client) to be configured for DHCP
- In another VM, lst2, I set netplan static.yaml to be dhcp4: true

- Verify DHCP leases on lst1 `cat /var/lib/dhcp/dhcpd.leases`
- Verify DHCP using syslog `cat /var/log/syslog`


Submit screenshots of:
- Your DHCP configuration on `lst1`.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-4.png)
- The DHCP leases file showing that the IP address was issued.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-5.png)
- The DHCP address on your client VM.
![alt text](/Linux%20Server%20Technologies/Lab_Images/lab3-6.png)