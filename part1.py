# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809750        
  
# Date: 9th December 2020

print("\t\tStudent Version\n")

try:
    pass_credits = int(input("Please enter your credits at pass : "))
    defer_credits = int(input("Please enter your credit at defer : "))
    fail_credits = int(input("Please enter your credit at fail  : "))

    if (pass_credits == 120):
        print("Progress")
    elif (pass_credits == 100):
        print("Progress (module trailer)")
    elif (fail_credits <= 60):
        print("Do not progress – module retriever")
    else:
        print("Exclude")
except ValueError:
    print("Not a Valid Input")
