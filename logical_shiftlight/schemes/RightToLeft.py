from extensions.Shiftkick.logical_shiftlight.lib.BaseScheme import BaseScheme

class Scheme(BaseScheme):
    def __init__(self, ac, leds, image, placeholder, valueToStartBlinking):
        super().__init__(ac, leds, image, placeholder, valueToStartBlinking)
        self.shouldAlwaysRefresh = True

    def applyScheme(self, floatValue = 0, blinkingState = True):
        turnAllLedsOff = blinkingState == False and self.blinkingEnabled and floatValue >= self.valueToStartBlinking
        if (turnAllLedsOff):
            for i in range(self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)
        else:
            x = self.nbLeds * (floatValue / 100)
            for i in range(self.nbLeds):
                if (self.nbLeds - (i + 1) < x):
                    self.ac.setBackgroundTexture(self.leds[i], self.image)
                else:
                    self.ac.setBackgroundTexture(self.leds[i], self.placeholder)