from parsers.StopGameParser import StopGameParser
from parsers.IgromaniaParser import IgromaniaParser
from utils import MongodbService

stopGameParser = StopGameParser()
stopGameLast = StopGameParser.lastTitle

igromaniaParser = IgromaniaParser()
igromaniaLast = IgromaniaParser.lastTitle

igromaniaoutput = igromaniaParser.parce()
stopGameaoutput = stopGameParser.parce()

articles = igromaniaoutput + stopGameaoutput

storage = MongodbService.get_instance()

for article in articles:
    storage.save_data(article.toArray())

for data in storage.get_data():
         print(data)

storage.delete_all_data()