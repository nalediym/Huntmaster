import pytest

from huntmaster.h1_connector.client import HackerOneClient


def test_submit_report_is_disabled():
    client = HackerOneClient(username="user", api_token="tok")
    with pytest.raises(RuntimeError, match="[Dd]isabled|disabled"):
        client.submit_report()


def test_list_programs_not_implemented():
    client = HackerOneClient(username="user", api_token="tok")
    with pytest.raises(NotImplementedError):
        client.list_programs()


def test_get_structured_scope_not_implemented():
    client = HackerOneClient(username="user", api_token="tok")
    with pytest.raises(NotImplementedError):
        client.get_structured_scope("prog-1")
