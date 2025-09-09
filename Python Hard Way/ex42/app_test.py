from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    # Prueba acceso a ruta inexistente
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    # Prueba GET en /hello (formulario)
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    # Prueba POST con datos válidos
    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)
