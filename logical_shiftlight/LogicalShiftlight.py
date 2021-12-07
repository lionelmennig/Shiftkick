################################################
# LogicalShiftlight by Lionel Mennig (leeyo)
# 
# Version: 1.0.0
# Based of Shiftkick 1.0.0
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
    
    def __init__(self, ac, pluginDir):
        # Load config and parameters
        configManager = ConfigManager(pluginDir)
        isVertical = configManager.displayVertically
        nbLeds = configManager.ledsCount
        ledsSpacing = configManager.ledsSpacing
        ledWidth = configManager.ledWidth
        ledHeight = configManager.ledHeight
        
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
        try:
            optimalModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeOptimal, fromlist=[configManager.schemeOptimal])
            self.optimalScheme = optimalModule.Scheme()
        except:
            optimalModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.optimalScheme = optimalModule.BaseScheme()
        self.optimalScheme.initialize(ac, leds, optimalImage, placeholder)
        
        try:
            optimalLateModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeOptimalLate, fromlist=[configManager.schemeOptimalLate])
            self.optimalLateScheme = optimalLateModule.Scheme()
        except:
            optimalLateModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.optimalLateScheme = optimalLateModule.BaseScheme()
        self.optimalLateScheme.initialize(ac, leds, optimalImage, placeholder)

        try:
            yellowModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeYellow, fromlist=[configManager.schemeYellow])
            self.yellowScheme = yellowModule.Scheme()
        except:
            yellowModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.yellowScheme = yellowModule.BaseScheme()
        self.yellowScheme.initialize(ac, leds, yellowImage, placeholder)

        try:
            redModule = __import__('extensions.Shiftkick.logical_shiftlight.schemes.' + configManager.schemeRed, fromlist=[configManager.schemeRed])
            self.redScheme = redModule.Scheme()
        except:
            redModule = __import__('extensions.Shiftkick.logical_shiftlight.lib.BaseScheme', fromlist=['BaseScheme'])
            self.redScheme = redModule.BaseScheme()
        self.redScheme.initialize(ac, leds, redImage, placeholder)
        
        # Instanciate an extinguisher (so 'self' doesn't need to retain 'ac', 'leds' and 'placeholder')
        self.extinguisher = Extinguisher(ac, leds, placeholder)
    
    def update(self, yellowFloatValue = 0, redFloatValue = 0, optimalShiftlightState = OptimalShiftlightState.OFF):
        if (optimalShiftlightState == OptimalShiftlightState.OPTIMAL):
            if (self.lastState is not ShifterState.OPTIMAL):
                self.optimalScheme.applyScheme()
                self.lastState = ShifterState.OPTIMAL
        elif (optimalShiftlightState == OptimalShiftlightState.OPTIMAL_LATE):
            if (self.lastState is not ShifterState.OPTIMAL_LATE):
                self.optimalLateScheme.applyScheme()
                self.lastState = ShifterState.OPTIMAL_LATE
        elif (redFloatValue > 0):
            if (self.lastState is not ShifterState.RED or self.redScheme.shouldAlwaysRefresh()):
                self.redScheme.applyScheme(redFloatValue)
                self.lastState = ShifterState.RED
        elif (yellowFloatValue > 0):
            if (self.lastState is not ShifterState.YELLOW or self.yellowScheme.shouldAlwaysRefresh()):
                self.yellowScheme.applyScheme(yellowFloatValue)
                self.lastState = ShifterState.YELLOW
        else:
            if (self.lastState is not ShifterState.OFF):
                self.extinguisher.extinguish()
                self.lastState = ShifterState.OFF