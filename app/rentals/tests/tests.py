import pytest
from fleet.models.car import Car
from rentals.models.rental import Rental
from datetime import date
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_should_create_rental_with_correct_car(sample_car):
    # Arrange
    start_date = date(2026,5,10)
    end_date = date(2026,5,5)

    # Act 
    rental = Rental.objects.create(
        car = sample_car, 
        start_date = date(2026,5,10), 
        end_date = date(2026,5,5)
        )

    # Assert 
    assert rental.car.brand == "Tesla"
    assert Rental.objects.count() == 1

    with pytest.raises(ValidationError):
        rental.full_clean()