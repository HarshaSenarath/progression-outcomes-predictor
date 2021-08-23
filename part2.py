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
    total = int(pass_credits) + int(defer_credits) + int(fail_credits)
    if (total > 120 or total < 120):
        print("Total incorrect\n")
    else:
        loop_count += 1


print("\t\tStudent Version (Validation)\n")
        
valid_credits = [0,20,40,60,80,100,120]   #Creating a list including all the valid inputs  

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

    if (int(pass_credits) == 120):
        print("Progress")
    elif (int(pass_credits) == 100):
        print("Progress (module trailer)")
    elif (int(fail_credits) <= 60):
        print("Do not progress – module retriever")
    else:
        print("Exclude")

    break
