from extensions.Shiftkick.logical_shiftlight.lib.BaseScheme import BaseScheme

class Scheme(BaseScheme):
    def __init__(self, ac, leds, image, placeholder, valueToStartBlinking):
        super().__init__(ac, leds, image, placeholder, valueToStartBlinking)
        self.shouldAlwaysRefresh = True
        self.supRoundedHalf = self.nbLeds / 2 if self.nbLeds % 2 == 0 else (self.nbLeds + 1) / 2    # half]
        self.downRoundedHalf = self.nbLeds / 2 if self.nbLeds % 2 == 0 else (self.nbLeds - 1) / 2   # ]half
    
    def applyScheme(self, floatValue = 0, blinkingState = True):
        turnAllLedsOff = blinkingState == False and self.blinkingEnabled and floatValue >= self.valueToStartBlinking
        if (turnAllLedsOff):
            for i in range(0, self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)
        else:
            x = self.supRoundedHalf * (floatValue / 100)
            start = 0
            end = int(self.supRoundedHalf)
            for i in range(start, end):
                if (self.supRoundedHalf - (i + 1) < x):
                    self.ac.setBackgroundTexture(self.leds[i], self.image)
                else:
                    self.ac.setBackgroundTexture(self.leds[i], self.placeholder)
            start = int(self.downRoundedHalf)
            end = self.nbLeds
            for i in range(start, end):
                if (i < x + self.downRoundedHalf):
                    self.ac.setBackgroundTexture(self.leds[i], self.image)
                else:
                    self.ac.setBackgroundTexture(self.leds[i], self.placeholder)