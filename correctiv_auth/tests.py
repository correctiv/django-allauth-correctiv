from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from allauth.socialaccount.providers import registry

from .provider import CorrectivProvider


class CorrectivTests(create_oauth2_tests(registry.by_id(CorrectivProvider.id))):
    def get_mocked_response(self):
        return MockedResponse(200, """{
  "first_name": "Stefan",
  "last_name": "Wehrmeyer",
  "email": "stefan.wehrmeyer@correctiv.org"
}""")
