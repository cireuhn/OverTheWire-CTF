## TASK #1

1. From another VM, use `ncat` to listen on port 4455.
2. Using `ncat` on `lst1`, call the other VM with the `-e /bin/bash` option.
3. Using `tshark` on `lst1`, in another shell, capture packets on port 4455 or use a filter. Use the pcapng format for the file.

Submit screenshots of:
- Your listening and calling sessions for `ncat`.
- Your `tshark` trace file of the first 10 packets.

## TASK #2

Transfer the trace file on `lst1` to Wireshark on another VM or host machine with Wireshark installed. Open the trace file. Click on the first packet and display the Transmission Control Protocol layer.

Submit a screenshot of the TCP layer detail in Wireshark.

## TASK #3

Enable SSH and Cockpit ports on `lst1` using UFW. You will have to enable UFW. Increase logging to high. Using `netcat` or `telnet`, try to access `lst1` TCP port 25.

Submit screenshots of:
- The UFW log showing the packets attempting to use port 25.
- The current rules in verbose mode for UFW.

## TASK #4

Configure DHCP on `lst1` for the bottom half of the network block for your subnet. IP addresses below 128. Please account for your gateway and host network IP addresses (usually 1 and 2 for VMWare). Your `lst1` server should have been configured with a static address using .201. Use another VM, server, or desktop to receive a dynamic DHCP address.

Submit screenshots of:
- Your DHCP configuration on `lst1`.
- The DHCP leases file showing that the IP address was issued.
- The DHCP address on your client VM.