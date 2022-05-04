# PlanIT-Testing-SDET-Preliminary-Assessment
Repository for the 2 code challenges and automation test cases

PREREQUISITES:
 * Python is installed and is in the user root directory (for Windows)
 * Python Pandas is installed (if not, run the command: 'pip install pandas' in the terminal)
 
 Hello hiring manager/technical manager,

I chose Challenge #2 and #7
For challenge #2, this is pretty straightforward as it does not have much flexibility compared to the the other challenges.
For challenge #7, since there are some room for flexibility, this would require a terminal input via CMD for the CSV files. I did this because it would be easier for me rather than having another user input for the CSV file. Also allows better testing with different CSV files IMO. Additionally, I have left two datasets within here. One is a simple one with 17 entries, the other is around 24 thousand entries just to test scalability. Lastly, there are limitations to when testing for Challenge #7, this is case sensitive and the lookup value must be exact as this is one of the limitations of using Python Pandas library.