# The whole purpose of networking is to send data from one machine to another.
# Switches => A device that connects network devices together, Is just a next generation of hubs that combine hubs with another device called a bridge, and they can use logic
    # to learn which physical ports are attached to which devices based on their mac addresses and in this way they can send data to specific devices in the network.
    # also known as a multiport bridge, it's a layer 2 device that connects multiple network segments together
# WAP ( wireless access point ) => Are devices that allows wireless devices to connect into a wired network, acts like a wireless hub.
# WAN ( wide area network ) Links => It simply connects an internal netwrok to an external one.
# IEEE 802.3 refers to Ethernet, IEEE 802.11 refer to Wi-Fi.
# OSI model is also called OSI Stack and reference model.
# TCP/IP Model also called TCP/IP Stack or DoD Model named for who created it.
# PDU is just a single unit of information transmitted in a computer network.
# TCP Header is a 20 bytes of data while UDP Header is a 8 bytes of data.
# Bandwidth => measure how many bits the network can transmit per second.
# Bridge => analyzes source MAC address and makes intelligent forwarding decisions based on the destination MAC in the frames, acts in layer 2.
# Router => acts in layer 3 because it's depends on ip addresses.
# multilayer switch or layer 3 switch => is a combination from switch and router and acts in layer 3 of the OSI Model.
# User Authentication ( 802.1x ) => requires users to authenticate themselves before gaining access to the network.
# SSH ( Secure Shell ) => remote administration program that allows connection to the switch over a network.
# FTP protocol is not encrypted so all passwords and data are sent in the clear.
# IIS and Apache is a web servers.
# DHCP is a network management protocol that operates over ports 67, 68 using UDP connection.
# DNS operates over port 53 using TCP connection.
# NTP operates over port 123 using UDP connection.
# www.facebook.com www is the subdomain, facebook is the domain name, .com is the top level domain.
# forward DNS lookup determines the IP address based on a given hostname.
# reverse DNS lookup determines the hostname based on the given IP and it's the opposite of A record in the DNS.
# Nameserver is a type of DNS server that stores all the DNS recrods for a given domain
# DNS resolver or DNS Cache makes a local copy of every DNS entry if resolves as you connect to websites
# the three methods we use in wireless security
#   1- WEB ( Wired Equivalent Privacy ) :- This is the original 802.11 wireless security standard which is an insecure security protocol,
#      and it works using pre-shared key to every host and it's 40 bit key, and you can easily crack the key and hack the wifi using aircrack-ng software which is used for wireless pentesting
#      uses a 24-bit initialization vector ( IV ) send in a clear text
#   2- WPA ( Wi-Fi Protected Access ) :- Replaced WEB and follows the temporal key integrity protcol ( TKIP ), uses 48-bit IV
#      and added another feature called Rivest Cipher 4 ( RC4 ) for encryption
#      also added the Message Integriy Check ( MIC ) to confirm data was not modified in transmit
#   3- WPA2 ( Wi-Fi Protected Access 2 ) :- Created as part of IEEE 802.11i standard and requires stronger encryption and integrity checking through CCMP
#      it replaced the RC4 with AES ( Advanced Encryption Standard ) to provide security by using a 128-bit key or higher.
#      the easiest way to crack WPA2 by using password attacks and this is means guessing the password using burte force attack or a dictionary attack.
#      there's two modes for WPA2 one is personal mode with pre-shared key where everyone has the same password and is used in home or small office,
#      two enterprise mode with centralized authentication, where every user gets a single username and password unique to them 

# ACL stands for Access Control List, it is a set of rules that is usually used to filter network traffic.
# SSID stands for Service Set ID and it's the name of your wifi and if you set to disable in the router configuration this will hide your wifi.
# enable wireless isolation this is a seeting in the router configurations always enable it to keep the channels and frequencies isolated from each other to act more like a switch not a hub.
# CIA Triad stands for 
#   Confidenttiality :- keeps data private and safe using encryption and authentication to access resources.
#   Integrity :- ensuers that the data was not modified in transit and verifies it came from it's original source and it helps to prevent attacks like ip spoofing, ARP spoofing, MAC spoofing
#   Availability :- measures data accessibility and is increased by designing redundant networks.


