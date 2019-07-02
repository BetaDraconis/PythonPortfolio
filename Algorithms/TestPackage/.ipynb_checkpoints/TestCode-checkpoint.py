def testFunc(testVals, testResults, func):
    import numpy as np
    import pandas as pd
    import sys
    longResults = ''
    passCount = 0
    failCount = 0
    for i in range (len(testVals)):
        try:
            if type(testResults[i]) == pd.core.frame.DataFrame:
                pd.testing.assert_frame_equal(func(testVals[i]), testResults[i], check_dtype = False)
            elif type(testResults[i]) == np.ndarray:
                assert((func(testVals[i]) == testResults[i]).all() == True)
            else:
                assert(func(testVals[i]) == testResults[i])
            longResults+=("Test {} passes. \n".format(i+1))
            passCount+=1
        except Exception:
            etype, value, tb = sys.exc_info()
            longResults+=("Test {} fails due to {}. \n".format(i+1, etype))
            failCount+=1
    results = Results(len(testVals), passCount, failCount, longResults)
    return results

class Results:
    def __init__(self, testTotal, testPass, testFail, longResults):
        self.testTotal =testTotal
        self.testPass = testPass
        self.testFail = testFail
        self.longResults = longResults
        
    def getTestTotal(self):
        return self.testTotal
    
    def getTestFail(self):
        return self.testFail
    
    def getTestPass(self):
        return self.testPass
    
    def getTestResults(self):
        return "{} tests run, {} test passes, {} test fails.".format(self.testTotal, self.testPass, self.testFail)
    
    def getLongResults(self):
        return self.longResults