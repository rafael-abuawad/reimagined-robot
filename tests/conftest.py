import boa
import pytest


@pytest.fixture(scope="module")
def accounts():
    return [boa.env.generate_address() for _ in range(10)]

@pytest.fixture(scope="module")
def sender():
    return boa.env.generate_address()

@pytest.fixture(scope="module")
def demo(sender):
    with boa.env.prank(sender):
        return boa.load("contracts/demo.vy")
