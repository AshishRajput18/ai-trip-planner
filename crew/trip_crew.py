from crewai import Crew, Process

from agents.agents import (
    location_expert,
    guide_expert,
    planner_expert
)

from tasks.travel_tasks import (
    location_task,
    guide_task,
    planner_task
)


def create_trip_crew(
        from_city,
        destination_city,
        interests,
        date_from,
        date_to
):

    # ---------------- TASKS ----------------

    location = location_task(
        agent=location_expert,
        from_city=from_city,
        destination_city=destination_city,
        date_from=date_from,
        date_to=date_to
    )

    guide = guide_task(
        agent=guide_expert,
        destination_city=destination_city,
        interests=interests,
        date_from=date_from,
        date_to=date_to
    )

    planner = planner_task(
        context=[location, guide],
        agent=planner_expert,
        destination_city=destination_city,
        interests=interests,
        date_from=date_from,
        date_to=date_to
    )

    # ---------------- CREW ----------------

    crew = Crew(
        agents=[
            location_expert,
            guide_expert,
            planner_expert
        ],
        tasks=[
            location,
            guide,
            planner
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew