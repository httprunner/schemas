# HttpRunner Schemas

[![LICENSE](MIT-LICENCE-Logo.svg)](https://github.com/HttpRunner/schemas/blob/master/LICENSE) [![Build Status](https://travis-ci.org/HttpRunner/schemas.svg?branch=master)](https://travis-ci.org/HttpRunner/schemas)

Repository of all schemas for JSON structures compatible with HttpRunner.

## Versions

- [v1](json/v1.json)

## Usage

All the schemas in this repository are valid JSON Schemas, compliant with the [JSON-Schema, Draft 6][JSON-Schema].

As such, they can be used with [jsonschema][jsonschema] to validate arbitrary JSON blobs, as show below:

```python
import json
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = requests.get('http://schema.httprunner.org/json/v1.json').json()

json_path = "tests/data/demo_validate_pass.json"  # Whatever needs to be validated.
with open(json_path) as f:
    test_input = json.load(f)

try:
    validate(test_input, schema)
except ValidationError:
    print('It is not a valid collection!')
else:
    print('It is a valid collection!')
```

[JSON-Schema]: http://json-schema.org/documentation.html
[jsonschema]: https://github.com/Julian/jsonschema