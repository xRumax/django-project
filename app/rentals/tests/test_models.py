import pytest
from rentals.models.rental import Rental
from datetime import date
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_should_create_rental(sample_car): 
    rental = Rental.objects.create(
        car = sample_car, 
        start_date = date(2026,5,1), 
        end_date = date(2026,5,5)
        )
    
    assert rental.car == sample_car

@pytest.mark.django_db
def test_should_not_allow_invalid_dates(sample_car):
    with pytest.raises(ValidationError):
        rental = Rental(
            car=sample_car,
            start_date=date(2026,5,10),
            end_date=date(2026,5,5)
        )
        rental.full_clean()