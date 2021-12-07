class BaseOptimalScheme:
    def __init__(self, ac, leds, image):
        self.ac = ac
        self.leds = leds
        self.nbLeds = len(leds)
        self.image = image
    
    def applyScheme(self, blinkingState = True):
        for i in range(self.nbLeds):
            self.ac.setBackgroundTexture(self.leds[i], self.image)