from mastodon import Mastodon

import settings


username = input()
password = input()

mastodon = Mastodon(client_id="apptoken.cfg",
                    api_base_url=settings.INSTANCE_URL)

mastodon.log_in(username,
                password,
                to_file="usertoken.cfg")
