from seasons import HowOld
from datetime import date
import pytest


def test_minutes_calculation():
    # 1 Year
    birth = "2022-01-01"
    today = date(2023, 1, 1)
    p = HowOld(birth, today)
    assert p.calculate_minutes() == 525600

    # 2 Years with lear year
    birth_leap = "2020-01-01"
    today_leap = date(2022, 1, 1)
    p_leap = HowOld(birth_leap, today_leap)
    assert p_leap.calculate_minutes() == 1052640


def test_invalid_date():
    # Invalid Dates
    with pytest.raises(SystemExit):
        HowOld("February 6th, 1998", date.today())
    with pytest.raises(SystemExit):
        HowOld("1998-13-40", date.today())
