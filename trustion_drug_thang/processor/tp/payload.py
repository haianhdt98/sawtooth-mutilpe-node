from sawtooth_sdk.processor.exceptions import InvalidTransaction

from protobuf import payload_pb2


class SupplyPayload(object):

    def __init__(self, payload):
        self._transaction = payload_pb2.SimpleSupplyPayload()
        self._transaction.ParseFromString(payload)

    @property
    def action(self):
        return self._transaction.action

    @property
    def data(self):
        if self._transaction.HasField('create_user') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.CREATE_USER:
            return self._transaction.create_user

        if self._transaction.HasField('drug_import') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.DRUG_IMPORT:
            return self._transaction.drug_import
            
        if self._transaction.HasField('company_import') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.COMPANY_IMPORT:
            return self._transaction.company_import

        if self._transaction.HasField('employee_import') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.EMPLOYEE_IMPORT:
            return self._transaction.employee_import

        if self._transaction.HasField('update_status') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.UPDATE_STATUS:
            return self._transaction.update_status
        if self._transaction.HasField('update_location') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.UPDATE_LOCATION:
            return self._transaction.update_location

        if self._transaction.HasField('update_company') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.UPDATE_COMPANY:
            return self._transaction.update_company
        if self._transaction.HasField('update_employee') and \
            self._transaction.action == \
                payload_pb2.SimpleSupplyPayload.UPDATE_EMPLOYEE:
            return self._transaction.update_employee

        raise InvalidTransaction('Action does not match payload data')

    @property
    def timestamp(self):
        return self._transaction.timestamp