#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyswarms` package."""

# Import modules
import unittest
import numpy as np

# Import from package
from pyswarms.utils.functions import single_obj as fx


class TestSingleObj(unittest.TestCase):
    """Base class for testing single-objective functions."""

    def setUp(self):
        """Set up test fixtures."""
        # Test swarm with size=3, dimensions=2
        self.input = np.zeros([3,2])
        self.input2 = np.ones([3,2])
        # Erroneous input - dimension
        self.bad_input = np.zeros([3,3])
        # Target value
        self.target = np.zeros(3)
        # Target output size
        self.target_size = (self.input.shape[0], )

class InputBoundFail(TestSingleObj):
    """Tests exception throws when fed with erroneous input."""

    def test_rastrigin_bound_fail(self):
        """Test rastrigin bound exception"""
        x = - np.random.randint(low=6,high=100,size=(3,2))
        x_ = np.random.randint(low=6,high=100,size=(3,2))
        with self.assertRaises(AssertionError):
            fx.rastrigin_func(x)
            fx.rastrigin_func(x_)

    def test_ackley_bound_fail(self):
        """Test ackley bound exception"""
        x = - np.random.randint(low=32,high=100,size=(3,2))
        x_ = np.random.randint(low=32,high=100,size=(3,2))
        with self.assertRaises(AssertionError):
            fx.ackley_func(x)
            fx.ackley_func(x_)

    def test_beale_bound_fail(self):
        """Test beale bound exception"""
        x = - np.random.randint(low=4.6666,high=100,size=(3,2))
        x_ = np.random.randint(low=4.6666,high=100,size=(3,2))
        with self.assertRaises(AssertionError):
            fx.beale_func(x)
            fx.beale_func(x_)

    def test_goldstein_bound_fail(self):
        """Test goldstein bound exception"""
        x = - np.random.randint(low=2.00001,high=100,size=(3,2))
        x_ = np.random.randint(low=2.00001,high=100,size=(3,2))
        with self.assertRaises(AssertionError):
            fx.goldstein_func(x)
            fx.goldstein_func(x_)

    def test_booth_bound_fail(self):
        """Test booth bound exception"""
        x = - np.random.randint(low=11.00001,high=100,size=(3,2))
        x_ = np.random.randint(low=11.00001,high=100,size=(3,2))
        with self.assertRaises(AssertionError):
            fx.booth_func(x)
            fx.booth_func(x_)

class InputDimFail(TestSingleObj):
    """Tests exception throws when fed with erroneous dimension."""

    def test_beale_dim_fail(self):
        """Test beale dim exception"""
        with self.assertRaises(AssertionError):
            fx.beale_func(self.bad_input)

    def test_goldstein_dim_fail(self):
        """Test golstein dim exception"""
        with self.assertRaises(AssertionError):
            fx.goldstein_func(self.bad_input)

    def test_booth_dim_fail(self):
        """Test booth dim exception"""
        with self.assertRaises(AssertionError):
            fx.booth_func(self.bad_input)

class ExpectedOutput(TestSingleObj):
    """Tests if a function outputs a minima if fed with expected argmin."""

    def test_sphere_output(self):
        """Tests sphere function output."""
        self.assertEqual(fx.sphere_func(self.input).all(), self.target.all())

    def test_rastrigin_output(self):
        """Tests rastrigin function output."""
        self.assertEqual(fx.rastrigin_func(self.input).all(), self.target.all())

    def test_ackley_output(self):
        """Tests ackley function output."""
        assert np.isclose(fx.ackley_func(self.input), self.target).all()

    def test_rosenbrock_output(self):
        """Tests rosenbrock function output."""
        self.assertEqual(fx.rosenbrock_func(self.input2).all(),np.zeros(3).all())

    def test_beale_output(self):
        """Tests beale function output."""
        assert np.isclose(fx.beale_func([3, 0.5] * self.input2),
            self.target).all()

    def test_goldstein_output(self):
        """Tests goldstein-price function output."""
        assert np.isclose(fx.goldstein_func([0, -1] * self.input2),
            (3 * np.ones(3))).all()

    def test_booth_output(self):
        """Test booth function output."""
        assert np.isclose(fx.booth_func([1, 3] * self.input2),
            self.target).all()

class OutputSize(TestSingleObj):
    """Tests if the output of the function is the same as no. of particles"""

    def test_sphere_output_size(self):
        """Tests sphere output size."""
        self.assertEqual(fx.sphere_func(self.input).shape, self.target_size)

    def test_rastrigin_output_size(self):
        """Tests rastrigin output size."""
        self.assertEqual(fx.rastrigin_func(self.input).shape, self.target_size)

    def test_ackley_output_size(self):
        """Tests ackley output size."""
        self.assertEqual(fx.ackley_func(self.input).shape, self.target_size)

    def test_rosenbrock_output_size(self):
        """Tests rosenbrock output size."""
        self.assertEqual(fx.rosenbrock_func(self.input).shape, self.target_size)

    def test_beale_output_size(self):
        """Tests beale output size."""
        self.assertEqual(fx.beale_func(self.input).shape, self.target_size)

    def test_goldstein_output_size(self):
        """Test goldstein output size."""
        self.assertEqual(fx.goldstein_func(self.input).shape, self.target_size)

    def test_booth_output_size(self):
        """Test booth output size."""
        self.assertEqual(fx.booth_func(self.input).shape, self.target_size)

if __name__ == '__main__':
    unittest.main()