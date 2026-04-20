import allure

from tests.assertions.base import assert_equal
from tests.clients.postgres.operations.model import OperationsTestModel
from tests.schema.operations import (
    OperationEventTestSchema,
    OperationTestType,
    OperationTestStatus,
)

from tests.tools.logger import get_test_logger
from tests.tools.date import to_proto_test_datetime

from protos.gen.contracts.services.operations.rpc_get_operations_pb2 import (
    GetOperationsResponse,
)
from protos.gen.contracts.services.operations.operation_pb2 import (
    Operation,
    OperationType,
    OperationStatus,
)


logger = get_test_logger("GRPC_OPERATIONS_ASSERTIONS")


OPERATION_TYPE_MAPPING = {
    OperationTestType.DEPOSIT: OperationType.OPERATION_TYPE_TOP_UP,
    OperationTestType.WITHDRAW: OperationType.OPERATION_TYPE_CASH_WITHDRAWAL,
}

OPERATION_STATUS_MAPPING = {
    OperationTestStatus.SUCCESS: OperationStatus.OPERATION_STATUS_COMPLETED,
    OperationTestStatus.FAILED: OperationStatus.OPERATION_STATUS_FAILED,
}


@allure.step("Check gRPC operation from event")
def assert_operation_from_event(
    actual: Operation,
    expected: OperationEventTestSchema,
) -> None:
    logger.info("Check gRPC operation from event")

    assert_equal(actual.type, OPERATION_TYPE_MAPPING[expected.type], "type")
    assert_equal(actual.status, OPERATION_STATUS_MAPPING[expected.status], "status")
    assert_equal(actual.amount, expected.amount, "amount")
    assert_equal(actual.user_id, expected.user_id, "user_id")
    assert_equal(actual.card_id, expected.card_id, "card_id")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(
        actual.created_at,
        to_proto_test_datetime(expected.created_at),
        "created_at",
    )
    assert_equal(actual.account_id, expected.account_id, "account_id")


@allure.step("Check gRPC operation from model")
def assert_operation_from_model(
    actual: Operation,
    expected: OperationsTestModel,
) -> None:
    logger.info("Check gRPC operation from model")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.type, OPERATION_TYPE_MAPPING[expected.type], "type")
    assert_equal(actual.status, OPERATION_STATUS_MAPPING[expected.status], "status")
    assert_equal(actual.amount, expected.amount, "amount")
    assert_equal(actual.user_id, expected.user_id, "user_id")
    assert_equal(actual.card_id, expected.card_id, "card_id")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(
        actual.created_at,
        to_proto_test_datetime(expected.created_at),
        "created_at",
    )
    assert_equal(actual.account_id, expected.account_id, "account_id")


@allure.step("Check gRPC get operations response from events")
def assert_get_operations_response_from_events(
    actual: GetOperationsResponse,
    expected: list[OperationEventTestSchema],
) -> None:
    logger.info("Check gRPC get operations response from events")

    assert_equal(len(actual.operations), len(expected), "operations count")

    for index, event in enumerate(expected):
        assert_operation_from_event(actual.operations[index], event)


@allure.step("Check gRPC get operations response from models")
def assert_get_operations_response_from_models(
    actual: GetOperationsResponse,
    expected: list[OperationsTestModel],
) -> None:
    logger.info("Check gRPC get operations response from models")

    assert_equal(len(actual.operations), len(expected), "operations count")

    for index, model in enumerate(expected):
        assert_operation_from_model(actual.operations[index], model)