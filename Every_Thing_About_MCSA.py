###### WINDOWS SERVER 2022 EDITIONS:- ######
# 1. Windows Server 2022 Essentials
# Target: Small businesses (25 users, 50 devices max)
# Think of it like: A compact car – small, efficient, and easy to manage.

# Features:
# Simplified management
# No virtualization rights
# Affordable for small teams

# 2. Windows Server 2022 Standard

# Target: Mid-sized businesses
# Think of it like: A family SUV – bigger, more powerful, can handle more tasks.

# Features:
# Supports up to 2 virtual machines
# Requires CALs (Client Access Licenses)
# Includes core Windows features (Active Directory, DNS, DHCP)
# 3. Windows Server 2022 Datacenter
# Target: Large enterprises and data centers
# Think of it like: A huge truck – powerful and built for heavy-duty work.

# Features:
# Unlimited virtual machines
# Advanced features (Shielded VMs, Storage Spaces Direct, Software-Defined Networking)
# Ideal for virtualization-heavy environments

# 4. Windows Server 2022 Datacenter: Azure Edition
# Target: Cloud-connected businesses
# Think of it like: A flying car – works on the ground and in the cloud

# Features:
# Exclusive to Azure (Microsoft's cloud)
# Hotpatching (no reboot updates)
# Advanced cloud integration features

##### What is Hyper-V? #####
# Hyper-V is a virtualization technology developed by Microsoft.
# It lets you create and run virtual machines (VMs) on a physical Windows server or computer.

##### What is a VM? #####
# A VM is a virtual machine that is created on a physical server or computer.
# It is a virtualized computer that can run its own operating system and applications.


###################### Everything About Printers ######################
# a printer is a type of device that is used to print text and images on a piece of paper.
# printer is a software program that controls physical printers devices.

#### printer conectivity ####
# 1- USB connections
    # the most common type of them and it's usually used within home envrionment.
# 2- Wired connections
    # uses network cables to plug into an RJ-45 port on the back of the printer.
# 3- wireless connections
    # generally comes in Wi-Fi or bluetooth.
    # wifi connectivity can use either infrastructure mode or wifi direct mode.
    # in infrastructure mode the printer connects to the network access point, receives an ip address via DHCP server, and functions like a wired device.
    # in wifi direct mode, the printer acts as it's the access point, broadcasts an SSID, and can be connected directly to the laptop to print wirelessly

########################################################################################### Notes ###########################################################################################
# 01- each computer in workgroup has it's own local SAM which stands for Security Account Mananger, it's a hidden database in all windows operating systems that contains the user accounts.
# 02- the software we use on a server to actually create the users account for each computer in the domain is called AD DS => active directory domain services.
# 03- active directory server we normally call a domain controller which is just a server, but a domain controller is nothing but the windows server that runs the active directory domain services.
# 04- when you create a new user in active directory server the password by default expires after 42 days.
# 05- when you add AD DS to your domain you need to convert your domain to a domain controller that hosts the AD DS.
# 06- the way things are organized within your domain is in organizational units and containers.
# 07- when you install AD DS on your domain controller several containers are created automatically.
# 08- everything about AD DS are actually stored in a database called NTDS.DIT and it's path is C:\Windows\NTDS\NTDS.DIT.
# 09- SYSVOL is a shared folder that is used to store files that are shared between all computers in the domain.
# 10- domain controllers host the kerberos authentication service and it is the authentication protocol for active directory.
# 11- KDC (key distribution center) is just an authentication service as well, it is used to authenticate users and computers on the domain controllers.
#     the difference between the kerberos authentication service and the KDC is that the kerberos authentication service is used to authenticate users and computers on the domain controllers
#     while the KDC is used to authenticate users and computers on the domain controllers it self.
# 12- the difference between the group policy and group policy preferences is that the group policy preferences let the user to set the preferences for the group policy, while the default group policy
#     is administratively defined so the user can not change it.
# 13- all DNS servers actually comes with root hints, root hints is just a list of the root servers that are used to resolve the domain names, is just a list of the public 13 root DNS servers.
# 14- when you want to create a template in active directory users and computers, it's name should begin with underscore to bring it up of the list of users, we create templates
#     so we could copy users and computers easily, so if i want to create template for guests of the network i just need to create the user one time and copy it for each guest user enters the network.
#     you add this guest template to the domain guests group, you don't need to specify a password for it, it will be a disable account.
# 15- when you want to give higher and custom permissions for a specific user or group just right click on the user and choose delegate control to open the delegation wizard.


