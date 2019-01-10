'''
Created on Dec 4, 2018

@author: jdc6
'''

from pymarc import MARCReader
import re

with open('H:\\Serial notes\\Consoles for coding\\mfhds_for_jamie mrc.mrc', 'rb') as fh:

    reader = MARCReader(fh)    
    for record in reader:
        
        holdingID = re.sub(r"(=001  )(.+)", r"\2", str(record["001"]))

        if re.match("(.+)(\$[xz])(.+)(UIUC Online Collection)", str(record["852"])):
            
            p1 = re.sub("(.+)(\$[xz])(.+)(UIUC Online Collection)", r"\1|\2\3\4|", str(record["852"]))
        
            print(holdingID, "|", p1, sep="")
            
        elif re.match("(.+)(\$[xz])(.+)(UIUC Online Collection)(.+)", str(record["852"])):
            
            p2 = re.sub("(.+)(\$[xz])(.+)(UIUC Online Collection)", r"\1|\2\3\4|\5", str(record["852"]))
            
            print(holdingID, "|", p2, sep="")