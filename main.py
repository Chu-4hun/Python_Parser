from parsers.StopGameParser import StopGameParser

stopGameParser = StopGameParser()
output = stopGameParser.parce()
for out in output:
    print(out.get_info())