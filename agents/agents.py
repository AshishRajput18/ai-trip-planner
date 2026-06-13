from crewai import Agent

from config.llm_config import llm
from tools.search_tool import search_web_tool


# Agent 1 - Local Guide Expert
guide_expert = Agent(
    role="City Local Guide Expert",

    goal="""
    Provides information on things to do in the city
    based on the user's interests.
    """,

    backstory="""
    A local expert with a passion for sharing
    the best experiences and hidden gems of their city.
    """,

    tools=[search_web_tool],

    verbose=True,
    max_iter=5,

    llm=llm,

    allow_delegation=False,
)


# Agent 2 - Travel Expert
location_expert = Agent(

    role="Travel Trip Expert",

    goal="""
    Adapt to the destination city's language and gather
    useful information about the city and travel.
    """,

    backstory="""
    A seasoned traveler who has explored various destinations
    and knows the ins and outs of travel logistics.
    """,

    tools=[search_web_tool],

    verbose=True,
    max_iter=5,

    llm=llm,

    allow_delegation=False,
)


# Agent 3 - Planner Expert
planner_expert = Agent(

    role="Travel Planning Expert",

    goal="""
    Compiles all gathered information to provide
    a comprehensive travel plan.
    """,

    backstory="""
    You are a professional guide with a passion for travel.
    An organizational wizard who can turn a list of
    possibilities into a seamless itinerary.
    """,

    tools=[search_web_tool],

    verbose=True,
    max_iter=5,

    llm=llm,

    allow_delegation=False,
)