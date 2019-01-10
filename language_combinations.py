'''
Created on Dec 10, 2018

@author: jdc6
'''

firstWord = ["Bound", 
             "Recent",
             "Unbound", 
             "Previous", 
             "Last", 
             "Latest", 
             "Recent and unbound", 
             "Unbound and recent", 
             "Current", 
             "Later", 
             "Last \\\d+ years and recent issues", 
             "Previous \\\d+ years and recent issues", 
             "Last \\\d+",
             "Recent \\\d+",
             "Previous \\\d+",
             "Next",
             "Next to last",
             "Early",
             "Earlier",
             "Earliest",
             "New",
             "Newer",
             "Most recent"
            ]

secondWord = [" editions",
              " issues",
              " volumes",
              " years",
              " vols\\\.",
              " eds\\\.",
              " yrs\\\.",
              " vol\\\.",
              " no\\\.",
              " nos\\\.",
              " ed\\\.",
              " yr\\\.",
              " edition",
              " issue",
              " volume",
              " year",
              " vol",
              " vols",
              " ed",
              " eds",
              " yr",
              " yrs",
              " nos",
              " no",
              " "]

thirdWord = ["",
             " in ",
             " at ",
             " located in",
             " held "]


for x in firstWord:
    
    for y in secondWord:
        
        for z in thirdWord:
    #Don't forget to remove double spaces after print!!!
    #Also the last |
    #Uppercase as well, change \\D+ back to \\d+
            print(x, y, z, "|", sep="", end="")