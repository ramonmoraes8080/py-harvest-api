import json
import logging
from datetime import datetime
from datetime import timedelta
from auth import PersonalAccessAuthClient
from api import TimeEntry


class BaseService(object):

    def __init__(self, personal_token=None, account_id=None):
        self.client = PersonalAccessAuthClient(
            personal_token,
            account_id,
        )


class TimeRangeBaseService(BaseService):

    def __init__(self, personal_token=None, account_id=None):
        super(TimeRangeBaseService, self).__init__(personal_token, account_id)
        self.today = datetime.now()

    def get_date_range(self):
        pass

    def all(self, page=1):
        date_range = self.get_date_range()
        logging.debug(
            'Quering from {} to {}'.format(date_range[0], date_range[1])
        )
        api = TimeEntry(client=self.client)
        resp = api.get(params={
            'from': date_range[0],
            'to': date_range[1],
        })
        logging.debug('Encoding = {}'.format(resp.encoding))
        return resp.json()

    def blanks(self):
        resp = self.all()
        empty_time_entries = []
        for entry in resp['time_entries']:
            if not entry['notes']:
                empty_time_entries.append(entry)
        resp['time_entries'] = empty_time_entries
        return resp


class Today(TimeRangeBaseService):

    def get_date_range(self):
        self.date_from = today.strftime('%Y-%m-%d')
        self.date_to = today.strftime('%Y-%m-%d')
        return (self.date_from, self.date_to)


class CurrentWeek(TimeRangeBaseService):

    def get_date_range(self):
        self.date_from = (self.today - timedelta(days=self.today.weekday()))
        self.date_to = (self.date_from + timedelta(days=6)).strftime('%Y-%m-%d')
        self.date_from = self.date_from.strftime('%Y-%m-%d')
        return (self.date_from, self.date_to)


class PreviousWeek(TimeRangeBaseService):

    def get_date_range(self):
        # Today from last week
        self.today = self.today - timedelta(days=(6 - self.today.weekday()))
        self.date_from = (self.today - timedelta(days=self.today.weekday()))
        self.date_to = (self.date_from + timedelta(days=6)).strftime('%Y-%m-%d')
        self.date_from = self.date_from.strftime('%Y-%m-%d')
        return (self.date_from, self.date_to)

