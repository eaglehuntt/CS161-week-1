#!/usr/bin/env python3
"""Script that finds the depth of the water from the great lakes if it was 
spread across the contiguous states
"""

# got great lakes volume from
# https://en.wikipedia.org/wiki/Contiguous_United_States

GREAT_LAKES_VOLUME = 22_810.0
CONTIGUOUS_STATES_AREA = 7_663_941.7
METERS_IN_ONE_KM = 1000
DECIMAL_PLACE = 2


def get_rounded_depth(volume, area):
    """
    Find the rounded depth of the volume in the specified area
Args:
volume (float): The volume in km^3 used for calculation
area (float): The area in km^2 used for calculation
Returns:
depth (float): The depth rounded to 2 decimal places
"""
    depth = (volume / area) * METERS_IN_ONE_KM
    return round(depth, DECIMAL_PLACE)


depth = get_rounded_depth(GREAT_LAKES_VOLUME, CONTIGUOUS_STATES_AREA)

print(f"If the water in the great lakes were spread evenly across the \
contiguous states, the water would be ~{depth} meters deep.")
