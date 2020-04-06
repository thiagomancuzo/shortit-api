# coding: utf-8

from flask import url_for
from shortit.exceptions import USER_NOT_FOUND


def _register_user(testapp, **kwargs):
    return testapp.post_json(url_for('user.register_user'), {
              "email": 'foo@bar.com',
              "username": 'foobar',
              "password": 'myprecious'}, **kwargs)


class TestUser:

    def test_get_user_not_loggedin(self, testapp):
        _register_user(testapp)
        resp = testapp.get(url_for('user.get_user', username='foobar'))
        assert resp.json['email'] == 'foo@bar.com'

    def test_get_user_not_existing(self, testapp):
        resp = testapp.get(url_for('user.get_user', username='foobar'), expect_errors=True)
        assert resp.status_int == 404
        assert resp.json == USER_NOT_FOUND['message']
