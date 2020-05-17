from django.test import TestCase


class PeopleEndpointTestCase(TestCase):
    def setUp(self) -> None:
        super.setup()
        # Do the rest of the setup for logging in the user and giving the user
        # required permissions

    def test_people_endpoint_post_data(self):
        """Test Posting to the endpoint with valid and invalid data."""
        url = '/api/people/'
        minimum_required_data = {
            "first_name": "Joe",
            "last_name": "Shmo",
            "address": "123 fake Street"
        }

        # Posting with all of the required data
        response = self.client.post(
            url,
            data=minimum_required_data,
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # POSTing with the first_name missing
        data = minimum_required_data.copy()
        data.pop("first_name")
        response = self.client.post(
            url,
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

        missing_subtests = (
            # A tuple of (field_name, subtest_description)
            ('first_name', 'Missing the first_name field'),
            ('last_name', 'Missing the last_name field'),
            ('address', 'Missing the address field'),
        )

        for field_name, subtest_description in missing_subtests:
            with self.subTest(subtest_description):
                # remove the missing field from the minimum_required_data
                data = minimum_required_data.copy()
                data.pop(field_name)

                # POSTing with the missing field name
                response = self.client.post(
                    url,
                    data=data,
                    content_type='application/json'
                )
                self.assertEqual(response.status_code, 400)

