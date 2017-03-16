from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #check that we get a 404 on the / urls
    resp = app.request("/")
    assert_response(resp, status="404")

    #test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # make sure default values work for the web form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    # test that we got the expected values
    data = {'name': 'Peter', 'greet': 'Hello'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Peter")
