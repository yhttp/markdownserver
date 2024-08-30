from bddrest import status, response


def test_server_index(ymdapp, ymdserver, mockupfs):
    root = mockupfs(**{
        'index.md': '# bar index',
    })

    ymdapp.settings.root = root
    ymdapp.ready()
    with ymdserver(url='/index.md'):
        assert status == 200
        assert response.text.startswith('<!DOCTYPE html>')


def test_server_css(ymdapp, ymdserver):
    ymdapp.ready()
    with ymdserver(url='/index.css'):
        assert status == 200
        assert response.text.startswith('')
