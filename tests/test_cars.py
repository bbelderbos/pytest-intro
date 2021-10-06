import pytest

from cars.cars import Car


@pytest.fixture
def car():
    print("making a car")
    return Car("defender", 2022)


@pytest.fixture
def car2():
    return Car.from_string("defender 2020")


@pytest.fixture
def car3():
    return Car.from_string("defender 2022")


@pytest.fixture
def car_with_mileage(car):
    car.add_mileage(10)
    car.add_mileage(20)
    return car


def test_creation_car(car):
    assert isinstance(car, Car)


def test_string_representation(car):
    assert str(car) == "Car: defender (2022)"


def test_add_mileage(car_with_mileage):
    assert car_with_mileage.miles_driven == 30


def test_mileage_report(car, capfd):
    car.add_mileage(10)
    car.add_mileage(20)
    car.mileage_report
    actual = capfd.readouterr().out
    expected = "10\n20\n---\n30\n"
    assert actual == expected


def test_create_car_from_string(car):
    assert str(car) == "Car: defender (2022)"


def test_gt_lt(car, car2):
    assert car > car2
    assert car2 < car


def test_eq(car, car3):
    assert car == car3
