# Treblle Flask SDK

This is an API to test the Flask SDK for Treblle.

## Requirements

### Installation

Install the necessary packages

`pip install -r requirements.txt`

### Setup

A `treblle.json` file has to be present in the root directory of the project. This file should contain a dictionary like the example below:

```
{
    "TREBLLE_API_KEY": "API key goes here",
    "TREBLLE_PROJECT_ID": "Project ID goes here",
    "TREBLLE_HIDDEN_KEYS": ["hidden", "keys", "goes", "here"]
}
```

> Don't forget to add `treblle.json` to .gitignore file

Once that is out of the way, the next step is to import the Treblle class and pass the `app` instance:

```py
from treblle-flask import Treblle
...
Treblle(app)
...
```

That is all it takes to set up the Treblle-flask SDK.

### Run the server

Two ways to run the server:

1. `flask --app main run`

To run in debug mode:

2. `flask --app main --debug run`

### Test files

There are also test files available, to run tests:

1. `cd treblle_flask`
2. `cd test`
3. run: `pytest` or `pytest -v` (to view test cases)

> Tip: Ensure treblle.json is present in project directory and test directory (just for testing purpose, don't forget to add to .gitignore) ;-)

## Available Endpoints

- Create user --> `http://127.0.0.1:5000/signup`
- Login --> `http://127.0.0.1:5000/signin`
- All articles --> `http://127.0.0.1:5000/` , { Bearer 'token' }
- Create article --> `http://127.0.0.1:5000/` , { Bearer 'token' }
- Fetch article --> `http://127.0.0.1:5000/:uuid` , { Bearer 'token' }
- Update article --> `http://127.0.0.1:5000/:uuid` , { Bearer 'token' }
- Delete article --> `http://127.0.0.1:5000/:uuid` , { Bearer 'token' }

Enjoy!
