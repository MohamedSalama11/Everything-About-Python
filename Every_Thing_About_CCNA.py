####################### CISCO OS Commands #######################
# NOTE:-
# 01- >                                                           => means that you are in user Execution mode also called user mode this mode can not change the configuration.
# 02- #                                                           => means that you are in privileges Execution mode this mode can not change the configuration.
# 03- (config)#                                                   => means that you are in global configuration mode.
# 04- <cr>                                                        => means that there's no other options.
# 05- 7                                                           => number seven indicates the type of ecnryption used to encrypt the password, means it's using cisco proprietary encryption alghorithm.
# 06- 5                                                           => number five indicates MD5 Encryption.
# 07- (config-if)#                                                => means that you are in the interface configuration mode.
# 08- (config-if-range)                                           => means that you are in the range of interfaces
# 09- (config-line)                                               => means that you are in the line configuration mode, used to configure console, SSH, Telnet, AUX access.
# 10- VTY lines                                                   => enable remote access using SSH, Telnet to the device, many cisco switches support up to 16 VTY lines ( from 0 to 15 ).
# 11- CTRL + A                                                    => to go to the beggining of the line in the CLI.


# 01- enable                                                      => to enter the privileges exeuction mode, en is the shortcut, disable to exit the privileged EXEC mode.
# 02- ?                                                           => to view the commands available in the mode you are currently at.
# 03- e?                                                          => will show the commands enable that starting with letter e.
# 04- configure terminal                                          => to enter the global configuration mode, conf t is the shortcut.
# 05- line                                                        => to enter the line configuration mode followed by the management line type, example => line console 0
# 06- line console 0                                              => to enter the line console configuration mode.
# 07- password your_password                                      => to create a password for the user EXEC mode.
# 08- login                                                       => to enable the password.
# 09- line vty 0 15                                               => is used to configure the Virtual Terminal (VTY) lines for remote access to the device, such as through Telnet or SSH.
# 10- banner motd #the message you want#                          => to display the message you want while accessing the device, motd stands for message of the day.
# 11- enable password your_password                               => to create password for the global configuration mode.
# 12- exit                                                        => to return to the back mode, will log out the device when you are in the privileges exec mode.
# 13- show running-config                                         => to view the running configuration file on the privilege exec mode.
# 14- show startup-config                                         => to view the startup configuration file on the privilege exec mode, which will be loaded if the device restarted.
# 15- write                                                       => to save the running configuration to make it the startup configuration, only from the privilege execution mode.
# 16- write memory                                                => same as write.
# 17- copy running-config startup-config                          => to copy the running-config file to the startup-config file, same as write and write memory.
# 18- erase startup-config                                        => to delete all the configurations from the startup-config file, use reload command after using it.
# 19- service password-encryption                                 => will encrypt all passwords in a set of numbers and letters so they can not easily hacked, not secure enough it can be cracked easily.
# 20- enable secret your_password                                 => more secured method to create passwords with more tough encryption alghorithm.
# 21- do                                                          => to run commands works in the privilege exec mode while you are in the global configuration mode, example => do show running-config.
# 22- run                                                         => executes a privileged exec level command from global configuration mode, example => run privileged-exec-level-command.
# 23- no                                                          => used to remove a command which you previously configured.
# 24- hostname name                                               => to change the hostname to the name you want.
# 25- reload                                                      => to reload the OS of the device.
# 26- show arp                                                    => to show the arp table in the privilege exec mode.
# 27- show mac address-table                                      => to show the mac address table on a switch.
# 28- clear mac address-table dynamic                             => to remove all the dynamic MAC addresess.
# 29- clear mac address-table dynmaic address the_mac_address     => to remove a specific MAC address.
# 30- clear mac address-table dynamic interface the_interface     => to remove all MAC address table entries for a specific interface.
# 31- show ip interface brief                                     => to confirm the status of each interface on the device as well as their ip addressess.
# 32- interface name_of_interface                                 => to configure the interface on the device, example => interface gigabitethernet 0/0 or in g0/0, shortcut is in.
# 33- ip address the_assigned_ip subnetmask                       => to assign ip address to specific interface, example ip address 10.255.255.254 255.0.0.0.
# 34- no shutdown                                                 => to enable the interface we currently at, we write it because cisco router interfaces have the shutdown command by default.
# 35- show interfaces                                             => display alot of inforamtion about the interfaces on the device, also the errors.
# 36- show interface name_of_interface                            => display alot of information only about the specified interface, example show interface g0/0.
# 37- show interfaces description                                 => give you a status of the interfaces.
# 38- description description_you_want                            => to configure an interface description
# 39- show inerfaces status                                       => display information on switch interfaces.
# 40- speed speed_you_want                                        => to specify the speed you want on a specific interface.
# 41- duplex auto/full/half                                       => to make the interface send and receive data in the same time.
# 42- interface range f0/5 - 12                                   => this is an interfaces range from interafce f0/5 to f0/12
# 43- interface range f0/5 - 6, f0/9 -12                          => this is an interface range from interface 5 to 6 and from 9 to 12, means that interface 7,8 not in the range.
# 44- shutdown                                                    => to shutdown the interfaces.
# 45- show clock                                                  => to show the clock of the Device OS.
# 46- clock set hh:mm:ss day month                                => to set clock and date, example => clock set 13:5:20 9 august 2023.
# 47- clock timezone zone                                         => to set the time and the zone, example => clock timezone cairo 2.
# 48- show ip route                                               => to show the router routing table.
# 49- ip route destination_network_ip_address net_mask next_hop   => to configure the static route for the router.
# 50- ip route destination_network_ip_address net_mask exit_int   => to configure the static route for the router, exit_interface option to specify which interface of the router should send the packet out of.
# 51- ip route dest_net_ip_add net_mask exit_interface next_hop   => to configure the static route for the router, with both exit_interface and next_hop options.
# 52- ip route 0.0.0.0 0.0.0.0 next_hop                           => to configure the default route ( the gateway route )
# 53- show running-config | include ip route                      => this command will work the same as piping in linux ( will take the output of the first command and put it as an input to the second command )
# 54- security password min-length specified_length               => to set a minimum acceptable password length, example => security password min-length 8.
# 55- login block-for attempts within                             => to stop brute force attacks or dictionary attacks, example => login block-for 120 attempts 3 within 60.
# 56- exec-timeout number_of_session time_specified               => to set the time you want for these sessions.
# 57- dir nvram:                                                  => verify the location of the saved configuration file, dir for directory.
# 58- dir flash:                                                  => verify the location of the OS device.
# 59- ip default-gateway gateway_address                          => to assign manually the default gateway.
# 60- transport input telnet                                      => to enable the telnet connection.
# 61- show vlan brief                                             => displays the vlans that exist on the switch and which interfaces are in each vlan, vlan 1 is the vlan that all interfaces are assigned to by default.
# 62- switchport mode access                                      => to set the interface as an access port.
# 63- switchport access vlan number_of_vlan                       => this is the command that actually assigns the vlan to the port, if the vlan does not exist it will create it automatically.
# 64- vlan number_of_vlan                                         => to create a vlan manually, if the vlan exists it will enter the vlan.
# 65- name vlan_name                                              => to create name for the vlan.
# 66- switchport trunk encapsulation dot1q                        => on switches that supports .1Q and ISL you must configure the encapsulation as .1Q or ISL (depreecated)
# 67- switchport mode trunk                                       => to configure the interface as a trunk.
# 68- show interfaces trunk                                       => to see the status of the turnk interfaces.
# 68- switchport trunk allowed vlan word                          => to configure the vlans allowed on a trunk port, example => swithcport trunk allowed vlan 10,30.
# 70- switchport trunk allowed vlan add 20                        => to configure the vlans allowed on a trunk port, will add the vlan 20 to the vlans allowed on the trunk port.
# 71- switchport trunk allowed vlan remove 20                     => to remove a specific vlan from the trunk port, will remove vlan 20.
# 72- switchport trunk allowed vlan all                           => will allow all the vlans on a trunk port, this is the same as the default state.
# 73- switchport trunk allowed vlan except 1-5,10                 => this allows all vlans on a trunk port except the vlans you specified.
# 74- switchport trunk allowed vlan none                          => this will not allow any vlans on the trunk, this command allows no traffic on the trunk port.
# 75- switchport trunk native vlan 1001                           => to set the native vlan to the number of vlan you want, here we set the vlan to 1001, for security purposes you should set the native vlan to unused vlan.
# 76- interface g0/0.10                                           => to enter a subinterface on a router on a stick (ROAS).
# 77- encapsulation dot1q vlan_id                                 => this tells the router to treat any arrived frames tagged with this specific vlan number as if they arrived on the subinterface.
# 78- encapsulation dot1q vlan_id native                          => this tells the router that this subinterface belongs to a native vlan.
# 79- default interface interface_id                              => to return the interface to it's default state.
# 80- ip routing                                                  => this command enables layer 3 routing on the multilayer switch.
# 81- no switchport                                               => this configured the interface as a routed port so you can assign an ip address to it, changes the interface port from layer 2 switch port to layer 3 routing port.
# 82- show spanning-tree                                          => to show information about the spanning tree protocol on the switch.
# 83- show spanning-tree detail                                   => like show spanning-tree protocol but with more details.
# 84- show spanning-tree summary                                  => this list each vlan and show how many interfaces are in STP state.
# 85- show spanning-tree vlan vlan_number                         => this list the status of STP in the vlan.
# 86- show etherchannel load-balance                              => to see the current load balancing method.
# 87- port-channel load-balance method                            => to change the load balance method.
# 88- channel-protocol lacp                                       => to enable the lacp protocol for etherchannel
# 89- channel-group 1 mode active                                 => to enable the LACP EtherChannel protocol.
# 90- interface port-channel 1                                    => to enter the group interface of etherchannel, shortcut interface po1.
# 91- show etherchannel summary                                   => to show a summary of the etherchannel interfaces.
# 92- show etherchannel port-channel                              => to show information about the etherchannel and the protocol being used, number of ports in the etherchannel gorup.
# 93- no switchport                                               => to make the interfaces act as layer three routed interfaces.
# 94- ip routing                                                  => to enable the routing table on the multilayer switch.
# 95- standby 1 ip ip_address                                     => to configure the virtual ip address.
# 96- standby 1 priority 200                                      => to configure the priority for the active router, highest priority router will be the active router.
# 97- standby 1 preempt                                           => causes the router to take the role of active router even if another router already has the role of active.
# 98- show standby                                                => to show the settings of HSRP.
# 99- standby version 2                                           => to configure the router to use HSRP v2.
# 100- ip dhcp excluded-address first_address second_address      => to specify a range of addresses that won't be given to DHCP clients.
# 101- ip dhcp pool pool_name                                     => to create a DHCP pool, pool is subnet of addresses that can be assigned to DHCP clients.
# 102- network network_address /prefix length                     => to configure the range of addresses to be assigned to the clients, ex => network 192.168.1.0 /24.
# 103- dns-server 8.8.8.8                                         => specify the DNS server the clients should be used.
# 104- default-router ip_address                                  => specify the default gateway
# 105- lease days hours minutes or lease infinite                 => to specify the lease time ( when to expired ).
# 106- show ip dhcp binding                                       => shows all of the dhcp clients that currently assigned.
# 107- ip helper-address ip_address_of_DHCP_server                => to configure the router as a dhcp relay agent, make sure the agent router has a route to the dhcp server.
# 108- ip address dhcp                                            => to tell the router to use the dhcp server to learn ip addresses for the router interfaces.
# 109- switchport port-security                                   => to enable the port security on the interface, interface must be in access or trunk mode.
# 110- switchport port-security mac-address mac_address           => to manually configure the allowed mac address on the interface.
# 111- switchport port-security violation restrict                => to enable the restrict mode.
# 113- switchport port-security violation protect                 => to enable the protect mode.
# 114- switchport port-security aging time minutes                => to enable the aging time for an secure mac address.
# 115- show port-security                                         => display which interfaces have port security enabled, the mac and current number of secure addresses on those interfaces.
# 116- show port-security interface interface_id                  => to show the default settings of the port security.
# 117- show interface interface_id switchport                     => to show the administrative mode and to see if the switchport is enabled on ther interface.
# 118- switchort port-security mac-adddress sticky                => basically a way of configuring static secure mac addresses without actually having to manually configure them.

