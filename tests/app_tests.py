from nose.tools import *
from bin.app import app
from tools import assert_response

def test_index():
    # check for a 404 on / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # test first GET request to /index
    resp = app.request("/index")
    assert_response(resp)

    # make sure default values work for game start
    resp = app.request("/game", method = "POST")
    assert_response(resp, contains = "central_corridor")

    # test for expected values
    data = {'name': 'shazbot', 'greet': 'sandraker'}
    resp = app.request("/hello", method = "POST", data = data)
    assert_response(resp, contains = "shazbot")
