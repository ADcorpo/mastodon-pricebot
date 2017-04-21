"""
Use this module to get applications credentials from the instance
you are targetting.

At the moment you have to manually replace the instance address, but
this will change in the near future.
"""

from mastodon import Mastodon

import settings


Mastodon.create_app(settings.APP_NAME,
                    api_base_url=settings.INSTANCE_URL,
                    to_file='apptoken.cfg')
