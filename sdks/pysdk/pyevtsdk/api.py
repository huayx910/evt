import requests


class Api:
    def __init__(self, host='https://testnet1.everitoken.io:8888'):
        self.host = host
        self.urls = {
            'abi_json_to_bin': '/v1/chain/abi_json_to_bin',
            'trx_json_to_digest': '/v1/chain/trx_json_to_digest',
            'get_required_keys': '/v1/chain/get_required_keys',
            'push_transaction': '/v1/chain/push_transaction',
            'get_domain': '/v1/evt/get_domain',
            'get_group': '/v1/evt/get_group',
            'get_token': '/v1/evt/get_token',
            'get_fungible': '/v1/evt/get_fungible',
            'get_tokens': '/v1/history/get_tokens',
            'get_domains': '/v1/history/get_domains',
            'get_groups': '/v1/history/get_groups',
            'get_fungibles': '/v1/history/get_fungibles',
            'get_actions': '/v1/history/get_actions',
            'get_fungible_actions': '/v1/history/get_fungible_actions',
            'get_transaction': '/v1/history/get_transaction',
            'get_transactions': '/v1/history/get_transactions'
        }

    def __getattr__(self, api_name):
        url = self.host + self.urls[api_name]

        def ret_func(data):
            return requests.post(url, data=data)
        return ret_func

    def get_info(self):
        return requests.get(self.host+'/v1/chain/get_info').text
