from extensions.Shiftkick.logical_shiftlight.lib.BaseOptimalScheme import BaseOptimalScheme

class AlwaysBlinking(BaseOptimalScheme):
    def __init__(self, ac, leds, image, placeholder):
        super().__init__(ac, leds, image)
        self.placeholder = placeholder
    
    def applyScheme(self, blinkingState = True):
        if (blinkingState):
            for i in range(self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.image)
        else:
            for i in range(self.nbLeds):
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)