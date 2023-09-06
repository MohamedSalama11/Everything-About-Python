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
# the first 3 parts (octets) represents the network portion while the last part represents the host (desktop computer, server, labtop, mobile, tablet)
# 255 in the subnet mask represents the network portion
# 0 in the subnet make represents the host portion
# 127.0.0.1 represents the local host or the home network, and it is also called the loopback address.
# APIPA Adresses always will be in range from 169.254.0.0 To 169.254.255.255


############# IPv6 #############
# The loopback address for ipv6 is ::1


############# Commands #############
# 1- tracert   => is a command that allows you to check all the routers you go through from your system to any other system
    ## tracert (Windows), traceroute (Linux)
    ## usage  => tracert destination  => tracert www.google.com

# 2- pathping  => similary to tracert but with more information and more faster.
    ## usage => pathping destination  => pathping www.google.com

# 3- ping      => used to get the status of a specific destination, helps us in network troubleshouting
    ## usage => ping www.google.com

# 4- ipconfig
    ## ipconfig (Windows) ifconfig (Linux)
    ## usage => gives you information about your network like ipv4, ipv6, DHCP server, etc...

# 5- route print == netstat -r
    ## usage  => to print the routing table in windows.

# 6- tcpdump => works in linux, and it is a alternative capture tool like wireshark
    ## usage  => it's a network analyzer 

# 7- netstat => lists all the open ports and connections on your computer, and to show you what is the type of network connections esablished between your computer and any other computer
    ## usage => netstat -n option will give you the ip address of the foreign address
            # netstat -b option shows the executable for every connection
            # netstat -o option shows you the executable and process id for every connection
            # netstat -a option shows you all the active ports
            # netstat -r option shows you the local routing table