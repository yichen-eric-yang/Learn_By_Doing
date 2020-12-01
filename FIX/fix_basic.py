from pyfixmsg.fixmessage import FixFragment, FixMessage
from pyfixmsg.codecs.stringfix import Codec
from pyfixmsg.reference import FixSpec, FixTag
import os


SPEC_FILE = os.environ["FIX_SPEC_FILE"]
spec = FixSpec(SPEC_FILE)
codec = Codec(spec=SPEC_FILE, fragment_class=FixFragment)


def fixmsg(*args, **kwargs) -> FixMessage:
    """
    docstring
    """
    returned = FixMessage(*args, **kwargs)
    returned.codec = codec
    return returned


data = (
    "8=FIX.4.2, 9=97, 35=6, 45=6, 49=ABC, 56=CAB, 34=14, 52=20201130-10:27:30"
    "23=115685,28=N,55=BLAH,54=2,44=2200.75,27=S,25=H,10=248"
)

fixMsg = FixMessage().load_fix(data, separator=",")

message = fixmsg().load_fix(data, separator=",")
message.codec = codec

print("Message Type {} ({})".format(fixMsg[35], spec.msg_types[fixMsg[35]].name))
check_tags = (55, 44, 27)
for element, required in spec.msg_types[fixMsg[35]].composition:
    if isinstance(element, FixTag) and element.tag in check_tags:
        if required:
            print("{} is required on this message type".format(element.name))
        else:
            print("{} is not required on this message type".format(element.name))
print(
    "Spec also allows looking up enums: {}  is {}".format(
        fixMsg[54], spec.tags.by_tag(54).enum_by_value(fixMsg[54])
    )
)

