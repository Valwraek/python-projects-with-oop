from src.bowling_bowl import Score_card

def test_exist_score_card():
    card = Score_card("1234567890")
    assert card