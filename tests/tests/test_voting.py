import pytest
from services.voting import VotingService
from models.proposal import Proposal

@pytest.fixture
def setup_voting():
    return VotingService()

def test_submit_proposal(setup_voting):
    proposal = Proposal("Upgrade Treasury Security", "Introduce multi-sig wallets", "Admin")
    proposal_id = setup_voting.submit_proposal(proposal)
    assert proposal_id == 1

def test_cast_vote(setup_voting):
    proposal = Proposal("Decentralized ID", "Blockchain-based identity system", "User1")
    proposal_id = setup_voting.submit_proposal(proposal)
    success = setup_voting.cast_vote(proposal_id, "User2", 10)
    assert success is True
    assert setup_voting.get_proposal_results(proposal_id)["User2"] == 10
