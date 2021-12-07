class BaseScheme:
    def initialize(self, ac, leds, image, placeholder):
        self.ac = ac
        self.leds = leds
        self.image = image
        self.placeholder = placeholder
    
    def applyScheme(self, floatValue = 0):
        for i in range(len(self.leds)):
            self.ac.setBackgroundTexture(self.leds[i], self.image)
    
    def shouldAlwaysRefresh(self): # Defines whether to refresh the LEDs state when the scheme is called to be applied twice (or more) in a row or to keep the current state
        return False