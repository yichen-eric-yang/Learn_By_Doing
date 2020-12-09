from testplan import test_plan
import sys
from testplan.report.testing.styles import Style, StyleEnum
from string_operation import string_test, NegativeTest
import api_request
import one_client_test
import two_clients_test

# from api_request import api_testsuite

OUTPUT_STYLE = Style(StyleEnum.ASSERTION_DETAIL, StyleEnum.ASSERTION_DETAIL)


@test_plan(
    name="my first test plan",
    pdf_path="result.pdf",
    stdout_style=OUTPUT_STYLE,
    pdf_style=OUTPUT_STYLE,
)
def main(plan):
    plan.add(string_test.gettest())
    plan.add(api_request.get_test())
    plan.add(one_client_test.add_fix_test_one_client())
    plan.add(two_clients_test.add_fix_test_two_clients())
    plan.add(NegativeTest.gettest())


if __name__ == "__main__":
    res = main()
    print("Exiting code: {}".format(res.exit_code))
    sys.exit(res.exit_code)
