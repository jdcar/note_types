from pymarc import MARCReader
import re

with open('H:\\Serial notes\\Consoles for coding\\mfhds_for_jamie mrc.mrc', 'rb') as fh:

    reader = MARCReader(fh)    
    for record in reader:
        
        issueslower = re.sub(r" Issues", r" issues", str(record["852"]))
        
        removedoublespaces = re.sub(r"  ", r" ", issueslower)
        
        holdingID = re.sub(r"(=001  )(.+)", r"\2", str(record["001"]))
        
        if re.match("(.+)(\$[xz])(Recent|Unbound)(.+)", removedoublespaces):
                
            if re.match("(.+)(\$[xz])(Recent issues|Unbound issues|Recent volumes|Unbound volumes|Recent and unbound issues)($)", removedoublespaces):
                 
                 #=852  1\$bllper-nc$h410$iB455p$t1$x(Contin; Marked by v.)$zCopy 1 has v.1(1975) to date$zRecent issues
                   
                 removenote = re.sub(r"(.+)(\$[xz])(Recent issues|Unbound issues|Recent volumes|Unbound volumes|Recent and unbound issues)($)", r"\1", removedoublespaces)
                     
                 print ("A|", holdingID,"|" , str(record["852"]), "|" , removenote, sep="")
                   
            elif re.match("(.+)(\$[xz])(Recent issues|Unbound issues|Recent volumes|Unbound volumes|Recent and unbound issues)(\$[xz])(.+)", removedoublespaces):   
                     
                #=852  1\$bstx$kQ.$h809.05$iNEB1$t1$x(Marked by v.)$zRecent issues$zFor earlier volumes see Q.809.05NEB
         
                removenote1 = re.sub(r"(.+)(\$[xz])(Recent issues|Unbound issues|Recent volumes|Unbound volumes|Recent and unbound issues)(\$[xz])(.+)", r"\1\4\5", removedoublespaces)
                     
                print ("B|", holdingID,"|", str(record["852"]), "|", removenote1, sep="")
                   
            elif re.match("(.+)(\$[xz])(Recent issues in|Unbound issues in|Recent issues held|Unbound issues held|Recent volumes in|Unbound volumes in|Recent volumes held|Unbound volumes held|Recent and unbound issues held|Recent and unbound issues in)(.+)(\$[xz])(.+)", removedoublespaces):
                     
                #FIX THIS ONE     
                #=852  1\$bstx$kQ.$h809.05$iNEB1$t1$x(Marked by v.)$zRecent issues in Literature andLanguages Library$zFor earlier volumes see Q.809.05NEB
                     
                removenote2 = re.sub(r"(.+)(\$[xz])(Recent issues in|Unbound issues in|Recent issues held|Unbound issues held|Recent volumes in|Unbound volumes in|Recent volumes held|Unbound volumes held|Recent and unbound issues held|Recent and unbound issues in)(.+)(\$[xz])(.+)", r"\1\5\6", removedoublespaces)
                     
                print("C|", holdingID,"|", str(record["852"]), "|", removenote2, sep="")
                 
            elif re.match("(.+)(\$[xz])(Recent issues in|Unbound issues in|Recent issues held|Unbound issues held|Recent volumes in|Unbound volumes in|Recent volumes held|Unbound volumes held|Recent and unbound issues held|Recent and unbound issues in|Latest vols\. in|Latest vols\. held)((?:.(?!\$))+$)", removedoublespaces):
                  
                #=852  1\$bstx$kQ.$h809.05$iNEB1$t1$x(Marked by v.)$zRecent issues in Literature andLanguages Library
                  
                removenote3 = re.sub("(.+)(\$[xz])(Recent issues in|Unbound issues in|Recent issues held|Unbound issues held|Recent volumes in|Unbound volumes in|Recent volumes held|Unbound volumes held|Recent and unbound issues held|Recent and unbound issues in|Latest vols\. in|Latest vols\. held)((?:.(?!\$))+$)", r"\1", removedoublespaces)
                  
                print("D|", holdingID,"|", str(record["852"]), "|", removenote3, sep="")
                 
            else:
             
                print("Else|", holdingID, "|", str(record["852"]), sep="")
                
                
                