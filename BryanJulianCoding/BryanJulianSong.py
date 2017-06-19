#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(95)

def SectionA(startMeasure, endMeasure):
  fitMedia(HIPHOP_BASSSUB_007, 1, startMeasure, endMeasure)
  fitMedia(HIPHOP_DUSTYGROOVE_003, 2, startMeasure, endMeasure)
  fitMedia(HIPHOP_HIHAT_ROLL_002, 3, startMeasure, endMeasure)
  fitMedia(HIPHOP_STOMP_BEAT_008, 4, startMeasure, endMeasure)
  setEffect(1, VOLUME, GAIN, -50, startMeasure, 0, endMeasure)
  
def SectionB(startMeasure, endMeasure):
  fitMedia(HIPHOP_BASSSUB_003, 1, startMeasure, endMeasure)
  fitMedia(HIPHOP_FUNKBEAT_005, 2, startMeasure, endMeasure)
  setEffect(1, VOLUME, GAIN, -20, startMeasure, 0, endMeasure)
  fitMedia(HIPHOP_TRAP_BEAT_004, 4, startMeasure, endMeasure)
  
def SectionC(startMeasure, endMeasure):
  fitMedia(HIPHOP_VOCALHIT_001, 2, startMeasure, endMeasure)
  fitMedia(HIPHOP_TRAP_BEAT_001, 4, startMeasure, endMeasure)
  
def SectionD(startMeasure, endMeasure):
  fitMedia(Y06_HI_HATS, 1, startMeasure, endMeasure)
  fitMedia(Y31_ORGAN_2, 3, startMeasure, endMeasure)
  fitMedia(HIPHOP_TRAP_BEAT_003, 4, startMeasure, endMeasure)
  setEffect(3, FILTER, FILTER_FREQ, 400, startMeasure, 1000, endMeasure)

def myBeat(startMeasure, endMeasure):
  beatPattern = "0+-+-++--+-0+-+-++--+-0+-+-++--+-0"
  makeBeat(HIPHOP_STOMP_BEAT_PART_005, 6, startMeasure, beatPattern)
  
# ABABCCDD Pattern.
SectionA(1, 9)
SectionB(9, 17)
SectionA(17, 25)
SectionB(25, 33)
SectionC(33, 39)
SectionC(39, 45)
SectionD(45, 51)
SectionD(51, 57)
myBeat(1, 57)
for measure in range(1, 9):
  fitMedia(HIPHOP_DUSTYBASSLINE_001, 5, measure, measure + 1)
for measure in range(17, 25):
  fitMedia(HIPHOP_DUSTYBASSLINE_001, 5, measure, measure + 1)
  
finish()
