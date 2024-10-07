"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
"test, expected, expect_raises",
[
    # previous test cases here, with None for expect_raises, except for the next one - add ValueError
    # as an expected exception (since it has a negative input value)
    (
        [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
        ValueError,
    ),
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
        None,
    ),
])

def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            result = patient_normalise(np.array(test))
            npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)
    else:
        result = patient_normalise(np.array(test))
        npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)