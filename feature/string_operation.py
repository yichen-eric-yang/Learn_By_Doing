from testplan.testing.multitest import MultiTest, testsuite, testcase


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


def revert_sentance(input: str) -> str:
    arrayStr = input.split(" ")
    arrayStr.reverse()
    outputStr = ""
    for s in arrayStr:
        outputStr += s + " "
    res = outputStr.strip()
    return res


@testsuite
class string_test:
    @testcase
    def string_operation_test(self, env, result):
        result.equal(revert("I Love Living In Shanghai"), "iahgnahS nI gniviL evoL I")

    @testcase
    def sentance_operation_test(self, env, result):
        result.equal(
            revert_sentance("I Love Living In Shanghai"), "Shanghai In Living Love I"
        )

    @testcase
    def sentance_operation_ddt(self, env, result):
        inputArray = [
            ("I Love Technology", "Technology Love I"),
            ("I am a tester", "tester a am I"),
            ("Ada is living in Shanghai", "Shanghai in living is Ada"),
        ]
        for i in inputArray:
            result.equal(revert_sentance(i[0]), i[1])

    def gettest():
        test = MultiTest(name="String Operation Test", suites=[string_test()])
        return test
