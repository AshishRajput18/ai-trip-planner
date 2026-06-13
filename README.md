# AI Trip Planner

A sleek Streamlit app that uses CrewAI, Groq, and web search to build a personalized travel plan from a few simple inputs.

## What it does

Enter your departure city, destination, dates, and travel interests, then the app coordinates three AI agents to generate:

- A destination research report
- A personalized city guide
- A complete travel plan with itinerary and recommendations

The results are also saved as markdown files for easy reuse and export.

## Highlights

- Multi-agent travel planning powered by CrewAI
- Real-time web search with DuckDuckGo
- Streamlit interface for quick trip generation
- Markdown reports that are easy to read, edit, and share
- Supports destinations with language-aware responses for French-speaking countries

## Tech Stack

- Python
- Streamlit
- CrewAI
- Groq LLM
- DuckDuckGo search tool

## Project Output

Running the app generates these reports in the project root:

- `city_report.md`
- `guide_report.md`
- `travel_plan.md`

## Setup

1. Create and activate a Python environment.
2. Install the required packages.
3. Add your Groq API key to a `.env` file.

Example `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Install Dependencies

If you already have a `requirements.txt`, install from it. Otherwise, make sure these packages are available:

```bash
pip install streamlit crewai crewai-tools langchain-community python-dotenv
```

## Run the App

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## How It Works

1. You enter the trip details in the Streamlit form.
2. The app creates a CrewAI crew with three agents.
3. The agents gather destination data, build a city guide, and assemble the final travel plan.
4. The finished plan is displayed in the browser and downloaded as a text file.

## Project Structure

```text
AI-Trip-Planner/
├── app.py
├── agents/
│   ├── __init__.py
│   └── agents.py
├── config/
│   └── llm_config.py
├── crew/
│   └── trip_crew.py
├── tasks/
│   └── travel_tasks.py
├── tools/
│   └── search_tool.py
├── city_report.md
├── guide_report.md
└── travel_plan.md
```

## Agents

- Travel Trip Expert: gathers destination and travel logistics information
- City Local Guide Expert: suggests places and activities based on interests
- Travel Planning Expert: combines everything into a polished itinerary

## Notes

- The app expects a valid `GROQ_API_KEY` in the environment.
- Reports are generated in markdown so they can be reused outside the app.

## License

No license is currently specified.