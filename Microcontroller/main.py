from commands import *


token = createToken()
requestSiteInfo(token)
connectorStatus(token)
startCharger(token)
notifyStart(token)
consumedEnergy(token)
changeActiveCurrent(token)
stopCharger(token)
notifyStop(token)
setRFIDtagID(token)
requestRFIDtagID(token)
