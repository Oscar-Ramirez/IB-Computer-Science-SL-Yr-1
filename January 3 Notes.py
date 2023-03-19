print(""" Which one would you like to know more about? 
\033[1m Options \033[0m
1) IPO (Input-Process-Output)
2) Peripherals
3) Components of a Computer
""")

answer = "empty"
userchoice = input()
while (answer == "empty"):
  answer = "chosen"
  if (userchoice == "1"):
    print("""
    -Receives some input, processes it, and produces some output
    -Storage might be used as a cache
    -Feedback loop = output from one process being inputted again, to run the same process again or for a different process
    """)
  elif(userchoice == "2"):
    print("""
    -A hardware device that is used to transfer information into and out of a computer.
    -Refers to all hardware components that are attached to a computer and are controlled by the computer but they are not the core components of the computer
    -Input Device: sends data or instructions to the computers
    -Examples: mouse, keyboard, graphics tablet, image scanner, barcode reader, and game controller
    -Output Device: provides a platform for the data sent from the computer
    -Examples: Monitors, projectors, printers, headphones, and speakers
    -Input/Output Devices: performs both input and output functions
    -Examples: HDD, SDD, USB Flash Drive, modem, network adapter, and multi-function printer
 """)
  elif(userchoice == "3"):
     print ("""
     -Case: This houses all of the other internal components 
     -CPU: Executes instructions of a computer program, such as arithmetic, logic, controlling, and input/output (I/O) operations
     -Motherboard: This is like the back bone of the computer, it allows for communication between all the other internal components. 
     -RAM: Random Access Memory, a form of computer memory that can be read and changed in any order, typically used to store working data and machine code.
     -Graphic Card:  computer expansion card that generates a feed of graphics output to a display device such as a monitor.
     -HDD: data storage device that stores and retrieves digital data using magnetic storage with one or more rigid rapidly rotating platters coated with magnetic material.
     -SSD: a solid-state storage device that uses integrated circuit assemblies to store data persistently, typically using flash memory, and functioning as secondary storage in the hierarchy of computer storage.
     -Power Supply: convert electric current from a source to the correct voltage, current, and frequency to power the load. 

 """)
