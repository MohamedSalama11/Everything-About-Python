# NOTE:-
# servers or clients also called endhosts or endpoints.
# MAC addresess may also called (BIA) => Burned_In Address this is because the address is burned into the device as it's made.
# There are MAC addresses known as locally unique MAC addresses which don't have to be globally unique.
############### Routers ###############
# when we see a router like this CISCO ISR 2911 => CISCO is the company made this router, ISR is a line of CISCO routers, 2911 is a particural model in that line.
# Dynamic MAC addresess are removed from the MAC addresses table after 5 minutes if there's no traffic this is known as Aging.
# the minimum payload size for an etherent frame is 46 bytes and if it's not 46 bytes padding will be added, padding is just a series of zeros.

#################### Switches ####################


################## Hubs ##################


################ Firewalls ################

######################## Shortcuts ########################
# 01- SFD    => Start Frame Delimiter
# 02- FCS    => Frame Check Sequence
# 03-
# 04-
# 05-
# 06-
# 07-
# 08-
# 09-
# 10-
# 11-
# 12-
# 13-
# 14-
# 15-

######################### Standard numbers in network #########################
# 1- 802.3    => is the standard number for ethernet.
# 2-
# 3-
# 4-
# 5-
# 6-
# 7-
# 8-
# 9-

####################### Packet Tracer CLI #######################
# NOTE:-
# 01- >                                                           => means that you are in user Execution mode also called user mode this mode can not change the configuration.
# 02- #                                                           => means that you are in privileges Execution mode this mode can not change the configuration.
# 03- (config)#                                                   => means that you are in global configuration mode.
# 04- <cr>                                                        => means that there's no other options.
# 05- 7                                                           => number seven indicates the type of ecnryption used to encrypt the password, means it's using cisco proprietary encryption alghorithm.
# 06- 5                                                           => number five indicates MD5 Encryption.
# 07- (config-if)#                                                => means that you are in the interface configuration mode.
# 8- (config-if-range)                                            => means that you are in the range of interfaces



# 01- enable                                                     => to enter the privileges exeuction mode, en is the shortcut.
# 02- ?                                                          => to view the commands available in the mode you are currently at.
# 03- e?                                                         => will show the commands enable that starting with letter e.
# 04- configure terminal                                         => to enter the global configuration mode, conf t is the shortcut.
# 05- enable password your_password                              => to create password for the global configuration mode.
# 06- exit                                                       => to return to the back mode, will log out the device when you are in the privileges exec mode.
# 07- show running-config                                        => to view the running configuration file on the privilege exec mode.
# 08- show startup-config                                        => to view the startup configuration file on the privilege exec mode, which will be loaded if the device restarted.
# 09- write                                                      => to save the running configuration to make it the startup configuration, only from the privilege execution mode.
# 10- write memory                                               => same as write.
# 11- copy running-config startup-config                         => to copy the running-config file to the startup-config file, same as write and write memory.
# 12- service password-encryption                                => will encrypt all passwords in a set of numbers and letters so they can not easily hacked, not secure enough it can be cracked easily.
# 13- enable secret your_password                                => more secured method to create passwords with more tough encryption alghorithm.
# 14- do                                                         => to run commands works in the privilege exec mode while you are in the global configuration mode, example => do show running-config.
# 15- run                                                        => executes a privileged exec level command from global configuration mode, example => run privileged-exec-level-command.
# 16- no                                                         => used to remove a command which you previously configured.
# 17- hostname name                                              => to change the hostname to the name you want.
# 18- show arp                                                   => to show the arp table in the privilege exec mode.
# 19- show mac address-table                                     => to show the mac address table on a switch.
# 20- clear mac address-table dynamic                            => to remove all the dynamic MAC addresess.
# 21- clear mac address-table dynmaic address the_mac_address    => to remove a specific MAC address.
# 22- clear mac address-table dynamic interface the_interface    => to remove all MAC address table entries for a specific interface.
# 23- show ip interface brief                                    => to confirm the status of each interface on the device as well as their ip addressess.
# 24- interface name_of_interface                                => to configure the interface on the device, example => interface gigabitethernet 0/0 or in g0/0, shortcut is in.
# 25- ip address the_assigned_ip subnetmask                      => to assign ip address to specific interface, example ip address 10.255.255.254 255.0.0.0.
# 26- no shutdown                                                => to enable the interface we currently at, we write it because cisco router interfaces have the shutdown command by default.
# 27- show interfaces                                            => display alot of inforamtion about the interfaces on the device, also the errors.
# 28- show interface name_of_interface                           => display alot of information only about the specified interface, example show interface g0/0.
# 29- show interfaces description                                => give you a status of the interfaces.
# 30- description description_you_want                           => to configure an interface description
# 31- show inerfaces status                                      => display information on switch interfaces.
# 32- speed speed_you_want                                       => to specify the speed you want on a specific interface.
# 33- duplex auto/full/half                                      => to make the interface send and receive data in the same time.
# 34- interface range f0/5 - 12                                  => this is an interfaces range from interafce f0/5 to f0/12
# 35- interface range f0/5 - 6, f0/9 -12                         => this is an interface range from interface 5 to 6 and from 9 to 12, means that interface 7,8 not in the range.
# 36- shutdown                                                   => to shutdown the interfaces.
# 37- 
# 38- 
# 39- 
# 40- 
# 41- 
# 42- 
# 43- 
# 44- 
# 45- 
# 46- 
# 47- 
# 48- 
# 49- 
# 50- 