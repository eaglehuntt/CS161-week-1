#!/usr/bin/env python3
"""Simple script to calculate the estimated population after x years"""
# Define the population variables

CURRENT_US_POPULATION = 334_617_349
BIRTH_RATE = 1/7
DEATH_RATE = 1/13
IMMIGRANT_RATE = 1/35
DAYS_IN_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
SECONDS_IN_A_MINUTE = 60

# Define the function to calculate the estimated population
def estimate_population(years):
    """Get the total population after x years

    Args:
        years (int): User inputted amount of years

    Returns:
        int: Estimated population after x amount of years
    """
    # Calculate seconds in given years
    total_seconds = years * DAYS_IN_YEAR * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_IN_A_MINUTE

    # Calculate the number of births, deaths, and immigrants in the given number of seconds
    births = total_seconds * BIRTH_RATE
    deaths = total_seconds * DEATH_RATE
    immigrants = total_seconds * IMMIGRANT_RATE

    # Add the birth and immigration rates and subtracting the death rate
    estimated_population = CURRENT_US_POPULATION + births + immigrants - deaths

    # Round the population to the nearest integer and return the result rounded
    return round(estimated_population)

# Get the input from the user and print the estimated population
inputted_years = int(input("Enter the number of years: "))
print(f"Estimated population in {inputted_years} years: {estimate_population(inputted_years):,}")
