class Score_card():
    
    def __init__(self, pins):
        
        self.pins = list(pins)
        
    def get_pins(self):
        return self.pins
        
    def total_score(self):
        
        
        
        return sum(list(map(lambda x: int(x) if x == f"{x}" else x, self.pins)))
        
        
    def miss_sign_to_num_conversor(self):
        converted_pins = list(map(lambda x: "0" if x == "-" else x, self.pins))                                     # Make private
        return converted_pins
        
        
    def spare_sign_to_num_conversor(self):
        converted_pins = list(map(lambda x: str(10 - self.pins.index(int(x)-1)) if x == "/" else x, self.pins))     # Make private, unfinished
        return converted_pins