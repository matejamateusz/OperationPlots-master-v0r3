__author__ = 'mmateja'
__version__ = '0.2'

from Plotter.PlotLPC import PlotLPC
from Plotter.PlotCondition import PlotCondition
from PLOT.PLOT import PLOT, dateformat
from RetrieveData.RetrieveDataForPlot import RetrieveDataForPlot
from RetrieveData.Retriever import Retriever
import numpy as np
from datetime import datetime

basic_path = "/group/online/tfc/ROOT/"
startfillnumber = 3819
endfillnumber = 5000

# Start by retrieving data for LPC/lumi_LHCb files in the range of fillnumbers
print 'Retrieving data from lumi_LHCb between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
lumi = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(lumi)

xaxis = "fillnumber"  
yaxis = "max_lumi_lumi"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()):
        #plot=PLOT(value1, value2)
        plot=PLOT()
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakLumiFill.png")


xaxis = "time_date"  
yaxis = "max_lumi_lumi"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot=PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Peak Inst Luminosity (Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakLumiTime.png")


xaxis = "fillnumber"  
yaxis = "average_lumi_lumi"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Average Instantaneous Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Average Inst Luminosity (Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AvgLumiFill.png")

xaxis = "time_date"  
yaxis = "average_lumi_lumi"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot=PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Average Inst Luminosity (Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AvgLumiTime.png")

xaxis = "fillnumber"  
yaxis = "max_lumi_lumispec"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot=PLOT()
        plot.setTitle("LHCb Peak Specific Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (10^-23 Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakSpecLumiFill.png")


xaxis = "time_date"  
yaxis = "max_lumi_lumispec"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot=PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Specific Lumi at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Peak Inst Luminosity (10^-23 Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakSpecLumiTime.png")

xaxis = "time_sec"  
yaxis = "value_lumi_lumi"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot=PLOT()
        plot.setTitle("LHCb Inst Lumi at p-p 6.5 TeV in fill " + str((int(key1)))) 
        plot.setxlabel("Time [s]")
        plot.setylabel("Inst Luminosity (Hz/ub)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015InstLumiFill"+str(int(key1))+".png")

d = Retriever( basic_path, "Mu", startfillnumber, endfillnumber)
mu = d.retrieve("Condition") #LPC, CONDITION
r = RetrieveDataForPlot(mu)

xaxis = "fillnumber"  
yaxis = "max_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakMuFill.png")

xaxis = "time_date"  
yaxis = "max_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot = PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Peak Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakMuTime.png")

xaxis = "fillnumber"  
yaxis = "average_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Average Mu at p-p 6.5 TeV in 2015")
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Average Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AverageMuFill.png")

xaxis = "time_date"  
yaxis = "average_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot = PLOT()
        plot.setDate()
        plot.setTitle("LHCb Average Mu at p-p 6.5 TeV in 2015")
        plot.setxlabel("Date")
        plot.setylabel("Average Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AverageMuTime.png")

d = Retriever( basic_path, "Pileup", startfillnumber, endfillnumber)
pileup = d.retrieve("Condition") #LPC, CONDITION
r = RetrieveDataForPlot(pileup)
xaxis = "fillnumber"  
yaxis = "max_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Peak Pileup at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Pileup")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakPileupFill.png")

xaxis = "time_date"  
yaxis = "max_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot = PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Pileup at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Peak Pileup")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakPileupTime.png")

xaxis = "fillnumber"  
yaxis = "average_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Average Pileup at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Average Pileup")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AveragePileupFill.png")

xaxis = "time_date"  
yaxis = "average_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        value1 = dateformat(value1)
        plot = PLOT()
        plot.setDate()
        plot.setTitle("LHCb Average Pileup at p-p 6.5 TeV in 2015") 
        plot.setxlabel("Date")
        plot.setylabel("Average Pileup")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015AveragePileupTime.png")

print 'Retriving data from lumireg_LHCb between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "lumireg_LHCb", startfillnumber, endfillnumber)
lumireg = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(lumireg)

xaxis = "fillnumber"  
yaxis = "average_lumireg_zmean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Luminous Region Average Centroid in z at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("LumiRegion z avg centroid (mm)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015LumiRegionzFill.png")

xaxis = "fillnumber"  
yaxis = "average_lumireg_xmean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Luminous Region Average Centroid in x at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("LumiRegion x centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015LumiRegionxFill.png")

