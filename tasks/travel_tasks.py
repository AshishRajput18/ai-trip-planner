from crewai import Task


# Task 1 : Location Task
def location_task(agent, from_city, destination_city, date_from, date_to):

    return Task(

        description=f"""
        This task involves collecting travel information about the destination.

        - Find hotels and accommodations
        - Estimate cost of living
        - Transportation options
        - Visa requirements
        - Travel advisories
        - Weather forecast
        - Important events during the travel period

        Traveling from : {from_city}

        Destination city : {destination_city}

        Arrival Date : {date_from}

        Departure Date : {date_to}

        Rules :

        1. If {destination_city} is in a French-speaking country,
           respond in FRENCH.
        """,

        expected_output=f"""
        A detailed markdown report containing:

        - Hotels and accommodations
        - Daily living expenses
        - Transportation information
        - Weather forecast
        - Travel tips

        If {destination_city} is in a French-speaking country,
        respond in FRENCH.
        """,

        agent=agent,

        output_file="city_report.md"

    )



# Task 2 : Guide Task
def guide_task(agent,
               destination_city,
               interests,
               date_from,
               date_to):

    return Task(

        description=f"""

        Create a personalized city guide.

        Destination city : {destination_city}

        Interests :

        {interests}

        Arrival Date :

        {date_from}

        Departure Date :

        {date_to}

        Include :

        - Tourist attractions
        - Historical places
        - Restaurants
        - Entertainment
        - Outdoor activities
        - Festivals and events

        Rules :

        1. If {destination_city} is in a French-speaking country,
        respond in FRENCH.

        """,

        expected_output="""

        A markdown report containing:

        - Activities
        - Attractions
        - Description
        - Location
        - Ticket or reservation information

        """,

        agent=agent,

        output_file="guide_report.md"

    )



# Task 3 : Planner Task

def planner_task(
        context,
        agent,
        destination_city,
        interests,
        date_from,
        date_to
):

    return Task(

        description=f"""

        Create a complete travel plan.

        Destination city :

        {destination_city}

        Interests :

        {interests}

        Arrival Date :

        {date_from}

        Departure Date :

        {date_to}

        Include:

        - Introduction of city (3-4 paragraphs)
        - Daily itinerary
        - Transportation
        - Expenses
        - Attractions

        Rules :

        1. If {destination_city} is in a French-speaking country,
        respond in FRENCH.

        """,

        expected_output=f"""

        # Welcome to {destination_city}

        Include:

        - City introduction
        - Daily expenses
        - Famous places

        # Travel Plan

        Include:

        - Day by day itinerary
        - Time allocation
        - Activities
        - Travel tips

        Use markdown and emojis.

        """,

        context=context,

        agent=agent,

        output_file="travel_plan.md"

    )