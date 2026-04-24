from huntmaster.h1_connector.client import HackerOneClient


def test_submit_report_is_disabled():
    client = HackerOneClient(username="user", api_token="tok")
    try:
        client.submit_report()
        assert False, "Should have raised RuntimeError"
    except RuntimeError as exc:
        assert "disabled" in str(exc).lower()


def test_list_programs_not_implemented():
    client = HackerOneClient(username="user", api_token="tok")
    try:
        client.list_programs()
        assert False, "Should have raised NotImplementedError"
    except NotImplementedError:
        pass


def test_get_structured_scope_not_implemented():
    client = HackerOneClient(username="user", api_token="tok")
    try:
        client.get_structured_scope("prog-1")
        assert False, "Should have raised NotImplementedError"
    except NotImplementedError:
        pass
