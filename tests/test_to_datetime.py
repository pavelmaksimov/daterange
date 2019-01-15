# -*- coding: utf-8 -*-
from datetime import datetime

import pendulum
import pytest

from daterangepy.daterange import _to_datetime


@pytest.mark.parametrize('dt', ['2018-01-01',
                                datetime.now().date(),
                                pendulum.now()])
def test_to_datetime(dt):
    result = _to_datetime(dt=dt)
    assert type(result) == type(datetime.now())
