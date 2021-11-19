def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def throw_if_unvalid_amount(value):
    if not isinstance(value, float):
        raise Exception('Amount must be float!')
    if value <= 0:
        raise Exception('Amount must be greater than 0!')
