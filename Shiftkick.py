################################################
# Shiftkick by Lionel Mennig (leeyo)
# 
# Version: 1.0.1
#
# None of the code below is to be redistributed
# or reused without the permission of the
# author.
################################################

import os
from os import path
from extensions.Shiftkick.common.OptimalShiftlightState import OptimalShiftlightState

class Shiftkick:
    
    gamesenseShiftlight = False
    gamesenseShiftlightEnabled = False
    logicalShiftlight = False
    logicalShiftlightEnabled = False
    
    def __init__(self, ac):
        pluginDir = os.path.dirname(__file__)
        if (os.path.isdir(pluginDir + "/gamesense_shiftlight")):
            from extensions.Shiftkick.gamesense_shiftlight.GamesenseShiftlight import GamesenseShiftlight
            self.gamesenseShiftlight = GamesenseShiftlight()
        if (os.path.isdir(pluginDir + "/logical_shiftlight")):
            from extensions.Shiftkick.logical_shiftlight.LogicalShiftlight import LogicalShiftlight
            self.logicalShiftlight = LogicalShiftlight(ac = ac, pluginDir = pluginDir + "/logical_shiftlight")
    
    def update(self, yellowFloatValue = 0, redFloatValue = 0, optimalShiftlightState = OptimalShiftlightState.OFF):
        if (self.gamesenseShiftlightEnabled and self.gamesenseShiftlight):
            self.gamesenseShiftlight.update(yellowFloatValue = yellowFloatValue, redFloatValue = redFloatValue, optimalShiftlightState = optimalShiftlightState)
        if (self.logicalShiftlightEnabled and self.logicalShiftlight):
            self.logicalShiftlight.update(yellowFloatValue = yellowFloatValue, redFloatValue = redFloatValue, optimalShiftlightState = optimalShiftlightState)