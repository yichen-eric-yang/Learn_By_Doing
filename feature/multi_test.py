from testplan import test_plan
import sys
from testplan.report.testing.styles import Style, StyleEnum
from string_operation import string_test
from api_request import api_testsuite

OUTPUT_STYLE = Style(StyleEnum.ASSERTION_DETAIL, StyleEnum.ASSERTION_DETAIL)


@test_plan(
    name="my first test plan",
    pdf_path="result.pdf",
    stdout_style=OUTPUT_STYLE,
    pdf_style=OUTPUT_STYLE,
)
def main(plan):
    plan.add(string_test.gettest())
    plan.add(api_testsuite.get_test())


if __name__ == "__main__":
    res = main()
    print("Exiting code: {}".format(res.exit_code))
    sys.exit(res.exit_code)
