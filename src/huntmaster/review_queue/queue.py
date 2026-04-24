from enum import Enum


class ReviewAction(str, Enum):
    APPROVE = "approve"
    EDIT = "edit"
    REJECT = "reject"


class ReviewQueue:
    """Human-in-the-loop review queue for draft reports.

    Each item in the queue is a draft report that must be reviewed
    and approved before any submission to HackerOne.
    """

    def __init__(self) -> None:
        self._queue: list[dict] = []

    def enqueue(self, report: dict) -> int:
        """Add a draft report to the review queue. Returns its queue index."""
        self._queue.append({**report, "review_status": "pending"})
        return len(self._queue) - 1

    def pending(self) -> list[dict]:
        """Return all items awaiting human review."""
        return [item for item in self._queue if item["review_status"] == "pending"]

    def review(self, index: int, action: ReviewAction, notes: str = "") -> dict:
        """Apply a human review decision to the item at the given index."""
        if index < 0 or index >= len(self._queue):
            raise IndexError(f"No queue item at index {index}.")
        item = self._queue[index]
        item["review_status"] = action.value
        item["review_notes"] = notes
        return item
