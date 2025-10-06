# FILE NAME - phishing_email_detector.py

# NAME: Kandise Perkins
# DATE: October 6, 2025
# BRIEF DESCRIPTION:  Program that can identify phishing emails based on common red flags and will output risk level



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    phishing_email_detector()
def phishing_email_detector():
    prompt = input('Enter email in subject line: ')
    prompt_lower = prompt.lower() 
    print('')
    print('SECURITY ASSESSMENT:')
#if
    if "urgent" in prompt_lower or "immediate action required" in prompt_lower:
        print('HIGH RISK: Possible phishing attempt.')
    elif "win" in prompt_lower or "free" in prompt_lower:
        print('MEDIUM RISK: Suspicious offer detected.')
    elif "password reset" in prompt_lower:
        print('LOW RISK: Verify legitimacy with sender.')
    else:
        print('No phishing indictators detected.')

    print('------------------------')
    print(f'Analyzed subject:"{prompt}"')



main()
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural?
using in was simple and makes sense I just need to work on getting the formatting correct. 






'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[x] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[x] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
