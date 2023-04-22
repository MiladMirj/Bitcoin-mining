# #                                                        Code Surge !
# #                                                        Code Surge !
# #                                                        Code Surge !
# #                                                        Code Surge !
#                                                   https://github.com/MiladMirj
#                                           https://www.linkedin.com/in/milad-mirjalili-15147421a/
#                                    https://www.youtube.com/watch?v=AoX1OZt2K18
#
"""
Enjoy mining !
This script allows the user to input a block number and mine that particular block !
Run 'main.py'  to run the script.

In order to run this script it's required to install the following library.
1- `pandas` for importing the block data
and download the blockdata.txt from `https://bitcointalk.org/index.php?topic=5246271.0`

Other modules to run this script:
1- `utility` for processing time and number representation
2- `bitcoin_processing` for processing and mining the block

 """
from bitcoin_processing import mine_block_num
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('blockdata.txt', usecols=['id', 'hash', 'time', 'version',
                                               'merkle_root', 'nonce', 'bits', 'difficulty'])
    block_number = int(input('Please Enter the Block number : '))
    mine_block_num(block_number, df)
