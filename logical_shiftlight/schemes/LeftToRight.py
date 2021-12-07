from extensions.Shiftkick.logical_shiftlight.lib.BaseScheme import BaseScheme

class Scheme(BaseScheme):
    def applyScheme(self, floatValue = 0):
        nbLeds = len(self.leds)
        x = nbLeds * (floatValue / 100)
        for i in range(nbLeds):
            if (i < x):
                self.ac.setBackgroundTexture(self.leds[i], self.image)
            else:
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)

    def shouldAlwaysRefresh(self):
        return True