from mastodon import Mastodon

mastodon_instance = input()
username = input()
password = input()

mastodon = Mastodon(client_id="apptoken.cfg",
                    api_base_url=mastodon_instance)

mastodon.log_in(username,
                password,
                to_file="usertoken.cfg")
