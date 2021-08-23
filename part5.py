# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809750        
  
# Date: 9th December 2020

#Creating the function "checkInputValidity(value)" to validate the inputs
def checkInputValidity(value):
    global loop_count
    try:
        value = int(value)
        if (value not in valid_credits):
            print("Out of range\n")
        else:
            loop_count += 1
    except ValueError:
        print("Integer required\n")

#Creating the function "checkTotalValidity()" to validate the total of the inputs
def checkTotalValidity():
    global loop_count
    total = pass_credits + defer_credits + fail_credits
    if (total > 120 or total < 120):
        print("Total incorrect\n")
    else:
        loop_count += 1

#Creating the function "displayHorizontalHistogram()" to display horizontal histogram
def displayHorizontalHistogram():
    print("\t\tHorizontal Histogram\n")
    for progress_level, count in count_dict.items():
        if (progress_level != "Total"):
            print(f"{progress_level:9} {count:1}",":","*"*count)
    print("\r")
    print(count_dict["Total"],"outcomes in total.")


print("\t\tAlternative Staff Version\n")   

    
valid_credits = [0,20,40,60,80,100,120]   #Creating a list including all the valid inputs
count_dict = {"Total" : 0, "Progress" : 0, "Trailer" : 0, "Retriever" : 0, "Excluded" : 0}   #Creating a dictionary called "count_dict" to store the number of total outcomes and number of each progression outcomes seperately
data_list = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]   #Creating a two-dimensional list where each of the inner lists are in the form of [pass_credits,defer_credits,fail_credits]

#Accessing each element inside the data_list through a loop
for i in data_list:
    loop_count = 0    #Creating the variable 'loop_count' to control the loop
    
    pass_credits = i[0]    #Assigning the value in 0th index of i in to the variable pass_credits
    checkInputValidity(pass_credits)    
    if (loop_count < 1):   
        break
    
    defer_credits = i[1]    #Assigning the value in 1st index of i in to the variable defer_credits
    checkInputValidity(defer_credits)    
    if (loop_count < 2):   
        break
    
    fail_credits = i[2]    #Assigning the value in 2nd index of i in to the variable fail_credits
    checkInputValidity(fail_credits)    
    if (loop_count < 3):   
        break
    
    checkTotalValidity()
    if (loop_count < 4):   
        break

    #Using conditional statements to determine the progresssion level and display it
    if (pass_credits == 120):
        print("Progress")
        count_dict["Progress"] += 1
    elif (pass_credits == 100):
        print("Progress (module trailer)")
        count_dict["Trailer"] += 1
    elif (fail_credits <= 60):
        print("Do not progress – module retriever")
        count_dict["Retriever"] += 1
    else:
        print("Exclude")
        count_dict["Excluded"] += 1
    count_dict["Total"] += 1

print("\r")

displayHorizontalHistogram()
