import sys
from os.path import dirname
from unittest import TestCase
from centeridentity.api import CenterIdentity


sys.path.append(dirname(__file__) + '/..')


class Test(TestCase):

    def test_revive_user(self):

        user = CenterIdentity.revive_user({
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        })
        self.assertEqual(user.username, 'test_service')
        self.assertEqual(user.username_signature, 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=')
        self.assertEqual(user.public_key, '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d')

    def test_add_user(self):
        # just creating a service out of thin air
        service = CenterIdentity.revive_service(
            'test_service',
            'L38yoTWooppsQD4FubNfg9BmhZSvec5jnQMxLKD3si2GHA3g9gJk'
        )
        print(service.username_signature)
        ci = CenterIdentity(service)

        # revive a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.revive_user(data)
        user = CenterIdentity.revive_user({
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        })

        result = ci.add_user(user)
        self.assertDictEqual({'status': True}, result)

    def test_authenticate_user(self):
        # revive a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.revive_user(data)
        user = CenterIdentity.revive_user({
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        })

        session_id_signature = 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M='
        result = CenterIdentity.authenticate(
            session_id_signature,
            'test_service',
            user
        )
        self.assertEqual(result, True)
