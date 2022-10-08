print(""" Which one would you like to know more about? 

\033[1m Options \033[0m
1) Update Terminology
2) Components of a Computer System
3) Servers and Clients
""")

answer = "empty"
userchoice = input()
while (answer == "empty"):
  answer = "chosen"
  if (userchoice == "1"):
    print("""Patches: used by software companies to update applications by fixing known bugs and vulnerabilities. Be aware that patches may introduce new bugs.

Upgrades: contain a novel function or characteristic and cumulative bug fixes. Upgrades often require an additional purchase

Updates: improve a product in a minor way, add new functionality or fix a bug. Updates are usually free, Updates may be obtained manually, or may also be automatic through an internet connection.

Releases: Final working versions of software applications. Prior to release, they should undergo alpha and beta testing. A release is a new product or an upgraded product.
 """)
  elif(userchoice == "2"):
    print("""Hardware: Physical Parts of the system.

Software: A set of instructions that makes the computer system do something, these sets of instructions are collected together in workable groups called programs, without programs and instructions computers would not be able to function.

Peripheral Devices: Hardware devices that are outside the computer processor, are typically connected to the computer by cables. Examples: Printer and Hard Disk. Input and output devices. Inputs are devices that put data into a computer system and output devices display data the computer system is putting out. Printing a document for example.

Computer Network: A set of computer systems that are interconnected and share resources, as well as data. For example Local Area Network, Wide Area Network, etc.

Human Resources: people who are part of (or could be part of) an organization, business, or economy.
 """)
  elif(userchoice == "3"):
     print ("""Server: A dedicated computer that provides services for clients. Multiple Clients connect to through the internet or local area network. 

Dumb Terminal: A terminal that does not perform local processing of entered information, but serves only as an input/output device for an attached or network-linked processor.

Thin Client:  a computer that uses resources housed inside a central server as opposed to a hard drive

Client: Any computer hardware or software device that requests access to a service provided by a server

Email Server: A computer system that sends and receives emails

Router: a device that connects two or more packet-switched networks or subnetworks
DNS Server: A DNS server is a computer server that contains a database of public IP addresses and their associated hostnames, and in most cases serves to resolve, or translate, those names to IP addresses as requested

Firewall: a part of a computer system or network which is designed to block unauthorized access while permitting outward communication.

Client-server: denotes a computer system in which a central server provides data to a number of networked workstations.
 """)