# there's two types of encryption
# 1- symmetric encryption :- sender and receiver use the same key to encrypt and decrypt a message.
# 2- Asymmetric Encryption :- sender and receiver use the different keys to encrypt and decrypt a message.

# Technical Vulnerabiliteis :- System-specific conditions that create security weakness like CVE or Zero-day vulnerability.
#   CVE stands for Common Vulnerabilities and Exposure :- it's a list of disclosed computer security weakness, basically it's an official list of all the known technical vulnerabilities
#   for each and every piece of software that's publicly avaliable.
#   Zero-Day :- is a brand new vulnerability that's no one has discovered or reported it yet and only the professional cyber security engineer's know it, when they reported it it becomes
#   no more a Zero-Day vulnerability and becomes a CVE

# when you take advantage of a vulnerability this is called an exploit, exploit is a piece of software code that takes advantage of a security vulnerability within a system or a network.

# Threat Assessment :- focused on identification of the different threats that may wish to attack or cause harm to your system or network
#   a common tool to do this called MITRE ATT&CKL and it's a globally accessible knowledge base of adversary tactics and techniques based on real world observations from the field
#   and it lets an administrator or analyst walk through the typical methodologies that are used by different threats or hackers to harm your network and help you to identify the 
#   vulnerability and protect your self.

# vulnerability assessment :- focused on identifying and prioritizing the risks and vuljnerabiliteis in a system or network using a vulnerability scanner like Nessus, QulaysGuard, OpenVAS

# penetration test :- evaluates teh security of an IT infrastructure by safely trying to exploit vulnerabiliteis within the systems or network.

# Brute force attack :- tries every possible combination until they figure out the password, if the password short and weak it's just a matter of time until the attacker gets your password.
# hubrid attack is a combination of dictionary and burteforce attacks.
# Authentication :- is the process of determining whether someone or something is who or what it claims itself to be.
# AD stands for Active Directory :- organizes and manages everything on the network including clients servers devices users.
# DoS attack stands for Denial of servcie attack :- occurs when one machine continually floods a victim with requests for services, to make a DoS attack the attacker may use 2 ways,
#   1- TCP SYN flood :- occurs when an attacker initiates multiple TCP sessions, but never completes them.
#   2- ICMP flood ( Smurf Attack ):- occurs when an attacker sends a ping to a subnet broadcast address with the source IP spoofed to be that of the victim server, to handle this attack
#      you shoud block ping requests to your server.

# DDoS attack stands for Distributed Denial of Service Attack :- occurs when an attacker uses multiple computers to ask for access to the same server at the same time.
# MITM attack stands for man in the middle attack or On-Path attack :- occurs when an attacker puts themselves between the victim and the intended destination, in this attack the attacker
#   have the ability to monitor whatever you're sending or manipulate the data you're sending to the server.

# session Hijacking Attack :- occurs when an attacker guesses the session ID that is in used between a client and a server and takes over authenticated sessoin.

# DNS poisoning Attack :- occurs when an attacker manipulates known vulnerabilities within the DNS to reroute traffic from one site to a fake version of that site, to overcome this attack
#   a new version of DNS servers invented called DNS SEC and it uses encrypted digital signatures when passing DNS information between servers to help protect it from poisoning.

# Rogue DHCP server :- A DHCP server on a netwrok which is not under the administrative contorl of the network administrators, it happens when the attacker connect his DHCP server on your
#    network and have control on it and handle everything like ip addresses, subnet masks, gateways, DNS servers.

# IP spoofing attack :- Modifying the source address of an IP packet to hide the identity of the sender or impersonate another client.
# MAC spoofing attack :- changing the MAC address to pretend the use of a different network interface card or device, to change the mac address in mac system you can use the command
#   sudo ifconfig en0 ether <MAC address>.

# MALWARE :- is a shorthand for Malicoius Software, designed for damage a computer system and possibly damage it without the user's knowledge.
# RAT stands for Remote Access Trojan :- provides the attacker with remote control of a victim machine.
# spyWare :- gathers informatin about you without your consent
# key looger :- captures any strokes made on the victim machine.
# rootkit:- designed to gain administrative control over a computer system or network device without being detected.

