import os

class mainGlobalObject():

    def __init__(self):
        self.user = os.getlogin()
        self.manager = ''
        self.country = ''
        self.city = ''
        self.object = ''
        self.client = ''
        self.time = ''
        self.position = ''
        self.company = ''
        self.note = ''
        self.location = ''

        # 'manualChange' - variable add into sql table fnd show filling type:
        # 0 - calculation created by program;
        # 1 - calculation with manually changed parameters
        self.manualChange = 0

        #   calculation equipment
        self.rto = rto()
        self.erpe = erpe()
        self.rvgo = rvgo()

class rto():
    def __init__(self):
        self.proposal_ID = 0
        self.gap = ''
        self.channelWidth = ''
        self.channelDepth = ''
        self.unloadH = ''
        self.driveIP = ''
        self.material = ''
        self.controlPanel = ''
        self.connection = ''

        self.controlPanel_price = 0
        self.price = 0
        self.weight = 0
        self.power = 0
        self.qMax = 0
        self.mark = ''

        # generated files names
        self.name_calculation = ''
        self.name_proposal = ''
        self.description_to_rdc = ''
        self.equipDescription_code = 2

class erpe():
    def __init__(self):
        self.proposal_ID = 0
        self.gap = ''
        self.channelWidth = ''
        self.channelDepth = ''
        self.unloadH = ''
        self.driveIP = ''
        self.material = ''
        self.controlPanel = ''
        self.connection = ''

        self.controlPanel_price = 0
        self.price = 0
        self.weight = 0
        self.power = 0
        self.qMax = 0
        self.mark = ''

        # generated files names
        self.name_calculation = ''
        self.name_proposal = ''
        self.description_to_rdc = ''
        self.equipDescription_code = 4

class rvgo():
    def __init__(self):
        self.proposal_ID = 0
        self.gap = ''
        self.channelWidth = ''
        self.channelDepth = ''
        self.screenHeight = ''
        self.unloadH = ''
        self.driveIP = ''
        self.material = ''
        self.controlPanel = ''
        self.connection = ''

        self.controlPanel_price = 0
        self.price = 0
        self.weight = 0
        self.power = 0
        self.qMax = 0
        self.mark = ''

        # generated files names
        self.name_calculation = ''
        self.name_proposal = ''
        self.description_to_rdc = ''
        self.equipDescription_code = 4