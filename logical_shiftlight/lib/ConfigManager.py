import configparser

class ConfigManager:
    def __init__(self, pluginDir):
        config = configparser.ConfigParser()
        config.read(pluginDir + '/config.ini')
        try:
            self.displayVertically = config.getboolean('LogicalShiftlight', 'display_vertically')
        except:
            self.displayVertically = False
        try:
            self.ledsCount = config.getint('LogicalShiftlight', 'leds_count')
        except:
            self.ledsCount = 5
        try:
            self.ledsSpacing = config.getint('LogicalShiftlight', 'leds_spacing')
        except:
            self.ledsSpacing = 20
        try:
            self.ledWidth = config.getint('LogicalShiftlight', 'led_width')
        except:
            self.ledWidth = 200
        try:
            self.ledHeight = config.getint('LogicalShiftlight', 'led_height')
        except:
            self.ledHeight = 20
        try:
            self.schemeYellow = config['LogicalShiftlight']['scheme_yellow']
        except:
            self.schemeYellow = 'Explosion'
        try:
            self.schemeRed = config['LogicalShiftlight']['scheme_red']
        except:
            self.schemeRed = 'Implosion'
        try:
            self.schemeOptimal = config['LogicalShiftlight']['scheme_optimal']
        except:
            self.schemeOptimal = 'Default'
        try:
            self.schemeOptimalLate = config['LogicalShiftlight']['scheme_optimal_late']
        except:
            self.schemeOptimalLate = 'DefaultBlinking'
        try:
            self.imageYellow = config['LogicalShiftlight']['image_yellow']
        except:
            self.imageYellow = 'default_yellow'
        try:
            self.imageRed = config['LogicalShiftlight']['image_red']
        except:
            self.imageRed = 'default_red'
        try:
            self.imageOptimal = config['LogicalShiftlight']['image_optimal']
        except:
            self.imageOptimal = 'default_optimal'
        try:
            self.imagePlaceholder = config['LogicalShiftlight']['image_placeholder']
        except:
            self.imagePlaceholder = 'default_placeholder'