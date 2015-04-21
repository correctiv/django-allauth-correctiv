from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class CorrectivAccount(ProviderAccount):

    def to_str(self):
        default = super(CorrectivAccount, self).to_str()
        first_name = self.account.extra_data.get('first_name', '')
        last_name = self.account.extra_data.get('last_name', '')
        name = ('%s %s' % (first_name, last_name)).strip()
        return name or default


class CorrectivProvider(OAuth2Provider):
    id = 'correctiv'
    name = 'Correctiv.org'
    package = 'correctiv_auth'
    account_class = CorrectivAccount

    def extract_uid(self, data):
        return str(data['email'])

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    last_name=data.get('last_name'),
                    first_name=data.get('first_name'))


providers.registry.register(CorrectivProvider)
