# -*- coding: utf-8 -*-
from datetime import datetime

import pytest

from daterangepy.daterange import period_range, frequency_dates


@pytest.mark.parametrize('start_date,end_date,'
                         'delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-01', '2017-01-01', 1, False, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-01', 1, True, True, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-01', 1, True, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-01', 1, False, True, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-03', 1, False, False, '2017-01-01', '2017-01-01', 3),
                             ('2017-01-01', '2017-01-03', 1, True, True, '2017-01-01', '2017-01-01', 3),
                             ('2017-01-01', '2017-01-03', 1, True, False, '2017-01-01', '2017-01-01', 3),
                             ('2017-01-01', '2017-01-03', 1, False, True, '2017-01-01', '2017-01-01', 3),
                             ('2017-01-01', '2017-01-01', 2, False, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-01', 2, True, True, '2017-01-01', '2017-01-02', 1),
                             ('2017-01-01', '2017-01-01', 2, True, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', '2017-01-01', 2, False, True, '2017-01-01', '2017-01-02', 1),

                             ('2017-01-01', '2017-01-10', 30, True, False, '2017-01-01', '2017-01-10', 1),
                             ('2017-01-01', '2017-01-10', 5, True, False, '2017-01-01', '2017-01-05', 2),
                         ])
def test_period_day_range(start_date, end_date,
                          delta,
                          result_date1, result_date2,
                          start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency,
                          lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='day', delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'num,delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-01', None, 1, 1, False, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', None, 1, 1, True, True, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', None, 1, 1, False, True, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', None, 1, 1, True, False, '2017-01-01', '2017-01-01', 1),
                             ('2017-01-01', None, 2, 1, False, False, '2017-01-01', '2017-01-01', 2),
                             ('2017-01-01', None, 2, 1, True, True, '2017-01-01', '2017-01-01', 2),
                             ('2017-01-01', None, 2, 1, False, True, '2017-01-01', '2017-01-01', 2),
                             ('2017-01-01', None, 2, 1, True, False, '2017-01-01', '2017-01-01', 2),

                             ('2017-01-01', None, 2, 2, False, False, '2017-01-01', '2017-01-02', 1),
                             ('2017-01-01', None, 2, 2, True, True, '2017-01-01', '2017-01-02', 1),
                             ('2017-01-01', None, 2, 2, False, True, '2017-01-01', '2017-01-02', 1),
                             ('2017-01-01', None, 2, 2, True, False, '2017-01-01', '2017-01-02', 1),
                             ('2017-01-01', None, 3, 2, False, False, '2017-01-01', '2017-01-02', 2),
                             ('2017-01-01', None, 3, 2, True, True, '2017-01-01', '2017-01-02', 2),
                             ('2017-01-01', None, 3, 2, False, True, '2017-01-01', '2017-01-02', 2),
                             ('2017-01-01', None, 3, 2, True, False, '2017-01-01', '2017-01-02', 2),
                         ])
def test_period_day_without_end_date_range(start_date, end_date,
                                           num, delta,
                                           result_date1, result_date2,
                                           start_date_adjustment_by_frequency,
                                           end_date_adjustment_by_frequency,
                                           lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='day', num=num, delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'num,delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-02', '2017-01-08', None, 1, False, False, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, True, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, False, True, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, False, '2017-01-02', '2017-01-08', 1),

                             ('2017-01-03', '2017-01-07', None, 1, False, False, '2017-01-03', '2017-01-07', 1),
                             ('2017-01-03', '2017-01-07', None, 1, True, True, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-03', '2017-01-07', None, 1, False, True, '2017-01-03', '2017-01-08', 1),
                             ('2017-01-03', '2017-01-07', None, 1, True, False, '2017-01-02', '2017-01-07', 1),

                             ('2017-01-03', '2017-01-14', None, 2, False, False, '2017-01-03', '2017-01-14', 1),
                             ('2017-01-03', '2017-01-14', None, 2, True, True, '2017-01-02', '2017-01-15', 1),
                             ('2017-01-03', '2017-01-14', None, 2, False, True, '2017-01-03', '2017-01-15', 1),
                             ('2017-01-03', '2017-01-14', None, 2, True, False, '2017-01-02', '2017-01-14', 1),

                             ('2017-01-03', '2017-01-20', None, 2, False, False, '2017-01-03', '2017-01-15', 2),
                             ('2017-01-03', '2017-01-20', None, 2, True, True, '2017-01-02', '2017-01-15', 2),
                             ('2017-01-03', '2017-01-20', None, 2, False, True, '2017-01-03', '2017-01-15', 2),
                             ('2017-01-03', '2017-01-20', None, 2, True, False, '2017-01-02', '2017-01-15', 2),

                             ('2017-01-03', '2017-01-14', None, 1, False, False, '2017-01-03', '2017-01-08', 2),
                             ('2017-01-03', '2017-01-14', None, 1, True, True, '2017-01-02', '2017-01-08', 2),
                             ('2017-01-03', '2017-01-14', None, 1, False, True, '2017-01-03', '2017-01-08', 2),
                             ('2017-01-03', '2017-01-14', None, 1, True, False, '2017-01-02', '2017-01-08', 2),
                         ])
