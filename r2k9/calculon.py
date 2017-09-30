import ethereum.utils as utils
import ethereum.genesis_helpers as genesis
from ethereum.block import Block, BlockHeader
from ethereum.pow.chain import Chain
from ethereum.state import State
from ethereum.config import Env
from ethereum.messages import apply_transaction
from ethereum.transactions import Transaction
import serpent

wallet_addr = '0x768965600E99d6c7ffE6398790dB4ba397ECC43d'

class Calculon:

    def __init__(self):
        self.wallet_addr = wallet_addr

    def test(self):
        print('running test with {}'.format(self.wallet_addr))
        key = utils.sha3('party of the fist part')
        key2 = utils.sha3('party of the second part')
        addr = utils.privtoaddr(key)
        addr2 = utils.privtoaddr(key2)

        env = Env()
        state = State(env=env)
        #g = genesis.mk_genesis_block({addr:10**18})
        g = genesis.mk_genesis_block(env)
        print(dir(g))
        da = state.account_to_dict(addr)
        print(da)
        tx = Transaction(0, 1000, 21000, addr2, 56789000, "").sign(key)
        success, data = apply_transaction(state, tx)
        print(success)
        print(data)
        print('test finished')


if __name__ == '__main__':
    c = Calculon()
    c.test()


