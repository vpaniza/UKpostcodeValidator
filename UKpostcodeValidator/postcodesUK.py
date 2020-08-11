##########################################################################
#
# Write a library that supports validating and formatting post codes for UK:
# 2, 3 or 4-character outward code, single space and 3-character inward code
#
# AA9A 9AA
# AA99 9AA
# AA9 9AA
# A9A 9AA
# A99 9AA
# A9 9AA
#
# Special cases are included in the regular expression
#
##########################################################################

import json
import requests
import sys
import re

postcodeRegEx = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA)\\s[0-9][A-Z]{2}|BFPO\\s[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[-][0-9]{4}|[A-Z]{2}\\s[0-9]{2}|GE\\sCX|GIR ?0A{2}|SAN\\sTA1)$"
INVALID_POSTCODE = -1
CONSOLE_PRINT = True #To turn logs ON change "False" to "True"


def getPostcodeData(postcode, optionalParam = None):
    if isPostcodeValid(postcode):
        try:
            if not optionalParam:
                response = requests.get("https://api.postcodes.io/postcodes/" + postcode)
            else:
                response = requests.get("https://api.postcodes.io/postcodes/" + postcode + optionalParam)
            
            dataJSON = json.loads(response.text)
            return dataJSON;
        except requests.exceptions.RequestException as error:
            if CONSOLE_PRINT: 
                print("Fetch failed: " + error)
            sys.exit(1)
    else:
        return INVALID_POSTCODE
    

def isPostcodeValid(postcode):
    if re.match(postcodeRegEx, postcode):
        if CONSOLE_PRINT:    
            print("Valid postcode")
        return True
    else:
        if CONSOLE_PRINT:
            print("Invalid format for postcode")
        return False
  

class postcodeData:
    def __init__(self, postcode, outward, inward, country, region, longitude, latitude):
        self.postcode    = postcode
        self.outward     = outward
        self.inward      = inward
        self.country     = country
        self.region      = region
        self.coordinates = [longitude, latitude]

    
def retrievedData(postcode):
    if not isPostcodeValid(postcode):
        return INVALID_POSTCODE
    else:
        retrievedData = getPostcodeData(postcode)
        postcodeObject = postcodeData(retrievedData["result"]["postcode"],
                                      retrievedData["result"]["outcode"],
                                      retrievedData["result"]["incode"],
                                      retrievedData["result"]["country"],
                                      retrievedData["result"]["region"],
                                      retrievedData["result"]["longitude"],
                                      retrievedData["result"]["latitude"])
        return postcodeObject