def test_period_week_range(start_date, end_date,
                           num, delta,
                           result_date1, result_date2,
                           start_date_adjustment_by_frequency,
                           end_date_adjustment_by_frequency,
                           lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='week', num=num, delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'num,delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-02', '2017-01-08', None, 1, False, False, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, True, '2017-01-01', '2017-01-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, False, True, '2017-01-02', '2017-01-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, False, '2017-01-01', '2017-01-08', 1),

                             ('2017-01-03', '2017-02-14', None, 2, False, False, '2017-01-03', '2017-02-14', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, True, '2017-01-01', '2017-02-28', 1),
                             ('2017-01-03', '2017-02-14', None, 2, False, True, '2017-01-03', '2017-02-28', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, False, '2017-01-01', '2017-02-14', 1),

                             ('2017-01-03', '2017-02-14', None, 1, False, False, '2017-01-03', '2017-01-31', 2),
                             ('2017-01-03', '2017-02-14', None, 1, True, True, '2017-01-01', '2017-01-31', 2),
                             ('2017-01-03', '2017-02-14', None, 1, False, True, '2017-01-03', '2017-01-31', 2),
                             ('2017-01-03', '2017-02-14', None, 1, True, False, '2017-01-01', '2017-01-31', 2),

                             ('2017-01-03', '2017-03-14', None, 2, False, False, '2017-01-03', '2017-02-28', 2),
                             ('2017-01-03', '2017-03-14', None, 2, True, True, '2017-01-01', '2017-02-28', 2),
                             ('2017-01-03', '2017-03-14', None, 2, False, True, '2017-01-03', '2017-02-28', 2),
                             ('2017-01-03', '2017-03-14', None, 2, True, False, '2017-01-01', '2017-02-28', 2),
                         ])
def test_period_month_range(start_date, end_date,
                            num, delta,
                            result_date1, result_date2,
                            start_date_adjustment_by_frequency,
                            end_date_adjustment_by_frequency,
                            lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='month', num=num, delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'num,delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-02', '2017-01-08', None, 1, False, False, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, True, '2017-01-01', '2017-03-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, False, True, '2017-01-02', '2017-03-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, False, '2017-01-01', '2017-01-08', 1),

                             ('2017-01-03', '2017-02-14', None, 2, False, False, '2017-01-03', '2017-02-14', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, True, '2017-01-01', '2017-06-30', 1),
                             ('2017-01-03', '2017-02-14', None, 2, False, True, '2017-01-03', '2017-06-30', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, False, '2017-01-01', '2017-02-14', 1),

                             ('2017-01-03', '2017-04-14', None, 1, False, False, '2017-01-03', '2017-03-31', 2),
                             ('2017-01-03', '2017-04-14', None, 1, True, True, '2017-01-01', '2017-03-31', 2),
                             ('2017-01-03', '2017-04-14', None, 1, False, True, '2017-01-03', '2017-03-31', 2),
                             ('2017-01-03', '2017-04-14', None, 1, True, False, '2017-01-01', '2017-03-31', 2),

                             ('2017-01-03', '2017-07-14', None, 2, False, False, '2017-01-03', '2017-06-30', 2),
                             ('2017-01-03', '2017-07-14', None, 2, True, True, '2017-01-01', '2017-06-30', 2),
                             ('2017-01-03', '2017-07-14', None, 2, False, True, '2017-01-03', '2017-06-30', 2),
                             ('2017-01-03', '2017-07-14', None, 2, True, False, '2017-01-01', '2017-06-30', 2),
                         ])
