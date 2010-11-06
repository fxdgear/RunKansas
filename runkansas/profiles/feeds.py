from runkansas.utils.icalendar import ICalendarFeed
from runkansas.race.models import Event

import datetime

class MyRaceCalendar(ICalendarFeed):

    def __init__(self, events):
	    self.events = events

    def items(self):
        return self.events

    def item_uid(self, item):
        return str(item.id)
	
    def item_start(self, item):
        return item.date

    def item_end(self, item):
	    return item.date + datetime.timedelta(hours=1)
		
    def item_summary(self, item):
        return item.__unicode__()
