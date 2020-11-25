import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite


def multiply(numberA: float, numberB: float) -> float:
    return numberA * numberB


@testsuite
class BasicSuite:
    @testcase
    def basic_mulityply(self, env, result) -> None:
        result.equal(multiply(2, 3), 6, description="passing assertion")
        result.equal(multiply(2, 1), 2, description="passing assertion")


@test_plan(name="multiply")
def main(plan):
    test = MultiTest(name="MultiplyTest", suites=[BasicSuite()])
    plan.add(test)


if __name__ == "__main__":
    sys.exit(not main())

