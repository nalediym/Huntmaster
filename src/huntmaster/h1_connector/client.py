class HackerOneClient:
    """Read-only HackerOne client placeholder.

    v0.1 should implement safe program and scope fetching only.
    Report submission must remain human-approved and is intentionally not implemented here.
    """

    def __init__(self, username: str, api_token: str) -> None:
        self.username = username
        self.api_token = api_token

    def list_programs(self) -> list[dict]:
        raise NotImplementedError("Implement read-only HackerOne program fetching.")

    def get_structured_scope(self, program_id: str) -> list[dict]:
        raise NotImplementedError("Implement read-only HackerOne structured scope fetching.")

    def submit_report(self, *args, **kwargs) -> None:
        raise RuntimeError("Auto-submission is disabled. Use human-approved workflow only.")
