import pytest

from cars.cars import Car


@pytest.fixture
def defender_car():
    return Car("defender", 2022)


@pytest.fixture
def older_defender_car():
    return Car("defender", 2020)


@pytest.fixture
def same_defender_made_from_str():
    return Car.from_string("defender 2022")


@pytest.fixture
def defender_car_with_mileage(defender_car):
    defender_car.add_mileage(10)
    defender_car.add_mileage(20)
    # if you need teardown logic yield the car instead
    return defender_car


def test_creation_car(defender_car):
    assert isinstance(defender_car, Car)


def test_string_representation(defender_car):
    assert str(defender_car) == "Car: defender (2022)"


def test_add_mileage(defender_car_with_mileage):
    assert defender_car_with_mileage.miles_driven == 30


def test_mileage_report(defender_car_with_mileage, capfd):
    defender_car_with_mileage.mileage_report
    actual = capfd.readouterr().out
    expected = "10\n20\n---\n30\n"
    assert actual == expected


def test_create_car_from_string(same_defender_made_from_str):
    assert str(same_defender_made_from_str) == "Car: defender (2022)"


def test_gt_lt_dunder_methods(defender_car, older_defender_car):
    assert defender_car > older_defender_car
    assert older_defender_car < defender_car


def test_eq_funder_method(defender_car, same_defender_made_from_str):
    assert defender_car == same_defender_made_from_str
