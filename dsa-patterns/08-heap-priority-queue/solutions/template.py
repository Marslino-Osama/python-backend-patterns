"""
Heap / Priority Queue template.

Write this template from memory before solving problems.
"""

import heapq

def top_k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap
