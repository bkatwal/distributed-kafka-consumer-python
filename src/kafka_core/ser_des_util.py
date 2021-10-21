import json

from src.exceptions.usi_exceptions import BadConsumerConfigException

SER_DES_OPTIONS = {
    'STRING_SER': lambda k: k.encode('utf-8') if k is not None else k,
    'JSON_SER': lambda v: json.dumps(v).encode('utf-8') if v is not None else v,
    'STRING_DES': lambda k: k.decode('utf-8') if k is not None else k,
    'JSON_DES': lambda v: json.loads(v) if v is not None else v,

}


def get_ser_des(name: str):
    ser_des_cal = SER_DES_OPTIONS.get(name)
    if ser_des_cal is None:
        raise BadConsumerConfigException(f'No Serializer/Deserializer found with name {name}')
    return ser_des_cal
