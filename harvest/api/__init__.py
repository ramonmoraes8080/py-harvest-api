import requests
import logging


class Endpoint(object):

    def __init__(self, client):
        self.client = client

    def get_url(self):
        return '{}{}'.format(
            self.client.get_base_api_url(),
            self.path,
        )

    def get(self, *args, **kwargs):
        url = self.get_url()
        params = kwargs
        headers = self.client.get_headers()
        logging.debug('HTTP - GET - Request - URL {}'.format(url))
        logging.debug('HTTP - GET - Request - Params '.format(params))
        logging.debug('HTTP - GET - Request - Headers {}'.format(headers))
        resp = requests.get(
            url=url,
            headers=headers,
            params=params,
        )
        logging.debug('HTTP - GET - Response - status code - {}'.format(resp.status_code))
        logging.debug('HTTP - GET - Response - content - {}'.format(resp.content))
        return resp

    def post(self, *args, **kwargs):
        url = self.get_url()
        params = kwargs.get('params', {})
        data = kwargs.get('data', {})
        headers = self.client.get_headers()
        logging.debug('HTTP - POST - URL {}'.format(url))
        logging.debug('HTTP - POST - Params '.format(params))
        logging.debug('HTTP - POST - Headers {}'.format(headers))
        resp = requests.post(
            url=url,
            headers=headers,
            params=params,
            data=data,
        )
        logging.debug('HTTP - POST - Response {}'.format(resp.content))
        return resp


class Projects(Endpoint):

    path = '/projects'


class Tasks(Endpoint):

    path = '/tasks'

    '''
    GET:
        is_active (boolean):
            Pass true to only return active tasks and false to return inactive
            tasks.
        updated_since (datetime):
            Only return tasks that have been updated since the given date and
            time.
        page (integer):
            The page number to use in pagination. For instance, if you make a
            list request and receive 100 records, your subsequent call can
            include page=2 to retrieve the next page of the list. (Default: 1)
        per_page (integer):
            The number of records to return per page. Can range between 1 and
            100. (Default: 100)

    POST:
    '''

class TimeEntry(Endpoint):

    path = '/time_entries'

    '''
    HTTP Methods:
        GET:
            user_id (integer):
                Only return time entries belonging to the user with the given ID.
            client_id (integer):
                Only return time entries belonging to the client with the given ID.
            project_id (integer):
                Only return time entries belonging to the project with the given ID.
            is_billed (str):
                Pass "true" to only return time entries that have been invoiced
                and "false" to return time entries that have not been invoiced.
            is_running (str):
                Pass "true" to only return running time entries and "false" to
                return non-running time entries.
            updated_since (datetime str):
                Only return time entries that have been updated since the given
                date and time.
            from (date str):
                Only return time entries with a spent_date on or after the
                given date.
            to (date str):
                Only return time entries with a spent_date on or before the
                given date.
            page (integer):
                The page number to use in pagination. For instance, if you make
                a list request and receive 100 records, your subsequent call
                can include page=2 to retrieve the next page of the list.
                (Default: 1)
            per_page (integer):
                The number of records to return per page. Can range between
                1 and 100. (Default: 100)
        POST:
            user_id (integer / optional):
                The ID of the user to associate with the time entry. Defaults
                to the currently authenticated user's ID.
            project_id  (integer / required):
                The ID of the project to associate with the time entry.
            task_id (integer / required):
                The ID of the task to associate with the time entry.
            spent_date (date / required):
                The ISO 8601 formatted date the time entry was spent.
            hours (decimal / optional):
                The current amount of time tracked. If provided, the time entry
                will be created with the specified hours and is_running will be
                set to false. If not provided, hours will be set to 0.0 and
                is_running will be set to true.
            notes (string / optional):
                Any notes to be associated with the time entry.
            external_reference (object / optional):
                An object containing the id, group_id, and permalink of the
                external reference.
    '''
