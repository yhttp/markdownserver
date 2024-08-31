import markdown2


extras = [
    'header-ids',
    'tables',
    'fenced-code-blocks',
]


markdowner = markdown2.Markdown(extras=extras)
