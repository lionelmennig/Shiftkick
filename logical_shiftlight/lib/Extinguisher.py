class Extinguisher:
    def __init__(self, ac, leds, placeholder):
        self.ac = ac
        self.leds = leds
        self.placeholder = placeholder
        
    def extinguish(self):
        for i in range(len(self.leds)):
            self.ac.setBackgroundTexture(self.leds[i], self.placeholder)