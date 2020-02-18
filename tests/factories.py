import factory
from accounts.models import User


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = True
    is_superuser = False
