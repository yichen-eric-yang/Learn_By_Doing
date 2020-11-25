import sys
from testplan.report.testing.styles import Style, StyleEnum
from testplan.testing.multitest import MultiTest, testsuite, testcase
from testplan import test_plan

input = "I Love Living In Shanghai"
OUTPUT_STYLE = Style(StyleEnum.ASSERTION_DETAIL, StyleEnum.ASSERTION_DETAIL)


def revert(textInput: str) -> str:
    arrayStr = textInput.split(" ")
    arrayStr.reverse()
    outputStr = ""
    for s in arrayStr:
        charlist = []
        res = ""
        for x in s:
            charlist.append(x)
        charlist.reverse()
        for y in charlist:
            res += y
        outputStr += res + " "
    return outputStr.strip()


# def main():
#     print(revert(input))


@testsuite
class string_test:
    @testcase
    def string_operation_test(self, env, result):
        result.equal(revert("I Love Living In Shanghai"), "iahgnahS nI gniviL evoL I")

    def gettest():
        test = MultiTest(name="my first test", suites=[string_test()])
        return test


@test_plan(
    name="my first test plan",
    pdf_path="result.pdf",
    stdout_style=OUTPUT_STYLE,
    pdf_style=OUTPUT_STYLE,
)
def main(plan):
    plan.add(string_test.gettest())


if __name__ == "__main__":
    res = main()
    print("Exiting code: {}".format(res.exit_code))
    sys.exit(res.exit_code)