xaxis = "fillnumber"  
yaxis = "average_lumireg_ymean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Luminous Region Average Centroid in y at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("LumiRegion y avg centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015LumiRegionyFill.png")

print 'Retriving data from beam1_LHCb between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "beam1_LHCb", startfillnumber, endfillnumber)
beam1shape = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(beam1shape)

xaxis = "fillnumber"  
yaxis = "average_beam_xmean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Beam1 Average Centroid in x at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Beam1 x avg centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015Beam1xFill.png")

xaxis = "fillnumber"  
yaxis = "average_beam_ymean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Beam1 Average Centroid in y at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Beam1 y avg centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015Beam1yFill.png")

print 'Retriving data from beam2_LHCb between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "beam2_LHCb", startfillnumber, endfillnumber)
beam2shape = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(beam2shape)

xaxis = "fillnumber"  
yaxis = "average_beam_xmean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Beam2 Average Centroid in x at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Beam2 x avg centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015Beam2xFill.png")

xaxis = "fillnumber"  
yaxis = "average_beam_ymean"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
        plot = PLOT()
        plot.setTitle("LHCb Beam2 Average Centroid in y at p-p 6.5 TeV in 2015") 
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Beam2 y avg centroid (um)")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015Beam2yFill.png")


#Intensities, to fix how to superimpose two plots
print 'Retriving data from IntensityPerFill_beam1 between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "IntensityPerFill_beam1", startfillnumber, endfillnumber)
beam1intensities = d.retrieve("Condition") #LPC, CONDITION
r1 = RetrieveDataForPlot(beam1intensities)
print 'Retriving data from IntensityPerFill_beam2 between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "IntensityPerFill_beam2", startfillnumber, endfillnumber)
beam2intensities = d.retrieve("Condition") #LPC, CONDITION
r2 = RetrieveDataForPlot(beam2intensities)

xaxis = "fillnumber"  
yaxis = "max_condition"
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r1.retrieveData(xaxis,yaxis)
#Define plot outside loop to be able to plot many graphs together
plotm = PLOT()
plotm.setTitle("LHC Peak Beams Intensities in 2015") 
plotm.setxlabel("LHC Fillnumber")
plotm.setylabel("Peak Beams Intensities (10^8 p)")	
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
	plotm.draw(value1, value2, 'b', 5)
datax,datay = r2.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()):
	plotm.draw(value1, value2, 'r', 5)
        plotm.savefig("OUTPUTPLOTS/2015PeakBeamsIntensitiesFill.png")

#xaxis = "time_date"  
#yaxis = "max_condition"
#print 'Doing ' + yaxis + ' vs ' + xaxis
#datax,datay = r1.retrieveData(xaxis,yaxis)
#for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
#        value1 = dateformat(value1)
#        plot = PLOT()
#datax,datay = r2.retrieveData(xaxis,yaxis)
#for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): 
#        value1 = dateformat(value1)
#        plot = PLOT()
#        plot.setDate()
#        plot.setTitle("LHC Peak Beams Intensities in 2015") 
#        plot.setxlabel("Date")
#        plot.setylabel("Peak Beams Intensities (10^8 p)")
#	 plot.draw(value1, value2, 'b')
#        plot.savefig("OUTPUTPLOTS/2015PeakBeamsIntensitiesTime.png")

#plot.show()
#raw_input("Press enter to continue")

##################################################TEMPLATE PLOTTING################################################
# basic_path = "/home/mmateja/PycharmProjects/OperationPlots/"
# nameFileEnd = "Mu"
# xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
# yaxis = "max_lumi"    #MAX_LUMI, AVERAGE_LUMI, MAX_CONDITION, AVERAGE_CONDITION
# d=PlotLPC(xaxis, yaxis, basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
# #d=PlotCondition("time_year","value", basic_path, nameFileEnd)
# for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): #-key2
#         #value1 = [datetime.fromtimestamp(v1) for v1 in value1]
#         if key1 != key2 and ("time_sec" and "lumi" in xaxis and yaxis):
#             print "ERROR DIFFERENT KEYS!!!!!!!"
#         if "time_date" in xaxis and yaxis:
#             value1 = dateformat(value1)
#             plot=PLOT()
#             plot.setTitle(key1) #key1
#             plot.setDate()
#             plot.draw(value1, value2, 'b')
#         else:
#             plot=PLOT()
#             plot.setTitle(key1) #key1
#             plot.draw(value1, value2, 'b')
#
######################################################################################################################
