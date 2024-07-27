from sqlalchemy import Column, String, Integer, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AccessAndMobilitySubscriptionData(Base):
    __tablename__ = 'AccessAndMobilitySubscriptionData'
    
    ueid = Column(String(15), primary_key=True)
    servingPlmnid = Column(String(15), primary_key=True)
    supportedFeatures = Column(String(50), nullable=True)
    gpsis = Column(JSON, nullable=True)
    internalGroupIds = Column(JSON, nullable=True)
    sharedVnGroupDataIds = Column(JSON, nullable=True)
    subscribedUeAmbr = Column(JSON, nullable=True)
    nssai = Column(JSON, nullable=True)
    ratRestrictions = Column(JSON, nullable=True)
    forbiddenAreas = Column(JSON, nullable=True)
    serviceAreaRestriction = Column(JSON, nullable=True)
    coreNetworkTypeRestrictions = Column(JSON, nullable=True)
    rfspIndex = Column(Integer, nullable=True)
    subsRegTimer = Column(Integer, nullable=True)
    ueUsageType = Column(Integer, nullable=True)
    mpsPriority = Column(Boolean, nullable=True)
    mcsPriority = Column(Boolean, nullable=True)
    activeTime = Column(Integer, nullable=True)
    sorInfo = Column(JSON, nullable=True)
    sorInfoExpectInd = Column(Boolean, nullable=True)
    sorafRetrieval = Column(Boolean, nullable=True)
    sorUpdateIndicatorList = Column(JSON, nullable=True)
    upuInfo = Column(JSON, nullable=True)
    micoAllowed = Column(Boolean, nullable=True)
    sharedAmDataIds = Column(JSON, nullable=True)
    odbPacketServices = Column(JSON, nullable=True)
    serviceGapTime = Column(Integer, nullable=True)
    mdtUserConsent = Column(JSON, nullable=True)
    mdtConfiguration = Column(JSON, nullable=True)
    traceData = Column(JSON, nullable=True)
    cagData = Column(JSON, nullable=True)
    stnSr = Column(String(50), nullable=True)
    cMsisdn = Column(String(50), nullable=True)
    nbIoTUePriority = Column(Integer, nullable=True)
    nssaiInclusionAllowed = Column(Boolean, nullable=True)
    rgWirelineCharacteristics = Column(String(50), nullable=True)
    ecRestrictionDataWb = Column(JSON, nullable=True)
    ecRestrictionDataNb = Column(Boolean, nullable=True)
    expectedUeBehaviourList = Column(JSON, nullable=True)
    primaryRatRestrictions = Column(JSON, nullable=True)
    secondaryRatRestrictions = Column(JSON, nullable=True)
    edrxParametersList = Column(JSON, nullable=True)
    ptwParametersList = Column(JSON, nullable=True)
    iabOperationAllowed = Column(Boolean, nullable=True)
    wirelineForbiddenAreas = Column(JSON, nullable=True)
    wirelineServiceAreaRestriction = Column(JSON, nullable=True)


class Amf3GppAccessRegistration(Base):
    __tablename__ = 'Amf3GppAccessRegistration'
    
    ueid = Column(String(15), primary_key=True)
    amfInstanceId = Column(String(50), nullable=False)
    supportedFeatures = Column(String(50), nullable=True)
    purgeFlag = Column(Boolean, nullable=True)
    pei = Column(String(50), nullable=True)
    imsVoPs = Column(JSON, nullable=True)
    deregCallbackUri = Column(String(50), nullable=False)
    amfServiceNameDereg = Column(JSON, nullable=True)
    pcscfRestorationCallbackUri = Column(String(50), nullable=True)
    amfServiceNamePcscfRest = Column(JSON, nullable=True)
    initialRegistrationInd = Column(Boolean, nullable=True)
    guami = Column(JSON, nullable=False)
    backupAmfInfo = Column(JSON, nullable=True)
    drFlag = Column(Boolean, nullable=True)
    ratType = Column(JSON, nullable=False)
    urrpIndicator = Column(Boolean, nullable=True)
    amfEeSubscriptionId = Column(String(50), nullable=True)
    epsInterworkingInfo = Column(JSON, nullable=True)
    ueSrvccCapability = Column(Boolean, nullable=True)
    registrationTime = Column(String(50), nullable=True)
    vgmlcAddress = Column(JSON, nullable=True)
    contextInfo = Column(JSON, nullable=True)
    noEeSubscriptionInd = Column(Boolean, nullable=True)


