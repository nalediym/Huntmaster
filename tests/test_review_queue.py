from huntmaster.review_queue import ReviewQueue, ReviewAction


def test_enqueue_returns_index():
    q = ReviewQueue()
    idx = q.enqueue({"title": "XSS draft", "draft": "## Summary\n..."})
    assert idx == 0


def test_pending_returns_unreviewed_items():
    q = ReviewQueue()
    q.enqueue({"title": "finding-1"})
    q.enqueue({"title": "finding-2"})
    assert len(q.pending()) == 2


def test_review_approve_updates_status():
    q = ReviewQueue()
    q.enqueue({"title": "finding-1"})
    result = q.review(0, ReviewAction.APPROVE, notes="Looks good.")
    assert result["review_status"] == "approve"
    assert result["review_notes"] == "Looks good."


def test_review_reject_removes_from_pending():
    q = ReviewQueue()
    q.enqueue({"title": "finding-1"})
    q.review(0, ReviewAction.REJECT, notes="Out of scope.")
    assert len(q.pending()) == 0


def test_review_invalid_index_raises():
    q = ReviewQueue()
    try:
        q.review(99, ReviewAction.APPROVE)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
