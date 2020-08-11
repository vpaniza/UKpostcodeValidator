import unittest
from postcodesUK import *

class TestPostcodeLibrary(unittest.TestCase):

    def testPostcodeValidation(self):
        self.assertTrue(isPostcodeValid("WA7 5QS"))
        self.assertTrue(isPostcodeValid("MK18 7AP"))
        self.assertTrue(isPostcodeValid("N1 8AL"))
        self.assertTrue(isPostcodeValid("PR8 6SQ"))
        self.assertTrue(isPostcodeValid("G3 6RH"))
        self.assertTrue(isPostcodeValid("SW1P 9TF"))
        self.assertTrue(isPostcodeValid("EH9 1TJ"))
        self.assertTrue(isPostcodeValid("VG-1120"))   #British Virgin Islands
        self.assertTrue(isPostcodeValid("AI-2640"))   #Anguilla 
        self.assertTrue(isPostcodeValid("FL 07"))     #Bermuda
        
        self.assertFalse(isPostcodeValid("N29 422SJ"))
        self.assertFalse(isPostcodeValid("CFDS 1UQ"))
        self.assertFalse(isPostcodeValid("CR2 20D"))
        self.assertFalse(isPostcodeValid("123 FA"))
        self.assertFalse(isPostcodeValid("ASHG 123"))
        self.assertFalse(isPostcodeValid("EH1 78J"))
        self.assertFalse(isPostcodeValid("AAAAAA"))
        self.assertFalse(isPostcodeValid("123 AAA"))
        
        
    def testFetchingMethod(self):
        outputCodeStatusValid = getPostcodeData("WA7 5QS")
        self.assertEqual(outputCodeStatusValid["status"], 200)
        
        outputCodeStatusInvalid = getPostcodeData("CR2 20D")
        self.assertEqual(outputCodeStatusInvalid, -1)
                         
        outputCodeWrongURL = getPostcodeData("NR9 4QJ", "nearby")
        self.assertEqual(outputCodeWrongURL["status"], 404)

    def testRetrievedData(self):
        outputData = retrievedData("SW1P 9TF")
        self.assertIsInstance(outputData.postcode, str)
        self.assertIsInstance(outputData.outward, str)
        self.assertIsInstance(outputData.inward, str)
        self.assertIsInstance(outputData.country, str)
        self.assertIsInstance(outputData.region, str)
        self.assertIsInstance(outputData.coordinates, list)
                         
        self.assertEqual(outputData.postcode, "SW1P 9TF")


if __name__ == '__main__':
    unittest.main()