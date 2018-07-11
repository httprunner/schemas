import json
import os
import unittest

import requests

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestMain(unittest.TestCase):

    def setUp(self):
        # schema = requests.get('http://schema.httprunner.org/json/v1.json').json()
        with open("json/v1.json") as f:
            self.schema = json.load(f)

    def test_validate(self):
        json_path = os.path.join(os.path.dirname(__file__), "data", "demo_validate_pass.json")
        with open(json_path) as f:
            test_input = json.load(f)

        validate(test_input, self.schema)
