class BaseScheme:
    def __init__(self, ac, leds, image, placeholder, valueToStartBlinking):
        self.ac = ac
        self.leds = leds
        self.nbLeds = len(leds)
        self.image = image
        self.placeholder = placeholder
        self.valueToStartBlinking = valueToStartBlinking
        self.blinkingEnabled = valueToStartBlinking < 100
        self.shouldAlwaysRefresh = self.blinkingEnabled      # Will always allow 'applyScheme' to be triggered
    
    def applyScheme(self, floatValue = 0, blinkingState = True):
        turnAllLedsOff = blinkingState == False and self.blinkingEnabled and floatValue >= self.valueToStartBlinking
        if (turnAllLedsOff):
            for i in range(self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)
        else:
            for i in range(self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.image)