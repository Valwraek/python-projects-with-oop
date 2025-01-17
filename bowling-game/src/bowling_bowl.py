class Score_card():
    
    def __init__(self, pins):
        
        self.pins = list(pins)
        
    def get_pins(self):
        return self.pins
        
    def miss_sign_to_num_conversor(self):
        converted_pins = list(map(lambda x: "0" if x == "-" else x, self.pins))
        return converted_pins
        