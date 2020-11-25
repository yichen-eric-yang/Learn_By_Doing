from req import request_body
from testplan.testing.multitest import MultiTest, testsuite, testcase


@testsuite
class api_testsuite:
    @testcase
    def test_get_method(self, env, result) -> None:
        header = {
            "Content-Type": "text/html",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "deny",
            "X-Github-Request-Id": "621C:0ADF:AF15BF:E50690:5FBE10AF",
        }
        runcommand = request_body(
            url="https://github.com/Morgan-Stanley/testplan", headers=header,
        )
        runcommand.response = request_body.get(runcommand).status_code
        result.equal(runcommand.response, 200)

    def get_test():
        test = MultiTest(name="API Test", suites=[api_testsuite()])
        return test


# if __name__ == "__main__":
#     sys.exit(not api_testsuite.test())
