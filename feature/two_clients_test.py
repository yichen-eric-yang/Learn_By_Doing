import os
from testplan.testing.multitest import testcase, testsuite, MultiTest
from pyfixmsg.fixmessage import FixMessage
from pyfixmsg.reference import FixSpec
from pyfixmsg.codecs.stringfix import Codec

from testplan.common.utils.context import context
from testplan.testing.multitest.driver.fix import FixServer, FixClient

CURRENT_PATH = os.getcwd()
SPEC_FILE = os.path.join(CURRENT_PATH, "spec", "FIX42.xml")
spec = FixSpec(SPEC_FILE)

codec = Codec(spec=spec)


def fixmsg(source: str) -> FixMessage:
    """
    docstring
    """
    msg = FixMessage(source)
    msg.codec = codec
    return msg


@testsuite
class FIXMultiClient:
    @testcase
    def send_and_receive_msgs(self, env, result):
        """
        docstring
        """
        msg1 = fixmsg({35: "6", 9: "97", 45: "6", 58: "first client"})
        env.client1.send(msg1)
        exp_msg1 = fixmsg(
            {
                8: "FIX.4.2",
                9: "73",
                35: "6",
                45: "6",
                49: env.client1.sender,
                56: env.client1.target,
                58: "first client",
            }
        )
        received1 = env.server.receive((env.client1.target, env.client1.sender))
        result.fix.match(
            exp_msg1,
            received1,
            description="Message sent by client 1 match",
            include_tags=[8, 9, 35, 45, 49, 56, 58],
        )


def add_fix_test_two_clients():
    """
    docstring
    """
    test = MultiTest(
        name="FIX_two_clients",
        suites=[FIXMultiClient()],
        environment=[
            FixServer(name="server", msgclass=FixMessage, codec=codec),
            FixClient(
                name="client1",
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
