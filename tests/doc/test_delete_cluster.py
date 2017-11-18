import os
import tempfile
import json

curfilePath = os.path.abspath(__file__)
scriptDir = os.path.abspath(os.path.join(curfilePath, os.pardir, os.pardir, os.pardir, 'docs', 'example_scripts'))

from unittest import TestCase
from mock import Mock, MagicMock
import mock

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
    def raise_for_status(self):
        return
    def json(self):
        return self.json_data

class DocExampleScripts_Test(TestCase):

    def mocked_requests_get(*args, **kwargs):
        print('GET: ' + args[0]) 

        if args[0] == 'https://api.ng.bluemix.net/v2/info':
            return MockResponse({"authorization_endpoint": "https://login.ng.bluemix.net/UAALoginServerWAR"}, 200)

        raise RuntimeError("Should not reach here")

    def mocked_requests_post(*args, **kwargs):
        print('POST: ' + args[0])

        if args[0] == 'https://login.ng.bluemix.net/UAALoginServerWAR/oauth/token':
            return MockResponse({'access_token': 'aaaaa', 'token_type': 'bearer', 'refresh_token': 'aaaaa', 'expires_in': 1209599}, 200)

        raise RuntimeError("Should not reach here")

    def mocked_requests_delete(*args, **kwargs):
        print('POST: ' + args[0])

        if args[0] == 'https://api.ng.bluemix.net/v2/service_instances/1234567890?recursive=true':
            return MockResponse({}, 204)

        raise RuntimeError("Should not reach here")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    @mock.patch('requests.delete', side_effect=mocked_requests_delete)
    def test(self, mock_get, mock_post, mock_delete):

        tmp = tempfile.NamedTemporaryFile(delete=True)
        try:
            data = json.dumps({
                "name": "iae-key",
                "description": "",
                "createdAt": "2017-11-14T12:30+0000",
                             "apiKey": ""
            }).encode('utf-8')
            tmp.write(data)
            tmp.flush()
        
            os.environ['API_KEY_FILENAME'] = tmp.name
            os.environ['CLUSTER_INSTANCE_GUID'] = '1234567890'

            scriptfile = os.path.abspath(os.path.join(scriptDir, 'delete_cluster.py'))
            try:
                # Python 2x
                execfile(scriptfile)
            except:
                # Python 3x
                exec(open(scriptfile).read())
        finally:
            tmp.close()  # deletes the file
