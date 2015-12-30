from trezor import TrezorPlugin
from electrum.util import print_msg
from electrum.plugins import hook

class TrezorCmdLineHandler:

    def get_passphrase(self, msg):
        import getpass
        print_msg(msg)
        return getpass.getpass('')

    def get_pin(self, msg):
        t = { 'a':'7', 'b':'8', 'c':'9', 'd':'4', 'e':'5', 'f':'6', 'g':'1', 'h':'2', 'i':'3'}
        print_msg(msg)
        print_msg("a b c\nd e f\ng h i\n-----")
        o = raw_input()
        return ''.join(map(lambda x: t[x], o))

    def stop(self):
        pass

    def show_message(self, msg):
        print_msg(msg)


class Plugin(TrezorPlugin):

    @hook
    def cmdline_load_wallet(self, wallet):
        if type(wallet) != self.wallet_class:
            return
        wallet.plugin = self
        if self.handler is None:
            self.handler = TrezorCmdLineHandler()
