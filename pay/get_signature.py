import crypt
import hashlib
from collections import OrderedDict


MERCHANT_ID = 535456
SECRET ="LeFnP16MP6AU6YKc"


def get_sig(param):
    """init_payment.php;25;test;{{paybox_merchant_id}};23;molbulak;{{secret_key}}"""
    sig = 'init_payment.php'
    ordered_dict = OrderedDict(sorted(param.items()))
    for key, value in ordered_dict.items():
        sig += ';' + str(value)
    sig += ';' + SECRET
    hashed_sig = hashlib.md5(sig.encode()).hexdigest()
    return hashed_sig


def get_salt():
    return crypt.mksalt(crypt.METHOD_SHA512)
