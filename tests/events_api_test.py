from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json


class OrganizationApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(OrganizationApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def event_latest_test(self):
        self.assertEquals(200, self.sdk.get_latest_events(self.org_uuid).status_code)

    def event_application_test(self):
        self.assertEquals(200, self.sdk.get_latest_application_creation(self.org_uuid).status_code)

    def event_server_test(self):
        self.assertEquals(200, self.sdk.get_latest_server_creation(self.org_uuid).status_code)

    def event_trace_test(self):
        self.assertEquals(200, self.sdk.get_latest_traces_received(self.org_uuid).status_code)

