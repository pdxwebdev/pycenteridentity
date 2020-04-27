import sys
from os.path import dirname
from unittest import TestCase
from centeridentity.api import CenterIdentity, User


sys.path.append(dirname(__file__) + '/..')


class Test(TestCase):

    def test_generate_service(self):
        service = CenterIdentity.generate('test_service')

        self.assertIsNotNone(service)

    def test_user_from_dict(self):

        user = CenterIdentity.user_from_dict({
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        })
        self.assertEqual(user.username, 'test_service')
        self.assertEqual(user.username_signature, 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=')
        self.assertEqual(user.public_key, '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d')

    def test_add_user(self):
        # just creating a service out of thin air
        ci = CenterIdentity(
            'L38yoTWooppsQD4FubNfg9BmhZSvec5jnQMxLKD3si2GHA3g9gJk',
            'test_service'
        )
        ci.service.domain = 'http://0.0.0.0:8000'
        # instantiate a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.user(data)
        post_data = {
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        }

        result = ci.add_user(post_data)
        self.assertDictEqual({'status': True}, result)

    def test_get_user(self):
        # just creating a service out of thin air
        ci = CenterIdentity(
            'L38yoTWooppsQD4FubNfg9BmhZSvec5jnQMxLKD3si2GHA3g9gJk',
            'test_service'
        )
        ci.service.domain = 'http://0.0.0.0:8000'

        # instantiate a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.user(data)
        post_data_for_add = {
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        }
        result = ci.add_user(post_data_for_add)

        post_data_for_get = {
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
        }
        user = ci.get_user(post_data_for_get)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'test_service')
        self.assertEqual(user.username_signature, 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=')
        self.assertEqual(user.public_key, '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d')

    def test_remove_user(self):
        # just creating a service out of thin air
        ci = CenterIdentity(
            'L38yoTWooppsQD4FubNfg9BmhZSvec5jnQMxLKD3si2GHA3g9gJk',
            'test_service'
        )
        ci.service.domain = 'http://0.0.0.0:8000'

        # instantiate a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.user(data)
        post_data_for_add = {
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d'
        }
        result = ci.add_user(post_data_for_add)
        self.assertDictEqual(result, {'status': True})

        post_data_for_get = {
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
        }
        user = ci.get_user(post_data_for_get)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'test_service')
        self.assertEqual(user.username_signature, 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=')
        self.assertEqual(user.public_key, '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d')

        user = ci.remove_user(post_data_for_add)
        user = ci.get_user(post_data_for_get)
        self.assertIsNone(user)

    def test_authenticate_user(self):
        # instantiate a user from a dict that should come from another center identity library
        # you should not have to create a dict manually
        # should be CenterIdentity.user(data)
        ci = CenterIdentity(
            'L38yoTWooppsQD4FubNfg9BmhZSvec5jnQMxLKD3si2GHA3g9gJk',
            'test_service'
        )
        ci.service.domain = 'http://0.0.0.0:8000'
        post_data = {
            'username': 'test_service',
            'username_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M=',
            'public_key': '030727d998882093dea970377f50e5d203ac805003e9c9b390aed3ae6bda05460d',
            'session_id_signature': 'MEUCIQDMGiwL5unMr4joJTWaNudo0NeIqGIkK/+DeQNK3wdeqgIgIWmqe2vILDcA1TPxNDuXJavt6K5MEUtJgZRF4q7LB1M='
        }

        session_id = 'test_service'

        result = ci.authenticate(
            session_id,
            post_data,
            hash_session_id=False
        )
        self.assertIsInstance(result, User)
