from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers: list[dict],
        hall_number: int,
        cleaner: str,
) -> None:

    hall = CinemaHall(number=hall_number)

    customer_objects = []
    for customer in customers:
        obj = Customer(customer["name"])
        CinemaBar.sell_product(obj.food, obj)
        customer_objects.append(obj)

    hall.movie_session(movie, customer_objects, Cleaner(cleaner))
