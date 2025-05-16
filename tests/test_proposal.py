import pytest
from models.proposal import Proposal

def test_create_proposal():
    proposal = Proposal("Improve Governance", "Implement new voting system", "Alice")
    assert proposal.title == "Improve Governance"
    assert proposal.description == "Implement new voting system"
    assert proposal.proposer == "Alice"

def test_cast_vote():
    proposal = Proposal("Test Proposal", "Sample description", "Bob")
    proposal.cast_vote("Alice", 5)
    assert proposal.votes["Alice"] == 5

def test_vote_count():
    proposal = Proposal("Budget Allocation", "Increase funding for research", "Charlie")
    proposal.cast_vote("Dave", 3)
    proposal.cast_vote("Eve", 2)
    assert proposal.get_vote_count() == 5