# Phishing attack :- is a one type of social engineering attacks, it's a method of sending an email in  an attempt to get a user to click a link, those types of attacks depends of the user,
#   because when you sending a link to a user he will probably open it without thinking so it's a great way for us as attackers.


############# ShortCuts #############
# 01- IPX ( Internetwork Packet Exchange but it's killed when IP appeared ).
# 02- ASCII ( American Standard for Computer Information Interchange ).
# 03- WAP ( wireless access point ).
# 04- WAN ( wide area network ).
# 05- MAC ( Media Access Control ).
# 06- IP ( Internet Protocol ).
# 07- TLS ( Transport Layer Security ).
# 08- TELNET ().
# 09- WI-FI ().
# 10- SSH ( Secure Shell ).
# 11- OSI ( Open System Interconnection ).
# 12- ISO ( International Organisation for Standarization ).
# 13- DNS ( Domain Name Service => Domain ).
# 14- FTP ( File Transfer Protocol ).
# 15- ISP ( Internet Service Provier ).
# 16- PDU ( Protocol Data Unit ).
# 17- TCP ( Transimission Control Protocol ).
# 18- UDP ( User Datagram Protocol ).
# 19- TCP/IP ( Transimition Control Protocol/Internet Protocol ).
# 20- SMTP ( Simple Mail Transfer Protocol ).
# 21- DHCP ( Dynamic Host Control Protocol ).
# 22- TFTP ( Trivial File Transfer Protocol ).
# 23- POP3 ( Post Office Protocol version 3 ).
# 24- NTP ( Network Time Protocol ).
# 25- NetBIOS ( Network Basic Input/Output System ).
# 26- IMAP ( Internet Mail Application Protocol ).
# 27- SNMP ( Simple Netwrok Management Protocol ).
# 28- LDAP ( Lightweight Directory Access Protocol ).
# 29- SSL ( Secure Socket Layer ).
# 30- SMB ( Server Message Block Protocol ).
# 31- Syslog ( System Logging Protocol ).
# 32- RDB ( Remote Desktop Protocol ).
# 33- SIP ( Session Initiation Protocol ).
# 34- Nmap ( Network Mapper ).
# 35- ICMP ( Internet Control Message Protocol ).
# 36- GRE ( Generic Routing Encapsulation ).
# 37- STP ( Spanning Tree Protocol ).
# 38- CIDR ( Classless Inter-domain Rounting Notation ).
# 39- FDDI Ring ( Fiber Distributed Data Interface ).
# 40- IDS ( Intrusion Detection System )
# 41- IPS ( Intrusion Prevention System )
# 42- VoIP phone ( Voice Over Internet Protocol )
# 43- APIPA ( Automatic Private Internet Protocol Address )
# 44- WINS ( Windows Internet Name Service )
# 45- BOOTP ( Bootstrap Protocol )
# 46- RIP ( Routing Information Protocol )
# 47- OSPF ( Open Shortest Path First )
# 48- EIGRP ( Enhanced Interior Gateway Routing Protocol )
# 49- BGP ( Border Gateway Protocol )
# 50- NAT ( Network Address Translation )
# 51- PAT ( Port Address Translation )
# 52- IIS ( Internet Information Service )
# 53- FQDN ( Fully-Qualified Domain Name )
# 54- URL ( Uniform Resource Locator )
# 55- DSL ( Digital Subscriber Line )


############# MAC Adresses #############
# Physical addressing system of a device which operates on a logical topology.
# It will be like 6 pairs of characters separated by : and each pair consists from two characters.
# Uses a 48-bit address assigned to a network interface card (NIC).
# It consists of 12 characters in hexadecimal.
# Each number or character is considered as 4 bits.
# The first 6 chars is called Vendor Code and it's represents who made this NIC.
# The next 6 chars is called unique value and it's repersents the exact machine that belongs to.
# Example => D2:51:F1:3A:34:65
# FF:FF:FF:FF:FF:FF is the broadcast mac address at layer two.


