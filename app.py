import streamlit as st

from crew.trip_crew import create_trip_crew


# Streamlit UI
st.title("🌍 AI-Powered Trip Planner")

st.markdown("""
💡 Plan your next trip with AI!

AI will create your full itinerary:
- 🎡 Places to visit  
- 💰 Budget planning  
- 🍕 Food recommendations  
- 🚆 Travel & visa info  
""")

# Inputs
from_city = st.text_input("🏡 From City", "Ahmedabad")
destination_city = st.text_input("✈️ Destination City", "Paris")

date_from = st.date_input("📅 Departure Date")
date_to = st.date_input("📅 Return Date")

interests = st.text_area(
    "🎯 Your Interests (e.g., food, history, adventure)",
    "sightseeing and food"
)


# Button
if st.button("🚀 Generate Travel Plan"):

    if not all([from_city, destination_city, date_from, date_to, interests]):
        st.error("⚠️ Please fill all fields")
    else:

        st.info("⏳ AI is planning your trip... please wait")

        # Create Crew
        crew = create_trip_crew(
            from_city=from_city,
            destination_city=destination_city,
            interests=interests,
            date_from=str(date_from),
            date_to=str(date_to)
        )

        # Run CrewAI
        result = crew.kickoff()

        # Output
        st.subheader("✅ Your Travel Plan")
        st.markdown(str(result))

        # Download button
        st.download_button(
            label="📥 Download Travel Plan",
            data=str(result),
            file_name=f"Travel_Plan_{destination_city}.txt",
            mime="text/plain"
        )