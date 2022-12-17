from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from car_auth.models import AppUser
from car.models import Car

UserModel = get_user_model()


class TestAppViews(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': '12345qwe',
    }

    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user

    @staticmethod
    def _create_car(user):
        test_user = user
        car = Car(
            car_make="BMW",
            car_model="M3",
            engine_type='Gasoline',
            price=20200,
            mileage=100000,
            model_year=2006,
            current_location='Sofia',
            contact_number='0896877082',
            description='Really fun!',
            user_id=test_user.id,
        )
        car.save()
        return car

    def test_about_us_page_loads_successfully(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_loads_successfully(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)

    def test_create_create_listing_opens_when_user_logged_in(self):
        AppUser.objects.create_user(username=self.VALID_USER_DATA['username'],
                                    password=self.VALID_USER_DATA['password'])

        self.client.login(username=self.VALID_USER_DATA['username'],
                          password=self.VALID_USER_DATA['password'])

        response = self.client.get('/create_listing')

        self.assertEqual(response.status_code, 200)

    def test_create_create_listing_NOT_open_when_user_NOT_logged_in(self):
        response = self.client.get('/create_listing')

        self.assertEqual(response.status_code, 302)

        url = response['location']

        self.assertIn('/accounts/login/?next=/create_listing', url)

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('profile', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('profile', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_car_details_page_loaded_when_is_owner(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        car_ad = self._create_car(user)
        car_ad.save()

        response = self.client.get(f'/{user.username}/car/{car_ad.slug}/')

        self.assertEqual(response.status_code, 200)

        url = response.wsgi_request.path

        self.assertEqual(f'/{user.username}/car/{car_ad.slug}/', url)
        self.assertContains(response, car_ad.description)

    def test_car_details_page_loaded_when_is_NOT_owner(self):
        create_user = UserModel.objects.create_user(
            username=self.VALID_USER_DATA['username'] + '1',
            email=self.VALID_USER_DATA['email'] + '1',
            password=self.VALID_USER_DATA['password'],
        )

        car_ad = self._create_car(create_user)
        car_ad.save()

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(f'/{create_user.username}/car/{car_ad.slug}/')

        self.assertFalse(response.context['is_owner'])

    def test_user_my_listings__when_is_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('my listings', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])
        self.assertEqual(response.status_code, 200)

    def test_user_my_listings__when_owner__expect_is_owner_false(self):
        create_user = UserModel.objects.create_user(
            username=self.VALID_USER_DATA['username'] + '1',
            email=self.VALID_USER_DATA['email'] + '1',
            password=self.VALID_USER_DATA['password'],
        )

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('my listings', kwargs={'pk': create_user.pk}))

        self.assertFalse(response.context['is_owner'])
