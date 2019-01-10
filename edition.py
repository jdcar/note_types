'''
Created on Dec 5, 2018

@author: jdc6
'''

from pymarc import MARCReader
import re

with open('H:\\Serial notes\\Consoles for coding\\mfhds_for_jamie mrc.mrc', 'rb') as fh:

    reader = MARCReader(fh)    
    for record in reader:
        
        holdingID = re.sub(r"(=001  )(.+)", r"\2", str(record["001"]))
        
        if re.match("(.+)(\$[xz])(\S+)( edition.+)", str(record["852"])):
                
            print(holdingID, "|", str(record["852"]), sep="")