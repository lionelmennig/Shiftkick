from extensions.Shiftkick.logical_shiftlight.lib.BaseScheme import BaseScheme

class Scheme(BaseScheme):
    def applyScheme(self, floatValue = 0):
        nbLeds = len(self.leds)
        half = nbLeds / 2 if nbLeds % 2 == 0 else (nbLeds + 1) / 2 # half]
        x = half * (floatValue / 100)
        for i in range(0, int(half)):
            if (half - (i + 1) < x):
                self.ac.setBackgroundTexture(self.leds[i], self.image)
            else:
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)
        half = nbLeds / 2 if nbLeds % 2 == 0 else (nbLeds - 1) / 2 # ]half
        for i in range(int(half), nbLeds):
            if (i < x + half):
                self.ac.setBackgroundTexture(self.leds[i], self.image)
            else:
                self.ac.setBackgroundTexture(self.leds[i], self.placeholder)

    def shouldAlwaysRefresh(self):
        return True