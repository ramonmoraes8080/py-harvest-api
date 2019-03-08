# Python's Client for Harvest API

## Build

`make build`

## Setup

`pip install git+https://github.com/vyscond/python-harvest.git@latest`

## Usage

### Core Client

Note that all the api objects will always return an "Response" object from
requests library

- Querying time entries

```
from harvest.auth import PersonalAccessAuthClient
from harvest.api import TimeEntry

client = PersonalAccessAuthClient(
    personal_token,
    account_id,
)


api = TimeEntry(client=self.client)
resp = api.get(params={
    'from': '1972-01-01',
    'to': '1972-01-02',
})
```

### Services (Common Routines)

### Module CLI

- Get all projects

```
python -m harvest.cli projects get all
```

- Get all tasks

```
python -m harvest.cli tasks get all
```

- Create time entry

```
python -m harvest.cli timeentry new [entry note] [date] [task id] [project id]
```

Examples:

- One project for today

```
python -m harvest.cli timeentry new "Hello world" today 9999999 8888888
```

- More than one project for today

```
python -m harvest.cli timeentry new "Hello world" today 9999999 8888888,7777777
```

## Tests

`make tests`

## License

MIT License

Copyright (c) 2019 Ramon Moraes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
