import streamlit as st
import folium
from streamlit_folium import st_folium

# Page configuration
st.set_page_config(
    page_title="Pakistan Cities Map",
    page_icon="🗺️",
    layout="wide"
)

# Title and description
st.title("🗺️ Pakistan Major Cities Map")
st.markdown("Interactive map showing major cities of Pakistan with their locations.")

# Create a Map centered on Pakistan
m = folium.Map(location=[30.3753, 69.3451], zoom_start=6)

# List of selected cities with their exact latitude and longitude + unique colors
cities = [
    {"city": "Lahore", "lat": 31.582045, "lon": 74.329376, "color": "red", 
     "info": "Cultural capital of Pakistan, known for its rich history and food."},
    {"city": "Peshawar", "lat": 34.0151, "lon": 71.5249, "color": "blue",
     "info": "Gateway to the Khyber Pass, historic trade route."},
    {"city": "Islamabad", "lat": 33.6844, "lon": 73.0479, "color": "green",
     "info": "Capital city, known for its modern planning and cleanliness."},
    {"city": "Karachi", "lat": 24.8607, "lon": 67.0011, "color": "purple",
     "info": "Largest city and economic hub of Pakistan."},
    {"city": "Faisalabad", "lat": 31.4187, "lon": 73.0790, "color": "orange",
     "info": "Industrial center, known for textile manufacturing."},
]

# Add markers for each city with different colors and popups
for city in cities:
    folium.Marker(
        [city["lat"], city["lon"]],
        popup=folium.Popup(
            f"<b>{city['city']}</b><br>{city['info']}", 
            max_width=300
        ),
        tooltip=city["city"],
        icon=folium.Icon(color=city["color"])
    ).add_to(m)

# Create two columns
col1, col2 = st.columns([2, 1])

# Display the map in the first (larger) column
with col1:
    # Display the map using st_folium
    st_folium(m, width=800, height=600)

# Display city information in the second column
with col2:
    st.markdown("### 🏙️ Major Cities")
    for city in cities:
        with st.expander(f"📍 {city['city']}"):
            st.markdown(f"""
            - **Location:** {city['lat']}, {city['lon']}
            - **Info:** {city['info']}
            """)

# Add some context about the map
st.markdown("---")
st.markdown("""
### 📝 About This Map
This interactive map shows the locations of major cities in Pakistan. Each city is marked with a unique color:
- 🔴 Lahore - Cultural Hub
- 🔵 Peshawar - Historical Gateway
- 🟢 Islamabad - Capital City
- 🟣 Karachi - Economic Center
- 🟡 Faisalabad - Industrial City

Click on any marker to see more information about the city.
""")

# Footer
st.markdown("---")
st.markdown("🗺️ Created with Streamlit and Folium | Data source: Geographic coordinates of major Pakistani cities")
