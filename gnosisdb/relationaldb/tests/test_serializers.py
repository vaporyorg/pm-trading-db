from unittest import TestCase
from relationaldb.factories import CentralizedOracleFactory
from relationaldb.serializers import CentralizedOracleSerializer


class TestSerializers(TestCase):
    def test_centralized_oracle(self):
        oracle = CentralizedOracleFactory()

        block = {
            'number': oracle.creation_block,
            'creationDate': oracle.creation_date
        }

        oracle_event = {
            'address': oracle.factory,
            'params': [
                {
                    'name': 'creator',
                    'value': oracle.creator
                },
                {
                    'name': 'centralizedOracle',
                    'value': oracle.address
                },
                # {
                #     'name': 'ipfsHash',
                #     'value': oracle.event_description
                # }
            ]
        }

        s = CentralizedOracleSerializer(data=oracle_event, block=block)
        self.assertTrue(s.is_valid(), s.errors)
        instance = s.save()
        self.assertIsNotNone(instance)
