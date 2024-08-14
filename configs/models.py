from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class LastIndexesModel(BaseModel):
    ausf: int

class SequenceNumberModel(BaseModel):
    sqn: str
    sqnScheme: str
    lastIndexes: LastIndexesModel

class PduSessionTypesModel(BaseModel):
    defaultSessionType: str

class SscModesModel(BaseModel):
    defaultSscMode: str

class ArpModel(BaseModel):
    priorityLevel: int
    preemptCap: str
    preemptVuln: str

class QoSProfileModel(BaseModel):
    qi: int = Field(alias='5qi')
    arp: ArpModel
    priorityLevel: int

class SessionAmbrModel(BaseModel):
    uplink: str
    downlink: str

class StaticIpAddressModel(BaseModel):
    ipv4Addr: str

class DnnConfigurationsInnerModel(BaseModel):
    pduSessionTypes: PduSessionTypesModel
    sscModes: SscModesModel
    qosProfile: QoSProfileModel = Field(alias='5gQosProfile')
    sessionAmbr: SessionAmbrModel
    staticIpAddress: Optional[list[StaticIpAddressModel]] = None

class DnnConfigurationsModel(BaseModel):
    oai: DnnConfigurationsInnerModel
    ims: DnnConfigurationsInnerModel

class AuthenticationSubscriptionModel(BaseModel):
    ueid: str
    authenticationMethod: str
    encPermanentKey: str
    protectionParameterId: str
    sequenceNumber: SequenceNumberModel
    authenticationManagementField: str
    algorithmId: str
    encOpcKey: str
    encTopcKey: Optional[str] = None
    vectorGenerationInHss: Optional[str] = None
    n5gcAuthMethod: Optional[str] = None
    rgAuthenticationInd: Optional[str] = None
    supi: str

class SessionManagementSubscriptionDataModel(BaseModel):
    ueid: str
    servingPlmnid: str
    singleNssai: Dict[str, Any]
    dnnConfigurations: DnnConfigurationsModel