############# IPv4 #############
# Writeen in a series of four decimal numbers separated by dot which known as Dotted-Decimal Notation
# each part of the four decimal numbers knows as Octet 
# each part has 8 bits so the values can go from 0 to 255
# total address is 32 bits ( 4 * 8 ) 
# ipv4 address is actually in binary digits but it is written as decimal to make it easirer for us to read
# 255 represents in binary as 11111111 and 0 in binary is 00000000
# the first 3 parts (octets) represents the network portion while the last part represents the host (desktop computer, server, labtop, mobile, tablet) in class C address.
# subnet mask is useless without a ip address and ip address is useless without subnet mask.
# 255 or 1 in the subnet mask represents the network portion
# 0 in the subnet make represents the host portion
# 127.0.0.1 represents the local host or the home network, and it is also called the loopback address.
# APIPA Adresses always will be in range from 169.254.0.0 To 169.254.255.255
# 192.168.1.1/24  /24 this tells you how many bits are set to one in the subnet mask, class C, 255.255.255.0 or 11111111.11111111.11111111.00000000
# 224.0.0.0 to 239.255.255.255 is the multicast address
# 255.255.255.255 is the broadcast address


############# IPv6 #############
# 128 bit address expressed in hexadecimal separated by colons
# The loopback address for ipv6 is ::1
# FE80 is a link local address for IPv6 similar to APIPA in IPv4
# FC00 or FD00 is a unique local addres and it's the internal private IP addresses
# There's no broadcast address in IPv6
# FF00::/8 is the multicast address 


############# Commands #############
# 1- tracert   => is a command that allows you to check all the routers you go through from your system to any other system, displays the path between device and it's destinatio, showing
#                 the source and destination ip address for each hop along the way.
    ## tracert (Windows), traceroute (Linux)
    ## usage  => tracert destination  => tracert www.google.com
# Hop is any router or firewall that is in the path of the transmission from client to destination.

# 2- pathping  => similary to tracert but with more information and more faster.
    ## usage => pathping destination  => pathping www.google.com

# 3- ping      => used to get the status of a specific destination, helps us in network troubleshouting
    ## usage => ping www.google.com
#               ping -n option allows you to calculate the number of ping ( ping -n 10 google.com )
#               ping -t option allows you to ping forever, you can use it to test if the WAN connection is running or not
#               ping -c number option works in linux and it will specify the number of ping ( ping -c 10 google.com )
# in windows ping will ping the target 4 times as default and if you want to ping it forever use ping -t, while in linux by default it will ping the target for ever until you stop it.


# 4- ipconfig  => displays all of the current TCP/IP network configuration values and refreshes DHCP and DNS settings for a windows client or server.
    ## ipconfig (Windows) ifconfig (Linux)
    ## usage => gives you information about your network like ipv4, ipv6, DHCP server, etc...
#               ipconfig /release :- to remove the ipv4 address and the subnet mask and the default gateway
#               ipconfig /renew   :- to renew the ipv4, subnetmask, default gatway
#               ipconfig /all     :- will give you more configurations like mac address, DNS server.

# 5- route print == netstat -r
    ## usage  => to print the routing table in windows.

# 6- tcpdump => works in linux, and it is a alternative capture tool like wireshark
    ## usage  => it's a network analyzer 

# 7- netstat => lists all the open ports and connections on your computer, and to show you what is the type of network connections esablished between your computer and any other computer
    ## usage => netstat -n option will give you the ip address of the foreign address.
#               netstat -b option shows the executable for every connection.
#               netstat -o option shows you the executable and process id for every connection.
#               netstat -a option shows you all the active ports.
#               netstat -r option shows you the local routing table.

# 8- ip => Assigns an address to a network interface or configures netwrok interface prameters on a Unix, Linux, or OS X operating systems, replaced the ifconfig.

# 9- nslookup (name server lookup) :- used to query the DNS to provide the mapping between domain names and IP addresses or other DNS records, it is used to know the ip address of a domain name.

# 10- hostname => used to display the hostname portion of the full computer name for a given system.

# 11- arp (address resolution protocol) => used to display and modify entries in the ARP cache on a system.
    ## usage => arp -a option to show you the ARP cache