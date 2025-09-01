import asyncio
import time
import streamlit as st
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel
from strands_tools import current_time
from geopy.geocoders import Nominatim

load_dotenv()

model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    params={
        "temperature": 0.0,
    }
)

@tool
def geolocation(city: str) -> dict:
    """Get geolocation for a city
    """
    geolocator = Nominatim(user_agent="strands-ai-demo")
    try:
        location = geolocator.geocode(city)
        if location:
            latitude = location.latitude
            longitude = location.longitude
        else:
            return {"error": f"Could not find location for city: {city}"}
    except Exception as e:
        return {"error": f"An error occurred during geocoding: {e}"}

    return {
        "latitude": location.latitude,
        "longitude": location.longitude
    }


async def main():

    agent = Agent(
        model=model,
        tools=[current_time, geolocation],
    )

    st.title("Strands App")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.markdown(content)

    if prompt := st.chat_input("Digite sua mensagem"):
        messages = []
        with st.chat_message("user"):
            st.markdown(prompt)
            messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            result = ""
            stream = agent.stream_async(prompt)
            placeholder = st.empty()
            async for chunk in stream:
                if "data" in chunk:
                    result += chunk["data"]
                    placeholder.markdown(result)
                    time.sleep(0.05)
            messages.append({"role": "assistant", "content": result})

        st.session_state["messages"] += messages

asyncio.run(main())