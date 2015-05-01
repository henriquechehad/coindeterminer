# -*- coding: utf-8 -*-


class CoinDeterminer():

    # List of available coins
    coins = [1, 5, 7, 9, 11]

    # Calculate minimal total of coins
    def get_coins_total(self, value):

        # Integer "value" attr validation
        try:
            value = int(value)
        except:
            return

        # Fill the list of coins used with initial values
        used_coins = [0] * (value + 1)

        # Fill the list of min coins with initial values
        min_coins = [0] * (value + 1)

        for val in range(value + 1):
            coin_val = val
            new = 1

            # Get list of values by coins
            for j in [c for c in self.coins if c <= val]:
                if min_coins[val-j] + 1 < coin_val:
                    coin_val = min_coins[val-j]+1
                    new = j

            min_coins[val] = coin_val
            used_coins[val] = new

        return min_coins[value]



