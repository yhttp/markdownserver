import io
import os
import re
from pathlib import Path


HEADING = re.compile(r'^(#{1,6}) (.*)')


def headings(filename):
    with open(filename) as f:
        for l in f:
            m = HEADING.match(l)
            if not m:
                continue

            level, title = m.groups()
            yield len(level), title


def allfiles(root):
    for filename in Path(root).rglob('*.md'):
        yield filename


def extract_toc(root, outfile, depth, cr='\n'):
    step = 2
    level = 0
    indent = 0

    def indentin():
        nonlocal indent
        indent += step

    def indentout():
        nonlocal indent
        indent -= step

    def spaces():
        return ' ' * indent

    def listopen():
        outfile.write(f'{spaces()}<ul>{cr}')
        indentin()

    def listclose():
        indentout()
        outfile.write(f'{spaces()}</ul>{cr}')

    def itemopen(s, href):
        outfile.write(f'{spaces()}<li><a href="{href}">{s}</a>{cr}')
        indentin()

    def itemclose():
        indentout()
        outfile.write(f'{spaces()}</li>{cr}')

    def closeall(l):
        nonlocal level
        itemclose()
        while l < level:
            listclose()
            itemclose()
            level -= 1

    listopen()
    baselevel = 0
    for filename in sorted(allfiles(root)):
        level = 0
        for l, h in headings(filename):
            if l > (baselevel + depth):
                continue

            if not level:
                level = baselevel = l
            elif l == level:
                itemclose()

            # Level ->
            elif l > level:
                if (l - level) > 1:
                    # Level gap, Ignoring node, TODO: warning
                    continue

                listopen()

            # Level <-
            elif l < level:
                closeall(l)

            href = os.path.relpath(filename, root)
            bookmark = re.sub(r'[:)(><]*', '', h.lower())
            bookmark = re.sub(r'\s+', '-', bookmark)
            itemopen(h, f'/{href}#{bookmark}')
            level = l

        if level >= 1:
            closeall(baselevel)

    listclose()


def generate(root, depth=1):
    f = io.StringIO()
    extract_toc(root, f, depth)
    return f.getvalue()