################################################################################################# shortcuts #########################################################################################
# 01- MCSA          => Microsoft Certified Solutions Associate.
# 02- MCSE          => Microsoft Certified Solutions Expert.
# 03- LTSC          => Long Term Support Channel.
# 04- LTSB          => Long Term Support Branch.
# 05- CAL           => Client Access License.
# 06- KMS           => Key Management Service, works on port 1688.
# 07- GPO           => Group Policy Object.
# 08- AD            => Active Directory.
# 09- DNS           => Domain Name System.
# 10- DHCP          => Dynamic Host Configuration Protocol.
# 11- WSUS          => Windows Server Update Services.
# 12- SCCM          => System Center Configuration Manager.
# 13- AD DS         => Active Directory Domain Services.
# 14- AD RMS        => Active Directory Rights Management Services.
# 15- AD LDS        => Active Directory Lightweight Directory Services.
# 16- SLMGR         => Software Licensing Manager.
# 17- SAM           => Security Account Mananger.
# 18- OUs           => orgranizational units.
# 19- GC            => global catalog.
# 20- RODC          => read-only domain controller.
# 21- KDC           => key distribution center.
# 22- BPA           => best practice ananlyzer..
# 23- FAT           => File Allocation Table.
# 24- NTFS          => New Technology File System.
# 25- ReFS          => Resilient File System.
# 26- exFAT         => extended File Allocation Table.
# 27- MFT           => Master File Table.
# 28- Dedup         => Data Deduplication.
# 29- DFS           => distributed file system.
# 30- DPM           => data protection manager.
# 31- VSS           => volume shadow copies services, also called shadow copies.
# 32- PPTP          => point to point tunneling protocol.
# 33- L2TP          => layer 2 tunneling protocol.
# 34- SSTP          => secure socket tunneling protocol.
# 35- IKEv2         => internet key exchange version 2.
# 36- PAP           => password authentication protocol.
# 37- CHAP          => challenge handshake authentication protocol.
# 38- MS-CHAPv2     => Microsoft challenge handshake authentication protocol version 2.
# 39- EAP           => extensible authentication protocol.


######################################################################################### Commands ##################################################################################################
# 01- winver                                                                  => to check the version of the windows server.
# 02- systeminfo | findstr /B /C:"OS Name" /C:"OS Version"                    => to check the windows server edition.
# 03- ipconfig                                                                => to check the ip address of the windows server.
# 04- ipconfig /release                                                       => to release the ip address of the windows server.
# 05- ipconfig /renew                                                         => to renew the ip address of the windows server.
# 06- ipconfig /flushdns                                                      => to flush the dns of the windows server.
# 07- ipconfig /displaydns                                                    => to display the dns of the windows server.
# 08- ipconfig /registerdns                                                   => to register the dns of the windows server.
# 09- slmgr.vbs                                                               => to check the license of the windows server, runs on the RUN command.
# 10- slmgr.vbs /dli                                                          => to display licensing information.
# 11- slmgr.vbs /xpr                                                          => to check the expiration date of the license.
# 12- slmgr.vbs /dlv                                                          => to display the license details.
# 13- c:\Program Files                                                        => to open the program files folder., runs on the RUN command.
# 14- regedit                                                                 => to open the registry editor.
# 15- msinfo32                                                                => to open the system information.
# 16- control                                                                 => to open the control panel.
# 17- diskpart                                                                => to open the diskpart tool.
# 18- diskpart /list disk                                                     => to list the disks.
# 19- diskpart /select disk 1                                                 => to select the disk.
# 20- diskpart /list volume                                                   => to list the volumes.
# 21- diskpart /select volume 1                                               => to select the volume.
# 22- diskpart /delete volume 1                                               => to delete the volume.
# 23- diskpart /create partition primary                                      => to create a primary partition.
# 24- notepad                                                                 => to open the notepad.
# 25- calc                                                                    => to open the calculator.
# 26- mspaint                                                                 => to open the paint.
# 27- cmd                                                                     => to open the command prompt.
# 28- powershell                                                              => to open the powershell.
# 29- wmic                                                                    => to open the wmic tool.
# 30- wmic process list full                                                  => to list the processes.
# 31- wmic process get name, processid, commandline                           => to get the name, process id, and command line of the processes.
# 32- shell:appsfolder                                                        => gives you all the apps and programs setuped in the your computer, runs in the RUN command.
# 33- \\servername                                                            => to show the shared folders of the server, runs in the RUN command, example:- \\rts-dc1.
# 34- whoami /groups | findstr "Domain Admins"                                => to check if the user is a domain admin.
# 35- dcgopfix                                                                => to fix the group policy of the domain and domain controller.
# 36- gpresult                                                                => verify the GPOs that currently applied to the user and computer account, and determine which GPO applied the setting.
# 37- gpupdate                                                                => to update the group policy of the domain and domain controller, applies only the policies that have changed since the last update.
# 38- gpupdate /force                                                         => to update the group policy of the domain and domain controller, reapplies all policies, even if nothing changed.
# 39- gpedit.msc                                                              => to open the local group policy editor.
# 40- set-location relative_path                                              => to go to a specific location, same as cd command.
# 41- gpresult /h file.html                                                   => to create a html file showing the GPOs Results applied to the user and computer account.
# 42- ddpeval dirve_letter                                                    => shows you if you provide data deduplication to this disk how much space you are gonna save, ex => ddpeval E: .
# 43- \\server_name                                                           => will open all the shared folders on the server ex => \\rts-dc1.
# 44-
# 45-