class AuthenticationStatus(Base):
    __tablename__ = 'AuthenticationStatus'
    
    ueid = Column(String(20), primary_key=True)
    nfInstanceId = Column(String(50), nullable=False)
    success = Column(Boolean, nullable=False)
    timeStamp = Column(String(50), nullable=False)
    authType = Column(String(25), nullable=False)
    servingNetworkName = Column(String(50), nullable=False)
    authRemovalInd = Column(Boolean, nullable=True)


class AuthenticationSubscription(Base):
    __tablename__ = 'AuthenticationSubscription'
    
    ueid = Column(String(20), primary_key=True)
    authenticationMethod = Column(String(25), nullable=False)
    encPermanentKey = Column(String(50), nullable=True)
    protectionParameterId = Column(String(50), nullable=True)
    sequenceNumber = Column(JSON, nullable=True)
    authenticationManagementField = Column(String(50), nullable=True)
    algorithmId = Column(String(50), nullable=True)
    encOpcKey = Column(String(50), nullable=True)
    encTopcKey = Column(String(50), nullable=True)
    vectorGenerationInHss = Column(Boolean, nullable=True)
    n5gcAuthMethod = Column(String(15), nullable=True)
    rgAuthenticationInd = Column(Boolean, nullable=True)
    supi = Column(String(20), nullable=True)


class SdmSubscriptions(Base):
    __tablename__ = 'SdmSubscriptions'
    
    subsId = Column(Integer, primary_key=True, autoincrement=True)
    ueid = Column(String(15), nullable=False)
    nfInstanceId = Column(String(50), nullable=False)
    implicitUnsubscribe = Column(Boolean, nullable=True)
    expires = Column(String(50), nullable=True)
    callbackReference = Column(String(50), nullable=False)
    amfServiceName = Column(JSON, nullable=True)
    monitoredResourceUris = Column(JSON, nullable=False)
    singleNssai = Column(JSON, nullable=True)
    dnn = Column(String(50), nullable=True)
    subscriptionId = Column(String(50), nullable=True)
    plmnId = Column(JSON, nullable=True)
    immediateReport = Column(Boolean, nullable=True)
    report = Column(JSON, nullable=True)
    supportedFeatures = Column(String(50), nullable=True)
    contextInfo = Column(JSON, nullable=True)


class SessionManagementSubscriptionData(Base):
    __tablename__ = 'SessionManagementSubscriptionData'
    
    ueid = Column(String(15), primary_key=True)
    servingPlmnid = Column(String(15), primary_key=True)
    singleNssai = Column(JSON, nullable=False)
    dnnConfigurations = Column(JSON, nullable=True)
    internalGroupIds = Column(JSON, nullable=True)
    sharedVnGroupDataIds = Column(JSON, nullable=True)
    sharedDnnConfigurationsId = Column(String(50), nullable=True)
    odbPacketServices = Column(JSON, nullable=True)
    traceData = Column(JSON, nullable=True)
    sharedTraceDataId = Column(String(50), nullable=True)
    expectedUeBehavioursList = Column(JSON, nullable=True)
    suggestedPacketNumDlList = Column(JSON, nullable=True)
    chargingCharacteristics3gpp = Column(String(50), nullable=True)


class SmfRegistrations(Base):
    __tablename__ = 'SmfRegistrations'
    
    ueid = Column(String(15), primary_key=True)
    subpduSessionId = Column(Integer, primary_key=True)
    smfInstanceId = Column(String(50), nullable=False)
    smfSetId = Column(String(50), nullable=True)
    supportedFeatures = Column(String(50), nullable=True)
    pduSessionId = Column(Integer, nullable=False)
    singleNssai = Column(JSON, nullable=False)
    dnn = Column(String(50), nullable=True)
    emergencyServices = Column(Boolean, nullable=True)
    pcscfRestorationCallbackUri = Column(String(50), nullable=True)
    plmnId = Column(JSON, nullable=False)
    pgwFqdn = Column(String(50), nullable=True)
    epdgInd = Column(Boolean, nullable=True)
    deregCallbackUri = Column(String(50), nullable=True)
    registrationReason = Column(JSON, nullable=True)
    registrationTime = Column(String(50), nullable=True)
    contextInfo = Column(JSON, nullable=True)


class SmfSelectionSubscriptionData(Base):
    __tablename__ = 'SmfSelectionSubscriptionData'
    
    ueid = Column(String(15), primary_key=True)
    servingPlmnid = Column(String(15), primary_key=True)
    supportedFeatures = Column(String(50), nullable=True)
    subscribedSnssaiInfos = Column(JSON, nullable=True)
    sharedSnssaiInfosId = Column(String(50), nullable=True)

