from yhttp.markdown import toc


def test_toc_extractdir(mockupfs):
    root = mockupfs(**{
        'bar': {
            'index.md': '# bar index',
        },
        '0-index.md': '# index',
        '1-foo.md': '## foo',
        '2-baz': '## baz',
        '.qux.md': '## qux',
    })

    headings, subdirs = toc.extractdir(root, '.')
    assert subdirs == ['bar']
    assert headings == [
        {
            'bookmark': 'index',
            'children': [
                {
                    'bookmark': 'foo',
                    'children': [],
                    'href': '1-foo.md',
                    'level': 2,
                    'title': 'foo',
                },
            ],
            'href': '0-index.md',
            'level': 1,
            'title': 'index',
        },
    ]


def test_toc_extract():
    doc = '''
    # Foo
    ## Bar
    ### Baz
    ## Qux
    # Quux
    '''

    out = toc.extract('foobarbaz.md', doc.splitlines())
    assert out == [
        {
            'bookmark': 'foo',
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Foo',
            'children': [
                {
                    'bookmark': 'bar',
                    'href': 'foobarbaz.md',
                    'level': 2,
                    'title': 'Bar',
                    'children': [
                        {
                            'bookmark': 'baz',
                            'href': 'foobarbaz.md',
                            'level': 3,
                            'title': 'Baz',
                            'children': [],
                        },
                    ],
                },
                {
                    'bookmark': 'qux',
                    'href': 'foobarbaz.md',
                    'level': 2,
                    'title': 'Qux',
                    'children': [],
                },
            ],
        },
        {
            'bookmark': 'quux',
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Quux',
            'children': [],
        },
    ]


def test_toc_extract_depth():
    doc = '''
    # Foo
    ## Bar
    ### Baz
    '''

    out = toc.extract('foobarbaz.md', doc.splitlines(), depth=2)
    assert out == [
        {
            'bookmark': 'foo',
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Foo',
            'children': [
                {
                    'bookmark': 'bar',
                    'href': 'foobarbaz.md',
                    'level': 2,
                    'title': 'Bar',
                    'children': [],
                },
            ],
        },
    ]


def test_toc_extract_levelgap():
    doc = '''
    # Foo
    ### Baz
    '''

    out = toc.extract('foobarbaz.md', doc.splitlines())
    assert out == [
        {
            'bookmark': 'foo',
            'children': [],
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Foo',
        },
    ]


def test_toc_extract_backwardgap():
    doc = '''
    # Foo
    ## Bar
    ### Baz
    # Quux
    '''

    out = toc.extract('foobarbaz.md', doc.splitlines())
    assert out == [
        {
            'bookmark': 'foo',
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Foo',
            'children': [
                {
                    'bookmark': 'bar',
                    'href': 'foobarbaz.md',
                    'level': 2,
                    'title': 'Bar',
                    'children': [
                        {
                            'bookmark': 'baz',
                            'href': 'foobarbaz.md',
                            'level': 3,
                            'title': 'Baz',
                            'children': [],
                        },
                    ],
                },
            ],
        },
        {
            'bookmark': 'quux',
            'href': 'foobarbaz.md',
            'level': 1,
            'title': 'Quux',
            'children': [],
        },
    ]
