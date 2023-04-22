from utility import little_endian, unix_time
from hashlib import sha256
import numpy as np


# Block header
def block_header_generator(version, perv_block_hash, merkle_root, time, bits, utc):

    """Generates the block header."""

    version_hex = '{0:08x}'.format(little_endian(version))
    perv_hash_hex = '{0:064x}'.format(little_endian(perv_block_hash))
    merkle_hex = '{0:064x}'.format(little_endian(merkle_root))
    time_hex = '{0:08x}'.format(little_endian(unix_time(time, utc)))
    bits_hex = '{0:08x}'.format(little_endian('{0:08x}'.format(bits)))
    header = [version_hex, perv_hash_hex, merkle_hex, time_hex, bits_hex]

    return ''.join(header)


# Calculate Target
def target_cal(bits: int):
    """Calculates the target value for comparing."""

    h = '{0:08x}'.format(bits)
    return int(h[2:], 16) * (256 ** (int(h[:2], 16) - 3))


# Mine block
def mine(b_version, b_perv_hash, b_merkle, b_time, b_bits, near_value, utc=True):
    """Performs the process of mining."""

    nonce = near_value  # for speeding up the process
    target = target_cal(b_bits)
    b = block_header_generator(b_version, b_perv_hash, b_merkle, b_time, b_bits, utc)
    print('Start Mining ... ')
    while True:
        nonce_little = '{0:08x}'.format(little_endian('{0:08x}'.format(nonce)))
        header = b + nonce_little
        first_hash = sha256(bytes.fromhex(header))  # needs byte format
        second_hash = sha256(first_hash.digest()).hexdigest()
        result = int.from_bytes(bytearray.fromhex(second_hash), 'little')  # for comparing with the target
        if result < target:
            print('Block Mined ! ', 'Nonce : ', nonce, sep='\n')
            print('hash : ', '{0:064x}'.format(result), sep='\n')
            return '{0:064x}'.format(result)
        nonce += 1


# Mine block# function

def mine_block_num(number, df):
    """Given a block number it will mine that block."""

    b_version = '{0:08x}'.format(df.loc[number, 'version'])
    if number == 0:
        b_perv_hash = '00'
    else:
        b_perv_hash = df.loc[number - 1, 'hash']
    b_merkle = df.loc[number, 'merkle_root']
    b_time = df.loc[number, 'time']
    b_bits = df.loc[number, 'bits']
    nonce = df.loc[number, 'nonce']
    # For mining faster, we start from a close number to the reported nonce
    if nonce > 2e6:
        near_value = np.random.randint(nonce - 2e6, nonce - 1e6, dtype='int64')
    else:
        near_value = np.random.randint(1, nonce, dtype='int64')

    return mine(b_version, b_perv_hash, b_merkle, b_time, b_bits, near_value)
