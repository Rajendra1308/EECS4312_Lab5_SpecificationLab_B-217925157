## Student Name:
## Student ID: 

"""
Public test suite for the meeting slot suggestion exercise.

Students can run these tests locally to check basic correctness of their implementation.
The hidden test suite used for grading contains additional edge cases and will not be
available to students.
"""
from solution import is_allocation_feasible
import pytest


def test_basic_feasible_single_resource():
    # Basic Feasible Single-Resource
    # Constraint: total demand <= capacity
    # Reason: check basic functional requirement
    resources = {'cpu': 10}
    requests = [{'cpu': 3}, {'cpu': 4}, {'cpu': 3}]
    assert is_allocation_feasible(resources, requests) is True

def test_multi_resource_infeasible_one_overloaded():
    # Multi-Resource Infeasible (one overload)
    # Constraint: one resource exceeds capacity
    # Reason: check detection of per-resource infeasibility
    resources = {'cpu': 8, 'mem': 30}
    requests = [{'cpu': 2, 'mem': 8}, {'cpu': 3, 'mem': 10}, {'cpu': 3, 'mem': 14}]
    assert is_allocation_feasible(resources, requests) is False

def test_missing_resource_in_availability():
    # Missing Resource in Requests
    # Constraint: request references unavailable resource
    # Reason: allocation must be infeasible
    resources = {'cpu': 10}
    requests = [{'cpu': 2}, {'gpu': 1}]
    assert is_allocation_feasible(resources, requests) is False

def test_non_dict_request_raises():
    # Non-Dict Request Raises Error
    # Constraint: structural validation
    # Reason: request must be a dict
    resources = {'cpu': 5}
    requests = [{'cpu': 2}, ['mem', 1]]  # malformed request
    with pytest.raises(ValueError):
        is_allocation_feasible(resources, requests)

def test_allocation_exact_capacity_match():
    resources = {"CPU": 8, "RAM": 16}
    requests = [
        {"CPU": 3, "RAM": 6},
        {"CPU": 5, "RAM": 10}
    ]

    assert is_allocation_feasible(resources, requests) is True
def test_multiple_requests_multiple_resources():
    resources = {"CPU": 10, "RAM": 32, "DISK": 100}
    requests = [
        {"CPU": 2, "RAM": 8},
        {"CPU": 4, "DISK": 40},
        {"RAM": 16, "DISK": 50}
    ]

    assert is_allocation_feasible(resources, requests) is True
def test_request_for_unavailable_resource():
    resources = {"CPU": 4, "RAM": 8}
    requests = [
        {"CPU": 2},
        {"GPU": 1}
    ]

    assert is_allocation_feasible(resources, requests) is False


def test_negative_request_amount():
    resources = {"CPU": 4}
    requests = [
        {"CPU": -1}
    ]

    assert is_allocation_feasible(resources, requests) is False

def test_empty_requests_list():
    resources = {"CPU": 4, "RAM": 8}
    requests = []

    assert is_allocation_feasible(resources, requests) is True
