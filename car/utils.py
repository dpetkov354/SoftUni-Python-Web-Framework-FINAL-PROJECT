from car.models import Car


def get_car_by_name_and_username(car_slug, username):
    return Car.objects \
        .filter(slug=car_slug, user__username=username) \
        .get()
