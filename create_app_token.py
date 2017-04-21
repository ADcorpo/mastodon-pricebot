"""
Use this module to get applications credentials from the instance
you are targetting.

At the moment you have to manually replace the instance address, but
this will change in the near future.
"""

from mastodon import Mastodon

print("Please enter the full URL to your instance")
mastodon_instance = input()

Mastodon.create_app('MoneroPriceBot',
                    api_base_url=mastodon_instance,
                    to_file='apptoken.cfg')
