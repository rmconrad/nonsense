# This script will parse the flat file error reports from MetLife into a readable excel file

header_list = ["CUST NO","CODE","ACTN","EMPLOYEE ID","MBR LAST NAME","MBR FIRST NAME","RC","DOB","SSN","X","PERSONNEL #","ST","ZIP","CV","C START","C STOP","C GROUP","CSUB","CBRANCH","CP","S","M","CN","C EU1","CV","M START","M STOP","M GROUP","MSUB","MBRANCH","MP","S","M","CN","M EU1"]

error_code_map = {"0001":"Birthdate not valid or missing","0004":"Employee number not valid","0006":"Cannot create new record - currently exists as surviving dependent cross-reference","0007":"Relationship code not valid or missing","0014":"State not valid or missing","0015":"Zip code not valid or missing","0016":"Date of hire not valid or missing","0033":"Possible duplicate dependent in MetLife","0039":"Last name contains invalid characters","0041":"First name is missing","0042":"First name contains invalid characters","0045":"SSN has invalid character","0046":"Relationship code must be 0 for EE","0048":"Gender code is not valid","0050":"Marital status not valid","0070":"Coverage start date no valid","0073":"Start date prior to cancellation date in MetLife","0074":"Start date in conflict with start date in MetLife","0076":"Coverage end date is not valid","0079":"Group number is not valid or missing","0081":"Sub code is not valid or missing","0083":"Branch code not valid or missing","0085":"Coverage level not valid","0086":"Coverage status is missing","0089":"Cancellation reason (COBRA) not valid","0090":"Missing end date with cancellation reason listed","0091":"Missing end date with cancellation reason being sent","0092":"End date prior to start date","0093":"Cannot cancel record prior to start date in MetLife","0095":"Missing coverage type needed to enroll","0096":"Cannot enroll with a termination date","0097":"Effective date not valid in MetLife","0102":"Plan code is not valid with connection's structure",""}