# Seshat API

This is the Python binding for the Seshat API. The Seshat API is a RESTful API
that allows you to interact with the Seshat database. The Seshat database is a
database of historical and archaeological data. The Seshat API allows you to
query the database and retrieve data in a structured format.

## Installation

To install the Seshat API, you can use pip:

```bash
pip install seshat
```

## Usage

To use the Seshat API, you need to create a `SeshatAPI` client object and use
it to interact with the database. Here is an example of how to set up a client:

```python
from seshat_api import SeshatAPI

# Set up a client
client = SeshatAPI(username="<USERNAME>", password="<TEST>")
```

Here is an example of how to use the API to retrieve data from the database:

```python
# Get all the polities in the database
from seshat_api.core import Polities

polities = Polities(client)

# Iterate through the polities
for polity in polities:
    print(polity.id, polity.name)
```

## Documentation

For more information on how to use the Seshat API, please refer to the
[documentation](docs).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.
