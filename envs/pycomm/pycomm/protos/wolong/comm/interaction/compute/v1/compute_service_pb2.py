
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8wolong/comm/interaction/compute/v1/compute_service.proto\x12"wolong.comm.interaction.compute.v1".\n\x10BaseStationPower\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06powers\x18\x02 \x03(\x01"c\n\x1bComputeFacilityPowerRequest\x12D\n\x06powers\x18\x01 \x03(\x0b24.wolong.comm.interaction.compute.v1.BaseStationPower"3\n\rFacilityPower\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0efacility_power\x18\x02 \x01(\x01"j\n\x1cComputeFacilityPowerResponse\x12J\n\x0ffacility_powers\x18\x01 \x03(\x0b21.wolong.comm.interaction.compute.v1.FacilityPower2\xac\x01\n\x0eComputeService\x12\x99\x01\n\x14ComputeFacilityPower\x12?.wolong.comm.interaction.compute.v1.ComputeFacilityPowerRequest\x1a@.wolong.comm.interaction.compute.v1.ComputeFacilityPowerResponseb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.compute.v1.compute_service_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _BASESTATIONPOWER._serialized_start = 96
    _BASESTATIONPOWER._serialized_end = 142
    _COMPUTEFACILITYPOWERREQUEST._serialized_start = 144
    _COMPUTEFACILITYPOWERREQUEST._serialized_end = 243
    _FACILITYPOWER._serialized_start = 245
    _FACILITYPOWER._serialized_end = 296
    _COMPUTEFACILITYPOWERRESPONSE._serialized_start = 298
    _COMPUTEFACILITYPOWERRESPONSE._serialized_end = 404
    _COMPUTESERVICE._serialized_start = 407
    _COMPUTESERVICE._serialized_end = 579
