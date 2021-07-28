from parsers.StopGameParser import StopGameParser
from parsers.IgromaniaParser import IgromaniaParser

stopGameParser = StopGameParser()
stopGameLast = StopGameParser.lastTitle
igromaniaParser = IgromaniaParser()
igromaniaLast = IgromaniaParser.lastTitle

igromaniaoutput = igromaniaParser.parce()
stopGameaoutput = stopGameParser.parce()
for out in igromaniaoutput:
    print(out.get_info())