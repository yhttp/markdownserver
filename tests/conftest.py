import os
import functools

import bddcli
import pytest


GITHUBACTIONS = 'CI' in os.environ and os.environ['CI'] \
    and 'GITHUB_RUN_ID' in os.environ


@pytest.fixture
def cliapp():
    cliapp = bddcli.Application(
        'yhttp-markdown',
        'yhttp.markdown.main:Main.quickstart'
    )
    return functools.partial(bddcli.Given, cliapp)
