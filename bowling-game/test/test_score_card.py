from src.score_card import Score_card

def test_exist_score_card():
    card = Score_card("1234567890")
    assert card
   
    
def test_get_pins():
    PINS = "12345123451234512345"
    card = Score_card(PINS)
    assert list(PINS) == card.get_pins()
    
def test_total_score():
    PINS = "12345123451234512345"
    card = Score_card(PINS)
    assert card.total_score() == 60
    
def test_miss_sign_to_num_conversor():
    PINS = "1234-123451-3451234-"
    card = Score_card(PINS)
    #assert 
    
    
def test_spare_sign_to_num_conversor():
    PINS = "1/3451234515345/234/"
    card = Score_card(PINS)
    assert list("19345123451534552346") == card.spare_sign_to_num_conversor()
    