# NOTE:-
# servers or clients also called endhosts or endpoints.
# MAC addresess may also called (BIA) => Burned_In Address this is because the address is burned into the device as it's made.
# There are MAC addresses known as locally unique MAC addresses which don't have to be globally unique.
# when we see a router like this CISCO ISR 2911 => CISCO is the company made this router, ISR is a line of CISCO routers, 2911 is a particural model in that line.
# Dynamic MAC addresess are removed from the MAC addresses table after 5 minutes if there's no traffic this is known as Aging.
# the minimum payload size for an rent frame is 46 bytes and if it's not 46 bytes padding will be added, padding is just a series of zeros.
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
# STP => is a layer 2 protocol
# ASwitch => is an access layer switch, a switch that end hosts connect to
# DSwitch => is a distribution layer switch, a switch that access layer switches connect to.
# some other names of etherchannel is port channel, LAG ( Link Aggregation Group ).


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
# Writeen in a series of four decimal numbers separated by dot which known as Dotted-Decimal Notation.
# each part of the four decimal numbers knows as Octet .
# each part has 8 bits so the values can go from 0 to 255.
# total address is 32 bits ( 4 * 8 ) .
# ipv4 address is actually in binary digits but it is written as decimal to make it easirer for us to read.
# 255 represents in binary as 11111111 and 0 in binary is 00000000.
# the first 3 parts (octets) represents the network portion while the last part represents the host (desktop computer, server, labtop, mobile, tablet) in class C address.
# subnet mask is useless without a ip address and ip address is useless without subnet mask.
# 255 or 1 in the subnet mask represents the network portion.
# 0 in the subnet mask represents the host portion.
# 127.0.0.1 represents the local host or the home network, and it is also called the loopback address.
# APIPA Adresses always will be in range from 169.254.0.0 To 169.254.255.255
# 192.168.1.1/24  /24 this tells you how many bits are set to one in the subnet mask, class C, 255.255.255.0 or 11111111.11111111.11111111.00000000
# 224.0.0.0 to 239.255.255.255 is the multicast address.
# 255.255.255.255 is the broadcast address.


