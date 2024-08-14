import oai_cn_5g_webui.db as db
import oai_cn_5g_webui.db.models as models
from configs.models import AuthenticationSubscriptionModel, SessionManagementSubscriptionDataModel

auth_sub_data = {
    'ueid': '001010000000001',
    'authenticationMethod': '5G_AKA',
    'encPermanentKey': 'fec86ba6eb707ed08905757b1bb44b8f',
    'protectionParameterId': 'fec86ba6eb707ed08905757b1bb44b8f',
    'sequenceNumber': '{"sqn": "000000000000", "sqnScheme": "NON_TIME_BASED", "lastIndexes": {"ausf": 0}}',
    'authenticationManagementField': '8000',
    'algorithmId': 'milenage',
    'encOpcKey': 'C42449363BBAD02B66D16BC975D77CC1',
    'encTopcKey': None,
    'vectorGenerationInHss': None,
    'n5gcAuthMethod': None,
    'rgAuthenticationInd': None,
    'supi': '001010000000001'
}

session_mgmt_data = {
    'ueid': '001010000000001',
    'servingPlmnid': '00101',
    'singleNssai': '{"sst": 1, "sd": "FFFFFF"}',
    'dnnConfigurations': '{"oai":{"pduSessionTypes":{ "defaultSessionType": "IPV4"},"sscModes": {"defaultSscMode": "SSC_MODE_1"},"5gQosProfile": {"5qi": 6,"arp":{"priorityLevel": 15,"preemptCap": "NOT_PREEMPT","preemptVuln":"PREEMPTABLE"},"priorityLevel":1},"sessionAmbr":{"uplink":"1000Mbps", "downlink":"1000Mbps"},"staticIpAddress":[{"ipv4Addr": "10.0.0.2"}]},"ims":{"pduSessionTypes":{ "defaultSessionType": "IPV4V6"},"sscModes": {"defaultSscMode": "SSC_MODE_1"},"5gQosProfile": {"5qi": 2,"arp":{"priorityLevel": 15,"preemptCap": "NOT_PREEMPT","preemptVuln":"PREEMPTABLE"},"priorityLevel":1},"sessionAmbr":{"uplink":"1000Mbps", "downlink":"1000Mbps"}}}'
}

class User():
    def __init__(self, auth_sub_data: AuthenticationSubscriptionModel, session_mgmt_data: SessionManagementSubscriptionDataModel):
        self._auth_sub_data = auth_sub_data
        self._session_mgmt_data = session_mgmt_data

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass

    def get_user(self):
        pass

    def get_active_users(self):
        pass
