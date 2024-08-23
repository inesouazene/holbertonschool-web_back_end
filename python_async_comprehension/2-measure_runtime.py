#!/usr/bin/env python3
"""Measure runtime module."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel
    and measure runtime."""
    start_time = time.time()

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    return end_time - start_time
