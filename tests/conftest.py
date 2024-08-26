import os
import functools

import bddcli
import bddrest
import pytest
import yhttp.core as y

from yhttp.dev.fixtures import mockupfs, freetcpport


GITHUBACTIONS = 'CI' in os.environ and os.environ['CI'] \
    and 'GITHUB_RUN_ID' in os.environ


@pytest.fixture
def cliapp():
    cliapp = bddcli.Application(
        'yhttp-markdown',
        'yhttp.markdown.main:Main.quickstart'
    )
    return functools.partial(bddcli.Given, cliapp)


@pytest.fixture
def yapp():
    return y.Application()


@pytest.fixture
def webapi(yapp):
    yield functools.partial(bddrest.Given, yapp)
