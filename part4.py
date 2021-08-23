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
            loop_count+=1
    except ValueError:
        print("Integer required\n")

#Creating the function "checkTotalValidity()" to validate the total of the inputs
def checkTotalValidity():
    global loop_count
    total = int(pass_credits) + int(defer_credits) + int(fail_credits)
    if (total > 120 or total < 120):
        print("Total incorrect\n")
    else:
        loop_count+=1

#Creating the function "displayHorizontalHistogram()" to display horizontal histogram
def displayHorizontalHistogram():
    print("\t\tHorizontal Histogram\n")
    for progress_level, count in count_dict.items():
        if (progress_level != "Total"):
            print(f"{progress_level:9} {count:1}",":","*"*count)
    print("\r")
    print(count_dict["Total"],"outcomes in total.")

#Creating the function "displayVerticalHistogram()" to display vertical histogram
def displayVerticalHistogram():
    print("\t\tVertical Histogram\n")
    print("|Progress",count_dict["Progress"],"\t|Trailing",count_dict["Trailer"],"\t|Retriever",count_dict["Retriever"],"\t|Excluded",count_dict["Excluded"])
    print("\r")
    max_rows = max(count_dict["Progress"],count_dict["Trailer"],count_dict["Retriever"],count_dict["Excluded"])
    for row in range(max_rows):
        for progress_level, count in count_dict.items():
            if (progress_level != "Total"):
                if (count > row):
                    print("     *",end = "\t\t")
                else:
                    print("      ",end = "\t\t")
        print("\r")
    print("\r")
    print(count_dict["Total"],"outcomes in total.")
    

print("\t\tStaff Version with Histogram\n")
 
valid_credits = [0,20,40,60,80,100,120]   #Creating a list including all the valid inputs
count_dict = {"Total" : 0, "Progress" : 0, "Trailer" : 0, "Retriever" : 0, "Excluded" : 0}  #Creating a dictionary called "count_dict" to store the number of total outcomes and number of each progression outcomes seperately


while True:
    loop_count = 0   #Initializing the variable "loop_count" to control inner loops
    
    while (loop_count < 1):   #Initializing inside loop 1 to iterate until user enters valid pass_credits
        pass_credits = input("Please enter your credits at pass : ")
        checkInputValidity(pass_credits)   
        
    while (loop_count < 2):   #Initializing inside loop 2 to iterate until user enters valid defer_credits
        defer_credits = input("Please enter your credit at defer : ")
        checkInputValidity(defer_credits)   
        
    while (loop_count < 3):   #Initializing inside loop 3 to iterate until user enters valid fail_credits
        fail_credits = input("Please enter your credit at fail  : ")
        checkInputValidity(fail_credits)
  
    checkTotalValidity()

    #Inititalizing a conditonal statement to iterate the loop from the begining if input total is not correct
    if (loop_count < 4):
        continue
t
    if (int(pass_credits) == 120):
        print("Progress")
        count_dict["Progress"] += 1
    elif (int(pass_credits) == 100):
        print("Progress (module trailer)")
        count_dict["Trailer"] += 1
    elif (int(fail_credits) <= 60):
        print("Do not progress – module retriever")
        count_dict["Retriever"] += 1
    else:
        print("Exclude")
        count_dict["Excluded"] += 1
    count_dict["Total"] += 1
    
    user_input = ''  #Creating a varible with an empty string to store user's decision to enter a another record or not in each turn

    #Intializing another inside loop to iterate until the user enters 'y' or 'q' into the variable "user_input"
    while (user_input.lower() != 'y' and user_input.lower() != 'q'):
        print("\nWould you like to enter another set of data?")
        user_input = input("Enter 'y' for yes or 'q' to quit and view results : ")

    #Inititalizing a conditonal statement to iterate the loop from the begining if variable "user_input" equals to 'y'
    if (user_input.lower() == "y"):
        print("\r")
        continue

    break

print("\r")

displayHorizontalHistogram()
print("\r")

displayVerticalHistogram()
