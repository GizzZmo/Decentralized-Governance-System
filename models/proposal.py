class Proposal:
    def __init__(self, title, description, proposer):
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = {}

    def cast_vote(self, voter, amount):
        """Registers a vote for the proposal."""
        if voter in self.votes:
            self.votes[voter] += amount
        else:
            self.votes[voter] = amount

    def get_vote_count(self):
        """Returns total votes cast."""
        return sum(self.votes.values())

    def get_results(self):
        """Returns vote breakdown."""
        return self.votes
