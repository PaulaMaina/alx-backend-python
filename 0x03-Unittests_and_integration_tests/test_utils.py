#!/usr/bin/env python3
"""Test utils module"""
from parameterized import parameterized
from unittest.mock import Mock, patch
import unittest
from typing import Dict, Mapping, Sequence, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """utils.access_nested_map test case"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
    ) -> None:
        """Tests"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        exception: Exception,
    ) -> None:
        """Test exception raising"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """utils.get_json test case"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        """Tests"""
        attr = {"json.return_value": test_payload}

        with patch("requests.get", return_value=Mock(**attr)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize function"""
    def test_memoize(self) -> None:
        """Tests"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
            ) as mem_func:
                test_class = TestClass()
                self.assertEqual(test_class.a_property(), 42)
                mem_func.assert_called_once()
