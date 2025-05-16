from flask import Flask, request, jsonify
from models.proposal import Proposal
from services.voting import VotingService
from services.treasury import TreasuryService

app = Flask(__name__)

# Initialize Services
voting_service = VotingService()
treasury_service = TreasuryService()

@app.route('/create_proposal', methods=['POST'])
def create_proposal():
    data = request.get_json()
    new_proposal = Proposal(data["title"], data["description"], data["proposer"])
    proposal_id = voting_service.submit_proposal(new_proposal)
    return jsonify({"message": "Proposal created!", "proposal_id": proposal_id})

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    data = request.get_json()
    success = voting_service.cast_vote(data["proposal_id"], data["voter"], data["vote_amount"])
    return jsonify({"message": "Vote recorded!"}) if success else jsonify({"error": "Voting failed!"})

@app.route('/treasury_transaction', methods=['POST'])
def treasury_transaction():
    data = request.get_json()
    success = treasury_service.execute_transaction(data["amount"], data["recipient"])
    return jsonify({"message": "Transaction successful!"}) if success else jsonify({"error": "Transaction failed!"})

if __name__ == '__main__':
    app.run(debug=True)
