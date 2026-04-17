import allure

from tests.assertions.base import assert_equal
from tests.tools.logger import get_test_logger
from protos.gen.contracts.services.users.user_pb2 import User

logger = get_test_logger("GRPC_USERS_ASSERTIONS")


@allure.step("Check gRPC user")
def assert_user(actual: User, expected: User) -> None:
    logger.info("Check gRPC user")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    assert_equal(actual.phone_number, expected.phone_number, "phone_number")