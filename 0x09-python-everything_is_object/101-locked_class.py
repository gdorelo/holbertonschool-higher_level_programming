#!/usr/bin/python3
class LockedClass:
    """Locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
