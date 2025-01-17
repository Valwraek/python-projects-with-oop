from src.bowling_bowl import Score_card

def test_exist_score_card():
    card = Score_card("1234567890")
    assert card
   
    
def test_get_pins():
    PINS = "12345123451234512345"
    card = Score_card(PINS)
    assert PINS[0] == card.get_pins()[0]
    
    
def test_miss_sign_to_num_conversor():
    PINS = "1234-123451-3451234-"
    card = Score_card(PINS)
    assert list("12340123451034512340") == card.miss_sign_to_num_conversor()