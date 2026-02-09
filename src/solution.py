## Student Name:Rajendra Brahmbhatt 
## Student ID: 217925157
from typing import Dict, List, Union

Number = Union[int, float]

def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    New requirement:
    At least ONE resource must remain unallocated after assignment.
    If all resources are fully consumed, allocation is NOT feasible.
    """

    # capacities must be non-negative
    for capacity in resources.values():
        if capacity < 0:
            return False

    usage: Dict[str, Number] = {}

    for request in requests:
        if not isinstance(request, dict):
            raise ValueError("Each request must be a dictionary")

        for resource, amount in request.items():
            if amount < 0:
                return False

            if resource not in resources:
                return False

            usage[resource] = usage.get(resource, 0) + amount

            # capacity exceeded
            if usage[resource] > resources[resource]:
                return False

    # ---------------- NEW REQUIREMENT ----------------
    # At least one resource must remain unallocated
    # i.e. exists resource where usage < capacity

    if not resources:
        # no resources -> nothing consumed -> valid
        return True

    for resource, capacity in resources.items():
        used = usage.get(resource, 0)
        if used < capacity:
            return True  # at least one has leftover

    # if we reach here → all resources fully consumed
    return False
