from models.proposal import Proposal

class VotingService:
    def __init__(self):
        self.proposals = {}

    def submit_proposal(self, proposal):
        """Adds a proposal to the system."""
        proposal_id = len(self.proposals) + 1
        self.proposals[proposal_id] = proposal
        return proposal_id

    def cast_vote(self, proposal_id, voter, amount):
        """Validates and processes a vote."""
        if proposal_id in self.proposals:
            self.proposals[proposal_id].cast_vote(voter, amount)
            return True
        return False

    def get_proposal_results(self, proposal_id):
        """Fetches voting results for a proposal."""
        if proposal_id in self.proposals:
            return self.proposals[proposal_id].get_results()
        return None
