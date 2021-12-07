################################################
# LogicalShiftlight by Lionel Mennig (leeyo)
# 
# Version: 1.1.0
# Based of Shiftkick 1.1.0
#
# None of the code below is to be redistributed
# or reused without the permission of the
# author.
################################################

from extensions.Shiftkick.common.OptimalShiftlightState import OptimalShiftlightState
from extensions.Shiftkick.logical_shiftlight.lib.ShifterState import ShifterState
from extensions.Shiftkick.logical_shiftlight.lib.ConfigManager import ConfigManager
from extensions.Shiftkick.logical_shiftlight.lib.Extinguisher import Extinguisher

class LogicalShiftlight:
    
    lastState = ShifterState.OFF
    blinkerIsOn = True
    blinkerHeartbeat = 0
    
    def __init__(self, ac, pluginDir):
        # Load config and parameters
        configManager = ConfigManager(pluginDir)
        isVertical = configManager.displayVertically
        nbLeds = configManager.ledsCount
        ledsSpacing = configManager.ledsSpacing
        ledWidth = configManager.ledWidth
        ledHeight = configManager.ledHeight
        self.blinkingSpeed = configManager.blinkingSpeed
        yellowValueToStartBlinking = configManager.yellowBlinkingPerc
        redValueToStartBlinking = configManager.redBlinkingPerc
        
        # Load images
        yellowImage = pluginDir + "/images/" + configManager.imageYellow + ".png"
        redImage = pluginDir + "/images/" + configManager.imageRed + ".png"
        optimalImage = pluginDir + "/images/" + configManager.imageOptimal + ".png"
        placeholder = pluginDir + "/images/" + configManager.imagePlaceholder + ".png"
        
        # Create the app
        self.shiftlightWindow = ac.newApp("Shiftkick logical shiftlight")
        ac.setTitle(self.shiftlightWindow, "")
        ac.drawBorder(self.shiftlightWindow, 0)
        ac.setIconPosition(self.shiftlightWindow, 0, -10000)
        windowWidth = ledWidth if isVertical else (ledWidth * nbLeds + (nbLeds - 1) * ledsSpacing)
        windowHeight = (ledHeight * nbLeds + (nbLeds - 1) * ledsSpacing) if isVertical else ledHeight
        ac.setSize(self.shiftlightWindow, windowWidth, windowHeight)
        ac.setVisible(self.shiftlightWindow, 1)
        ac.setBackgroundOpacity(self.shiftlightWindow, 0)
        
        # Create the LEDs
        leds = []
        for i in range(nbLeds):
            led = ac.addLabel(self.shiftlightWindow, "")
            ac.setSize(led, ledWidth, ledHeight)
            xPosition = 0 if isVertical else (ledWidth * i + (i * ledsSpacing))
            yPosition = (ledHeight * i + (i * ledsSpacing)) if isVertical else 0
            ac.setPosition(led, xPosition, yPosition)
            ac.setVisible(led, 1)
            ac.setBackgroundTexture(led, placeholder)
            leds.append(led)
        
        # Get the schemes and initialize them
        optimalModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseOptimalScheme', fromlist=['BaseOptimalScheme'])
        self.optimalScheme = optimalModule.BaseOptimalScheme(ac, leds, optimalImage)
        
        optimalLateModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.AlwaysBlinking', fromlist=['AlwaysBlinking'])
        self.optimalLateScheme = optimalLateModule.AlwaysBlinking(ac, leds, optimalImage, placeholder)
        
        try:
            yellowModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeYellow, fromlist=[configManager.schemeYellow])
            self.yellowScheme = yellowModule.Scheme(ac, leds, yellowImage, placeholder, yellowValueToStartBlinking)
        except:
            yellowModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.yellowScheme = yellowModule.BaseScheme(ac, leds, yellowImage, placeholder, yellowValueToStartBlinking)
        
        try:
            redModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeRed, fromlist=[configManager.schemeRed])
            self.redScheme = redModule.Scheme(ac, leds, redImage, placeholder, redValueToStartBlinking)
        except:
            redModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.redScheme = redModule.BaseScheme(ac, leds, redImage, placeholder, redValueToStartBlinking)
        
        # Instanciate an extinguisher (so 'self' doesn't need to retain 'ac', 'leds' and 'placeholder')
        self.extinguisher = Extinguisher(ac, leds, placeholder)
    
    def __heartbeat(self):
        self.blinkerHeartbeat += 1
        if (self.blinkerHeartbeat >= self.blinkingSpeed):
            self.blinkerIsOn = not self.blinkerIsOn
            self.blinkerHeartbeat = 0
            
    
    def update(self, yellowFloatValue = 0, redFloatValue = 0, optimalShiftlightState = OptimalShiftlightState.OFF):
        self.__heartbeat()
        if (optimalShiftlightState == OptimalShiftlightState.OPTIMAL):
            if (self.lastState is not ShifterState.OPTIMAL):
                self.optimalScheme.applyScheme()
                self.lastState = ShifterState.OPTIMAL
        elif (optimalShiftlightState == OptimalShiftlightState.OPTIMAL_LATE):
            self.optimalLateScheme.applyScheme(self.blinkerIsOn)
            self.lastState = ShifterState.OPTIMAL_LATE
        elif (redFloatValue > 0):
            if (self.lastState is not ShifterState.RED or self.redScheme.shouldAlwaysRefresh):
                self.redScheme.applyScheme(redFloatValue, self.blinkerIsOn)
                self.lastState = ShifterState.RED
        elif (yellowFloatValue > 0):
            if (self.lastState is not ShifterState.YELLOW or self.yellowScheme.shouldAlwaysRefresh):
                self.yellowScheme.applyScheme(yellowFloatValue, self.blinkerIsOn)
                self.lastState = ShifterState.YELLOW
        else:
            if (self.lastState is not ShifterState.OFF):
                self.extinguisher.extinguish()
                self.lastState = ShifterState.OFF