def test_period_quarter_range(start_date, end_date,
                              num, delta,
                              result_date1, result_date2,
                              start_date_adjustment_by_frequency,
                              end_date_adjustment_by_frequency,
                              lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='quarter', num=num, delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'num,delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency,'
                         'result_date1,result_date2,'
                         'lenght',
                         [
                             ('2017-01-02', '2017-01-08', None, 1, False, False, '2017-01-02', '2017-01-08', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, True, '2017-01-01', '2017-12-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, False, True, '2017-01-02', '2017-12-31', 1),
                             ('2017-01-02', '2017-01-08', None, 1, True, False, '2017-01-01', '2017-01-08', 1),

                             ('2017-01-03', '2017-02-14', None, 2, False, False, '2017-01-03', '2017-02-14', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, True, '2017-01-01', '2018-12-31', 1),
                             ('2017-01-03', '2017-02-14', None, 2, False, True, '2017-01-03', '2018-12-31', 1),
                             ('2017-01-03', '2017-02-14', None, 2, True, False, '2017-01-01', '2017-02-14', 1),

                             ('2017-01-03', '2018-04-14', None, 1, False, False, '2017-01-03', '2017-12-31', 2),
                             ('2017-01-03', '2018-04-14', None, 1, True, True, '2017-01-01', '2017-12-31', 2),
                             ('2017-01-03', '2018-04-14', None, 1, False, True, '2017-01-03', '2017-12-31', 2),
                             ('2017-01-03', '2018-04-14', None, 1, True, False, '2017-01-01', '2017-12-31', 2),

                             ('2017-01-03', '2019-07-14', None, 2, False, False, '2017-01-03', '2018-12-31', 2),
                             ('2017-01-03', '2019-07-14', None, 2, True, True, '2017-01-01', '2018-12-31', 2),
                             ('2017-01-03', '2019-07-14', None, 2, False, True, '2017-01-03', '2018-12-31', 2),
                             ('2017-01-03', '2019-07-14', None, 2, True, False, '2017-01-01', '2018-12-31', 2),
                         ])
def test_period_year_range(start_date, end_date,
                           num, delta,
                           result_date1, result_date2,
                           start_date_adjustment_by_frequency,
                           end_date_adjustment_by_frequency,
                           lenght):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='year', num=num, delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)
    assert result[0]['date1_str'] == result_date1
    assert result[0]['date2_str'] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize('start_date,end_date,'
                         'delta,'
                         'start_date_adjustment_by_frequency,'
                         'end_date_adjustment_by_frequency',
                         [
                             (datetime(2016, 1, 1).date(), datetime(2019, 1, 16, 1, 1, 1, 1), 366, True, False),
                         ])
def test_period_year_range_custom(start_date, end_date,
                                  delta,
                                  start_date_adjustment_by_frequency,
                                  end_date_adjustment_by_frequency):
    result = period_range(start_date=start_date,
                          end_date=end_date,
                          frequency='year', delta=delta,
                          start_date_adjustment_by_frequency=start_date_adjustment_by_frequency,
                          end_date_adjustment_by_frequency=end_date_adjustment_by_frequency,
                          return_type='dict', string_format='%Y-%m-%d')
    print(result)


@pytest.mark.parametrize('start_date,frequency,result1,result2',
                         ((datetime(2019, 1, 3), 'week', datetime(2018, 12, 31, 0, 0),
                           datetime(2019, 1, 6, 23, 59, 59, 999)),
                          (datetime(2019, 1, 3), 'month', datetime(2019, 1, 1, 0, 0),
                           datetime(2019, 1, 31, 23, 59, 59, 999)),
                          (datetime(2019, 1, 3), 'quarter', datetime(2019, 1, 1, 0, 0),
                           datetime(2019, 3, 31, 23, 59, 59, 999)),
                          (datetime(2019, 1, 3), 'year', datetime(2019, 1, 1, 0, 0),
                           datetime(2019, 12, 31, 23, 59, 59, 999)),
                          ))
def test_frequency_end_date(start_date, frequency, result1, result2):
    results = frequency_dates(start_date, frequency)
    assert results['start'] == result1
    assert results['end'] == result2
