# Nmap-Scanner

```
  ____   _____ _____  ______  
 /    \ /     \\__  \ \____ \ 
|   |  \  Y Y  \/ __ \|  |_> >
|___|  /__|_|  (____  /   __/ 
     \/      \/     \/|__|    
```

## Next steps:
- [x] Get the code running
- [x] Improve strings output
- [ ] Understand what is really going on
- [ ] Document on ReadMe to grasp the concept and utility
- [ ] Check if possible to add options
- [ ] Add search's time

## Types of scan:

### TCP SYN (Stealth) Scan (-sS)
SYN scan is the default and most popular scan option for good reasons. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It is also relatively unobtrusive and stealthy since it never completes TCP connections. SYN scan works against any compliant TCP stack rather than depending on idiosyncrasies of specific platforms as Nmap's FIN/NULL/Xmas, Maimon and idle scans do. It also allows clear, reliable differentiation between the open, closed, and filtered states. <br>
This technique is often referred to as half-open scanning, because you don't open a full TCP connection. You send a SYN packet, as if you are going to open a real connection and then wait for a response. A SYN/ACK indicates the port is listening (open), while a RST (reset) is indicative of a non-listener. If no response is received after several retransmissions, the port is marked as filtered. The port is also marked filtered if an ICMP unreachable error (type 3, code 0, 1, 2, 3, 9, 10, or 13) is received. The port is also considered open if a SYN packet (without the ACK flag) is received in response. This can be due to an extremely rare TCP feature known as a simultaneous open or split handshake connection (see https://nmap.org/misc/split-handshake.pdf).

### UDP scan (-sU)
While most popular services on the Internet run over the TCP protocol, UDP services are widely deployed. DNS, SNMP, and DHCP (registered ports 53, 161/162, and 67/68) are three of the most common. Because UDP scanning is generally slower and more difficult than TCP, some security auditors ignore these ports. This is a mistake, as exploitable UDP services are quite common and attackers certainly don't ignore the whole protocol. Fortunately, Nmap can help inventory UDP ports. It can be combined with a TCP scan type such as SYN scan to check both protocols during the same run.
UDP scan works by sending a UDP packet to every targeted port. For most ports, this packet will be empty (no payload), but for a few of the more common ports a protocol-specific payload will be sent. Based on the response, or lack thereof, the port is assigned to one of four states.

How Nmap interprets responses to a UDP probe :

| Probe Response	       | Assigned State |
| ----------- | ----------- |
| Any UDP response from target port (unusual) | open       |
| No response received (even after retransmissions)  | open / filtered        |
| ICMP port unreachable error (type 3, code 3)  | closed   |
| Other ICMP unreachable errors (type 3, code 1, 2, 9, 10, or 13) | filtered |
