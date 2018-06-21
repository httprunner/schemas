# HttpRunner Schemas

Repository of all schemas for JSON structures compatible with HttpRunner.

## Versions

- [v0.0.1](json/v1.json)

## Usage

All the schemas in this repository are valid JSON Schemas, compliant with the [JSON-Schema, Draft 4][JSON-Schema].

As such, they can be used with [jsonschema][jsonschema] to validate arbitrary JSON blobs, as show below:

```python
import requests  # make sure this is installed
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = requests.get('http://schema.httprunner.org/json/v1.json').json()

test_input = {}  # Whatever needs to be validated.

try:
    validate(test_input, schema)
except ValidationError:
    print 'It is not a valid collection!'
else:
    print 'It is a valid collection!'
```

[JSON-Schema]: http://json-schema.org/documentation.html
[jsonschema]: https://github.com/Julian/jsonschema