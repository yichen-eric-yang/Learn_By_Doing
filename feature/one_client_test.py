import os
from os.path import split
from testplan.testing.multitest import testcase, testsuite, MultiTest
from pyfixmsg.fixmessage import FixMessage
from pyfixmsg.reference import FixSpec
from pyfixmsg.codecs.stringfix import Codec

from testplan.common.utils.context import context
from testplan.testing.multitest.driver.fix import FixServer, FixClient

from ..FIX import fix_basic

CURRENT_PATH = os.getcwd()
SPEC_FILE = os.path.join(CURRENT_PATH, "spec", "FIX42.xml")
spec = FixSpec(SPEC_FILE)

codec = Codec(spec=spec)


def fixmsg(source):
    """
    docstring
    """
    msg = FixMessage(source)
    msg.codec = codec
    return msg


@testsuite
class fix_one_client_test:
    @testcase
    def send_receive_message(self, env, result):
        """
        docstring
        """
        source = {8: "FIX.4.2", 9: "97", 35: "D", 45: "6", 34: "14"}
        msg = fixmsg(source=source)
        expmsg = fixmsg(
            {
                8: "FIX.4.2",
                35: "D",
                34: "2",
                49: env.client.sender,
                56: env.client.target,
            }
        )
        env.client.send(msg)
        received = env.server.receive()
        result.fix.match(
            expmsg,
            received,
            include_tags=[8, 35, 34, 49, 56],
            description="Message client sent match",
        )


def add_fix_test_one_client():
    """
    docstring
    """
    test = MultiTest(
        name="FIX_one_client",
        suites=[fix_one_client_test()],
        environment=[
            FixServer(name="server", msgclass=FixMessage, codec=codec),
            FixClient(
                name="client",
                host=context("server", "{{host}}"),
                port=context("server", "{{port}}"),
                sender="TW",
                target="ISLD",
                msgclass=FixMessage,
                codec=codec,
            ),
        ],
    )
    return test
