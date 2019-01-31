import unittest
from marmopy import Contract, ERC20, Wallet, Conf, Intent


class IntentGenericTests(unittest.TestCase):
    def setUp(self):
        self.conf = Conf(
            "0xe814f48c2eaf753ae51c7c807e2b1736700126c58af556d78c7c6158d201a125",
            "0x4E0B13eDeE810702884b72DBE018579Cb2e4C6fA",
            "",
            999
        )

        abi = """
        [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"PRICE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"beneficiary","type":"address"}],"name":"buyTokens","outputs":[],"payable":true,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"CreatedToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
        """

        self.token_address = "0x6B0F919A5d450Fa5e6283Ff6178dC1FCd195FD2A"
        self.wallet = Wallet("0x5ef1dbf8ef171b33cd72a5d11b713442dcd2c70695753a0f6df9b38136e08d54", self.conf)

        self.ERC20 = Contract(abi)

    def test_transfer(self):
        intent_action = self.ERC20(self.token_address).transfer({"_to": "0x009ab4de1234c7066197d6ed75743add3576591f", "_value": 4})

        intent = Intent(
            intent_action=intent_action,
            expiration=1548030494,
            max_gas_price=10 ** 32
        )

        self.assertEqual(intent.id(self.wallet), "0xe34f44ab2514803ba5f1a4766f5fe1d6d012a9599c8e13843962366f04427198")

    def test_intent_with_dependency(self):
        dependency_signed_intent = self.wallet.sign(Intent(
            intent_action = ERC20(
                "0x6B0F919A5d450Fa5e6283Ff6178dC1FCd195FD2A"
            ).transfer("0x009ab4de1234c7066197d6ed75743add3576591f", 0),
            expiration = 10 ** 32
        ))

        intent_action = self.ERC20(self.token_address).transfer({"_to": "0x009ab4de1234c7066197d6ed75743add3576591f", "_value": 100 * 10 ** 18})

        intent = Intent(
            intent_action=intent_action,
            expiration=10 ** 36
        )

        intent.add_dependency(dependency_signed_intent)

        self.assertEqual(intent.id(self.wallet), "0x0f1a91058c267c034e020aa4651b59e4d459ec7314225de3865217bec8bfefdc")

if __name__ == '__main__':
    unittest.main()
