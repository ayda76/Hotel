from pytest_factoryboy import register

from factories.account_factory import UserFactory,AccountFactory,GuestFactory,EmployeeFactory

register(UserFactory)

register(AccountFactory)
register(GuestFactory)
register(EmployeeFactory)