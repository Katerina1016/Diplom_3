from faker import Faker
import allure


class UserData:
    @staticmethod
    @allure.step('Сгенерировать имя, адрес электронной почты и пароль')
    def create_correct_user_data():
        faker = Faker('ru_RU')
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return data
