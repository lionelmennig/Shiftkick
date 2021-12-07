from extensions.Shiftkick.logical_shiftlight.lib.BaseScheme import BaseScheme

class Scheme(BaseScheme):
    def applyScheme(self, floatValue = 0):
        for i in range(len(self.leds)):
            if (i % 2 == 0):
                self.ac.setBackgroundTexture(self.leds[i], self.image)
            else:
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)

    def shouldAlwaysRefresh(self):
        return False