# Treblle Flask SDK

This is an API to test the Flask SDK for Treblle.

## REQUIREMENTS

A `treblle.json` file has to be present in the root directory of the project. This file should contain a dictionary like the example below:

```
{
    "TREBLLE_API_KEY": "API key goes here",
    "TREBLLE_PROJECT_ID": "Project ID goes here",
    "TREBLLE_HIDDEN_KEYS": ["hidden", "keys", "goes", "here"]
}
```

Once that is out of the way, the next step is to import the Treblle class and pass the `app` instance:

```py
from treblle-flask import Treblle
...
Treblle(app)
...
```

That is all it takes to set up the Treblle-flask SDK.

Enjoy!