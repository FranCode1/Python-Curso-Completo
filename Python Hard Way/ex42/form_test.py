from flask import Flask, render_template, request
from app import app
from nose.tools import *

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    # GET vacío debe mostrar el formulario
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    # POST con datos
    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', data=data, follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)
