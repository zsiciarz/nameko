import sys
from unittest.mock import patch

import pytest


@pytest.fixture
def command():
    from nameko.cli import cli

    def _command(*argv):
        with patch.object(sys, "argv", list(argv)):
            cli(standalone_mode=False)

    return _command
