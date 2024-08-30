from bddrest import status, response, when


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
        assert response.text.startswith('/* yhttp-markdown css */')


def test_server_exclude(ymdapp, ymdserver, mockupfs):
    root = mockupfs(**{
        'index.md': '# index',
        'foo.md': '# foo',
        'bar': {
            'index.md': '# bar index'
        }
    })

    ymdapp.settings.merge(f'''
    root: {root}
    exclude:
        - foo\\.md
        - bar/?.*
    ''')

    ymdapp.ready()
    with ymdserver():
        assert status == 200
        assert response.text.startswith('<!DOCTYPE html>')

        when(url='/index.md')
        assert status == 200

        when(url='/foo.md')
        assert status == 404

        when(url='/bar')
        assert status == 404

        when(url='/bar/index.md')
        assert status == 404

    ymdapp.settings.merge('''
    root: .
    exclude: []
    ''')


def test_server_fallback(ymdapp, ymdserver, mockupfs):
    root = mockupfs(**{
        'index.md': '# index',
        'bar': {
            'index.md': '# bar index'
        },
        'baz': {
            'baz.md': '# baz'
        }
    })
    ymdapp.settings.root = root

    ymdapp.ready()
    with ymdserver():
        assert status == 200

        when(url='/bar.md')
        assert status == 302
        assert response.headers['location'] == 'index.md'

        when(url='/bar/bar.md')
        assert status == 302
        assert response.headers['location'] == 'index.md'

        when(url='/baz/bar.md')
        assert status == 302
        assert response.headers['location'] == '/index.md'


def test_server_webmanifest(ymdapp, ymdserver):
    ymdapp.ready()
    with ymdserver('/webmanifest.json'):
        assert status == 200
        assert response.json == {
            'icons': [
                {
                    'sizes': '192x192',
                    'src': '/.ymdmetadata/android-chrome-192x192.png',
                    'type': 'image/png',
                },
                {
                    'sizes': '512x512',
                    'src': '/.ymdmetadata/android-chrome-512x512.png',
                    'type': 'image/png',
                },
            ],
        }