####################################################################### PowerShell For MCSA #######################################################################
# windows powershell is a command line shell and scripting language.
# windows powershell cmdlets execute in a windows powershell console or can be executed as powershell scripts.
# Cmdlets is command line utilites that perform specific function.
# modules is a cmdlets specific to a product are packaged together and installed as modules.
# powershlle ISE ( integrated scripting environment ) is a graphical user interface tool that allows you to run commands, create, modify, execute scripts.
# any command structure in powershell will always be like this - Verb-Noun, example => Test-connection google.com
# when ever you write a command always use tap completition to complete the command, same thing for the options of the command (some called switches), same for parameters.
# always use powershell ISE to search for the commands you need and it's parameters, from the command window search for the command you want and adjust it's parameters and then click insert.
#


############### Commands ###############
# 01- Test-connection google.com -count 5                                                               => will test the connectivity of google 5 times.
# 02- Get-Eventlog -LogName System                                                                      => will get the logs of the system.
# 03- Get-netipaddress                                                                                  => will get everything related to your network.
# 04- Get-help *eventlog*                                                                               => will search for every command contains eventlog keyword in it.
# 05- Get-help get-eventlog -detailed | -examples | -full | -online                                     => operators used with get-help command.
# 06- Get-command "*aduser"                                                                             => to search for the commands that contains the keyword aduser.
# 07- Get-Command | Where-Object { $_.Source -eq "Microsoft.PowerShell.Core" }                          => to get all the commands in powershell.
# 08- get-windowsfeature                                                                                => to show you all the features installed and available in the server.
# 09- get-windowsfeature -name "RSAT-AD-Tools"                                                          => to show you the RSAT-AD-Tools feature.
# 10- install-windowsfeature DNS -includemanagementtools                                                => to install the DNS feature and the management tools.
# 12- get-ADUser -identity administrator                                                                => to get the administrator user of the domain.
# 13- get-ADUser -filter *                                                                              => to get all the users of the domain.
# 14- unlock-ADAccount -identity useraccount                                                            => to unlock a specific user account.
# 15- disable-ADAccount -identity useraccount                                                           => to disable a specific user account.
# 16- enable-ADAccount -identity useraccount                                                            => to enable a specific user account.
# 17- search-ADAccount -AccountDisabled                                                                 => will return all the disabled account on the domain.
# 18- search-ADAccount -UsersOnly -AccountInactive -TimeSpan 60                                         => will search for only the user account that has been inactive in the past 60 days.
# 19-
# 20-

######################################################################################## Real Life IT Scenarios #########################################################################################
# 01- when we add a new computer to the domain, it will create by default a password for the computer, this password is called the computer account password, and it changes every 30 days, so when the user have a vacation and he doesn't have access to the computer, and he returns back and try to login to the computer the computer will  pops him a message that the password has expired, and to solve this problem we need to rejoin the computer to the domain.
# 02- when you are trying to join a new server to your main server and a problem occurs, one of the most common erros is the DNS address of the server you want to join is not the same as the address of
#     the main server.
# 03- when any problem occur with internet access in the domain envrionemt, always look at the DNS server first, because the DNS server is the one that is responsible for resolving the domain names.
#     if you want all the users in the domain to not have internet access, you can remove the root hints from the DNS server.