############# IPv6 #############
# Each hexadecimal digit contains 4 bits.
# Contain 32 hexadecimal character.
# Contains eight groups, each group has 4 hexadecimal digits.
# Each group separated by column.
# 128 bit address expressed in hexadecimal separated by colons
# The loopback address for ipv6 is ::1
# FE80 is a link local address for IPv6 similar to APIPA in IPv4
# FC00 or FD00 is a unique local addres and it's the internal private IP addresses
# There's no broadcast address in IPv6
# FF00::/8 is the multicast address


######################## Shortcuts ########################
# 01- IPX ( Internetwork Packet Exchange but it's killed when IP appeared ).
# 02- ASCII ( American Standard for Computer Information Interchange ).
# 03- WAP ( wireless access point ).
# 04- WAN ( wide area network ).
# 05- MAC ( Media Access Control ).
# 06- IP ( Internet Protocol ).
# 07- TLS ( Transport Layer Security ).
# 08- TELNET (Teletype Network).
# 09- WI-FI (wireless fidelity).
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
# 38- CIDR ( Classless Inter-domain Routing Notation ).
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
# 56- SFD ( Start Frame Delimiter )
# 57- FCS ( Frame Check Sequence )


######################### Standard numbers in network #########################
# 1- IEEE 802.3         => is the standard number for ethernet.
# 2- IEEE 802.11        => is the standard number for WI-FI.
# 3- H.323              => used to setup, maintain, teardown voice and video connections, operates over RTP (real time protocol) protocol.
# 4- IEEE 802.1D        => is the standard for the classic spanning tree protocol.
# 5- IEEE 802.1x        => User Authentication.
# 6- IEEE 802.3ad       => is the standard number for LACP (Link Aggregation Control Protocol).


