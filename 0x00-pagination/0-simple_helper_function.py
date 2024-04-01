#!/usr/bin/env python3
"""
Pagination index function to help with range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Obtain page and page size information and outputs index range

    Args:
        page: Page number
        page_size: Max page numbers

    Return: Index range
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
