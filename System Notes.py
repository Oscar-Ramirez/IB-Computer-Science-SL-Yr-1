print("""System Notes

- MENU- 
--------
Please choose one of the options below, and press enter

1) What is a System?
2) Legacy Systems
3) Planning
4) Changing Management
5) Business Merger
6) Modern Example from US Post Office
7) Hyppthetical Example
8) System Changeover
9) Implementation Methods
10) Related to Data Mirgration
11) Phases in Data Migration
12) Related to Business M&A
13) Strategies for integration
14) On-Premise Software
15) Saas
16) Software Lifecycle
17) Functional Testing
18) Debugging
19) Validation vs Verification
20) Testing and Types of Testing
21) Types of Data used in Testing


""")

answer = "empty"
userchoice = input()
while (answer == "empty"):
  answer = "chosen"
  if(userchoice == "1"):
    print(""" A system is not just hardware + sofeware, it also includes people and immediate environment. A system may include: training employees and/or users, as well as maintaining and protecting data or hardware.A new system should improve the cost-to-benefit ratio in contrast to not implementing the system. There are a bunch of reason to implement a new system: replace a current system because it's inefficient, no longer suitable for desired tasks, or redunant or out-dated. The system may be added for a purpose that is new for an organization.""")
  elif(userchoice == "2"):
      print("""An Example would be a hospital and the systems it uses: Clinical, Accounting, Pharmacy, and Purchasing. These systems sometimes need to communicate with each other but are also sometimes stored in indivisual silos and silos do not communcate with each other. 
\033[1m Multiple systems that do not communicate with each other are called Legacy Systems \033[0m
There are some situtations where moderns systems have to work together with legacy systems.
An example would be, if the legacy system contains a lot of data it is not realistic to transfer all the data unless there is an automated way to.""")
  elif(userchoice == "3"):
      print("""When planning on implementing a new system, including discussing new hardware, changing potential locations of technology, new policiess, new training and upskilling, and potentially hiring and firing employees as well.
There is also a varity of issues that should be taken into consideration during the planning process:
A lack of ...
  - Organizational & Bussiness strategy
  - Stakeholder & end-user participation
  -End-user 'ownership'
Attention to ...
  -Required training
  -Organizational issues, inclding group culture
  -Design of tasks & job roles
  -Overall usability of the system
After considering the issues mentioned above a feasibility study should be conducted, the study should cover different areas. A common acronym is TELOS.
T: Technical (Here all hardware and software would be justified in whether it is necessary for the new system)
E: Economic (Relates to the budget for a project and how money will be spent, financial costs for purchasing new hardware or software, cost on training staff or timelines running past deadlines)
L: Legal (are there any conflicts between the proposed system and any local laws, regulation, etc.)
O: Operational (Realtes to whether the participants will be able to handle the new system. Factors that need to be considered include the technical skills of employees, as well whether or not raining will be nescessary for sstaff and what materials would need ro be avaliable for training.)
S: Schedule (Relates to the amount of time allocated to the development of the new system. The time frame would be assessed, as projects that run overtime can have both a financial and organizational impact on business.)
""")
  elif(userchoice == "4"):
    print(""" Changing systems almsot always includes some form of change management. This may ne shifting, hiring, or letting go employees or whole deparments, it may be just changing the process or work they do.
Organizantial Change
  -Refers to the actions in which a company or business alters a major componet of its organization such as: its culture, underlying technologies or infrastructure it uses to operate, or its internal processes.
Change is often approached with concern, and sometimes fear; especially if it includes new tech or somputerized/automated systems. Change management should maximize benefits and mimimize negatives, for all stakeholders, including the employees.
Successful change management should result in buy-in from all stakeholders. Resistance or conflict related to new processes or work stations suggests change mangagement was not entirely successful. Some famay fear that they may lose their job with increased automation, and unfortuanately this sometimes comes true.
""")
  elif(userchoice == "5"):
     print("""- Mergers combine two seperate businesses into a single new legal entity. True megers are uncommmon because it's rare for two equal companies to mutaully benefit from combing resources and staff, including their CEOs. 
""")
  elif(userchoice == "6"):
    print("""Almost all letters in the US are taken to the closest processing center, where cameras and computer take a picture of the front of the envelope and read the address with optical characyer regonition, OCR.
What if the handwriting on the letter is bad?
The post office have a system in place where letters are sent to a facility to verify what the handwriting is saying.
The system they have in place is solefy for the purpose of reading bad writing and to make it more efficent for the person who is reading the hand writing. From the software that is used to the custom key board that are used for their work.
On the software being used, it tracks that amount the work and progress that been made for the day.
There are rules that the person who is reading that have to follow such as the 3+1 rule and writing exactly what the sender wrote.
""")
  elif(userchoice == "7"):
    print("""If this new system was implemented some affects that might happen is that if there was multiple secretaries to help put in the order than some would be let go since the salesperson is now handling the orders and not the secretaries.
""")
  elif(userchoice == "8"):
    print("""Is the process used to swithc from one system to another. The smaller environments like an individual changing their perosnal system or a family changing theirs probably won't have much thought or concern.
The larger the environment becomes the more problematic and complicated changing that system may be.
A company or organization likely handles and stores people's personal data, financial information, and may also be tired to people's livelihood health and wellness or a region's infrastructure.
System changeover in facilities like medidical facilities, power planets, and communication provider can lead to significant consequences so there are various stratigies that can be used to change systems.
""")
  elif(userchoice == "9"):
    print("""arrallel: Both systems work in parallel for a short period of time, this allows for measuring output of the new system before the old system is taken offline.
If the new system is not sastifactory in its functionality then those issues can be ironed out while the old system is still running. 
This can be both expensive and taxing as both systems are running at the smae time.
This may require addtional man power, computer or network resources, and financial expense and if the two systems are drastically different then this method can be extremly uneffecient for how long this change will take.
Big Bang/Direct/Immediate: As soon as preperations are made one system is entirely discontinued, and the other is brought online.
This is the least taxing on computer and network resources but requires frontloading training priot to the changeover.
Any data that needs to be transfered from old system to new may need a third system or external location while the changeover happens.
Pilot: A smaller group of an organization or company changes to this new system. Allows for test on the new system and iron-out issues with lower risk before it is implemented to the whole organization.
Once the system is succesful in the pilot group then it planning for whole company implementation can start.
Phased: Change one part of the system at a time over a period of time. 
The old and new system may need to be similar enough for the data and process go back and forth between the two.
This process will generally take longer as each phase is implemented seperately.""")
  elif(userchoice == "10"):
    print("""What is Data Migration: Moving data from one system to another system in the most optimal fashion
Account for needing to transfer data from one system to another.
Changing formats
Types of storage
Computer systems
Issues that may occur during transferring.
Changing mediums ex.: Changing from Paper files to digital one
Incompatibility of data types in digital formats ex. Data stored in PDFs to go into a csv spreadsheet format.
Issues may be caused if the data migration process times out, fails, or encounters other errors, data is misinterpreted
""")
  elif(userchoice == "11"):
    print("""3 stages: Plan, Migrate, and Validate
Plan: Should include determining the requirement of the migration, future environment, development, and documentation of migration plan
Migrate: Plan is communicated, all needed software and hardware is obtained, installed, and configured, and the process of actual transference occurs.
Validate: Test check that data is in the same state before and after the migration. Tests should be run pre-migration and post-migration to have a benchmark.
""")
  elif(userchoice == "12"):
    print("""Likely to be changes to the systems when two or more business entities merge and integrate into one.
Merging can result in reduced cost by controlling more of the process, reducing competition, or other factors.
The merger should result in a competitive advantage for the new merged entity.
""")
  elif(userchoice == "13"):
    print("""Strategies for integration
Both systems may be kept, with development to have the same functionality. Running both systems in parallel has high maintenance costs.
Both systems may be replaced with a new system. This may result in a new system that meets the new company/organization's needs better overall, but will have higher increased initial costs, including new training for all employees.
Select the best system components from each and merge them. This provides some familiarity for original employees from both, but may result in a longer period to become adjusted to the entire system due to operating by habit in some parts instead of a total change.
Select the better of the two systems, and drop the other system entirely. Those used to the dropped system may show resistance to change, and there may be policy issues. However, those already familiar with the chosen system can be resources since they are already experienced with it.
""")
  elif(userchoice == "14"):
    print("""On-Premise Software
Installed and runs on computers on the premise of the person or organization instead of a remote facility like a server farm or cloud
Sometimes referred to as “shrinkwrap” software
Typically requires IT staff or IT support or Software engineer which can result in more cost.)
  elif(userchoice == "15"):
    print(Saas
Meaning “Software as a service”
A software licensing and delivary meodel in which software is licensed on a subscription basis and is centrally hosted.
Sometimes refered as “on-demand software” and was formally refered as “software plus services” by Microsoft
Advantages
Lower Initial cost, likely faster implementaion
Maintencance and updates by software manudacturer
No staff needed to maintain the system
Software manufacturer likely provides more support
On-site natural disasters do not put data at risk
Disadvantages
continued subscription fees may ultimately be more expensive than On-premises software or custom designed software for large companies
Potential data-risk from software manufacturer
Potential differing time zones, maintenance and support may not be at convenient times
Specialized or unusual needs of a specific client may not be a priority of the software manufacturer
Because host is not the user itself, user feedback is harder to get
System change may be required sooner than ideal if the service is discontinued, the company seeks new functionality that the manufacturer is not interested in adding, or the manufacturer goes out of business
""")
  elif(userchoice == "16"):
    print("""Software Lifecycle
Planning
Customer will find the company they want to use for their project, meeting with that companies project manager or product owner, discuss terms of agreement, sign the deal, then start the project. Requirements for the application will also be outlined and future requirements may be added
Requirement Analysis
Define each outline reuirement and give more planning details
Design
Takes all the requirements and starts to plan the product, may include: business rules, user-interface layout, color schemes, which programming languages to use, frame works, system server design, database relationships, archtech of the application, mobile aspects, supported browsers and much more.
Implementaion / Coding
Physical hardware will be setup, code will start being written, continuing planning user-interface, and analyze requirements to test cases for their test plans
Testing
Start testings and executing test plans that were created, validate that all the requirements are met, make sure all functionality is working as expected, find and fix bugs, 
Deployment
Mirror the staging or development setup and make it scaleable for production, install new hardware,  set up links, databases, and syncing up the development teams and release managers, application will go live for real users
Maintenance
Making sure that the application is stable and works and makikng sure that the servers are able to work properly and any bugs that are found are sorted out.
""")
  elif(userchoice == "17"):
    print("""Functional Testing: A type of software testing that validates the software system against the functional requirements/specifications.
""")
  elif(userchoice == "18"):
    print("""Debugging: The systematic process of correcting and finding bugs or erros in a program.
""")
  elif(userchoice == "19"):
    print("""Validation vs Verification
Verification: A way of preventing errors when data is copied from one medium to another. Only makes sure that data matches.
Validation: An automatic computer check to ensure that the data entered is sensible and reasonable.
""")
  elif(userchoice == "20"):
    print("""Testing and Types of Testing
Two Categories: Dynamic and Static
Dynamic: Using the system to test, running and operating the software or system for testing.
Static: Testing where the software or system is not actually running, maybe analyzing the algorithm design, reviewing code, or checking client’s request.
Variety of methods relating to testing: Functional, User Acceptance, and Integration.
Functional: testing individual commands, text input, menu functions, etc.
User Acceptance: Determining if the system satisfies the customer’s need. Usually done on premise before the system or software is shipped or transferred to the customer. 
Integration: Test different parts of a system or software, this also often includes inputting data to verify whether or not the system returns the expect output. 
Dry Run Testing: The process of a programmer manually working through their code to trace the value of variables.
Alpha Testing: The software or system is release to those within the cmpany or organization who are not specifically involved in the development or implementaqtion of the product. This allows for them to get feedback and testing data similar to how actual customers would use the new product.
Beta Testing: The software system is availble to the public or a group consisting of the public. This is closest and most realist testing that is possible for a new product.
""")
  elif(userchoice == "21"):
    print("""Types of data used in Testing: Normal, At the Limits, Extreme, and Abnormal
Normal: Typical data (expected) that should be accepeted by the system
Extreme: Data at the upper or lower limits of the expections that shold be accepted by the system
At the Limits: A pair of values at each end of a range
The data at the upper or lower limits of expectations thta sould be accepted
The immediate values before or beyond the limits of expectations that should be rejected
Abnormal: Data that falls outside of what is acceptable and should be rejceted by the system
""")
