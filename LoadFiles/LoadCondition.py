__author__ = 'mmateja'

from IO.ConditionData import ConditionData
import numpy as np
class LoadCondition():

    def __init__(self,fillNumbers, basic_path, nameFileEnd):

        self.fillNumbers=fillNumbers
        self.data=ConditionData()
        self.basic_path = basic_path
        self.nameFileEnd = nameFileEnd

    def load(self):
        fillnumber=self.fillNumbers.getFillNumbers()

        self.data.takeFillNumbers(fillnumber)
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):

            # Create the proper path
            if self.nameFileEnd is 'Mu' or self.nameFileEnd is 'Pileup':
                path = self.basic_path + "RunParameters/%d_%s.txt" %(fillnumber[z], self.nameFileEnd) 
            elif self.nameFileEnd is 'IntensityPerFill_beam1' or self.nameFileEnd is 'IntensityPerFill_beam2':
                path = self.basic_path + "IntensitiesPerFill/%d_%s.txt" %(fillnumber[z], self.nameFileEnd)
            elif 'AnalysisTool' in self.nameFileEnd:
                path = "/scratch/everyone/LHCbAnalysisTool/%d_%s.txt" %(fillnumber[z], self.nameFileEnd)

            # Get the content of the data
            try:
                d=np.genfromtxt(path, delimiter=' ',dtype=None, names=['time_year','time_month','time_day','time_hour','time_minute','time_sec','value']).T
            except IOError:
                pass
            except ValueError:
                pass

            self.data.load(fillnumber[z], d)