############################ Networking Commands For Troubleshooting ############################
# 1- tracert   => is a command that allows you to check all the routers you go through from your system to any other system, displays the path between device and it's destination, showing
#                 the source and destination ip address for each hop along the way.
# tracert (Windows), traceroute (Linux)
# usage  => tracert destination  => tracert www.google.com
# Hop is any router or firewall that is in the path of the transmission from client to destination.

# 2- pathping  => similary to tracert but with more information and more faster.
# usage => pathping destination  => pathping www.google.com

# 3- ping      => used to get the status of a specific destination, helps us in network troubleshouting
# usage => ping www.google.com
#               ping -n option allows you to specify the number of ping ( ping -n 10 google.com )
#               ping -t option allows you to ping forever, you can use it to test if the WAN connection is running or not
#               ping -c number option works in linux and it will specify the number of ping ( ping -c 10 google.com )
# in windows ping will ping the target 4 times as default and if you want to ping it forever use ping -t, while in linux by default it will ping the target for ever until you stop it.


# 4- ipconfig  => displays all of the current TCP/IP network configuration values and refreshes DHCP and DNS settings for a windows client or server.
# ipconfig (Windows) ifconfig (Linux)
# usage => gives you information about your network like ipv4, ipv6, DHCP server, etc...
#               ipconfig /release :- to remove the ipv4 address and the subnet mask and the default gateway
#               ipconfig /renew   :- to renew the ipv4, subnetmask, default gatway
#               ipconfig /all     :- will give you more configurations like mac address, DNS server.

# 5- route print == netstat -r
# usage  => to print the routing table in windows.

# 6- tcpdump => works in linux, and it is a alternative capture tool like wireshark
# usage  => it's a network analyzer

# 7- netstat => lists all the open ports and connections on your computer, and to show you what is the type of network connections esablished between your computer and any other computer
# usage => netstat -n option will give you the ip address of the foreign address.
#               netstat -b option shows the executable for every connection.
#               netstat -o option shows you the executable and process id for every connection.
#               netstat -a option shows you all the active ports.
#               netstat -r option shows you the local routing table.

# 8- ip => Assigns an address to a network interface or configures netwrok interface prameters on a Unix, Linux, or OS X operating systems, replaced the ifconfig.

# 9- nslookup (name server lookup) :- used to query the DNS to provide the mapping between domain names and IP addresses or other DNS records, it is used to know the ip address of a domain name.

# 10- hostname => used to display the hostname portion of the full computer name for a given system.

# 11- arp (address resolution protocol) => used to display and modify entries in the ARP cache on a system.
# usage => arp -a option to show you the ARP cache.
