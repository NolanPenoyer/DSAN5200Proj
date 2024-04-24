import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

# Load data
df = pd.read_csv('../final_data/metro_data.csv')

# Get user input
st.sidebar.header('Rank the importance of each factor')
factors = ['personal.income', 'Median.Rent', 'median.sale.price', 'Walkable', 'Unemployment', 'Purchase_power_100_dollars']
weights = {factor: st.sidebar.slider(factor, 0, 10, 5) for factor in factors}

# Calculate scores
df['Score'] = sum(df[factor] * weight for factor, weight in weights.items())

# Get geographical data
geolocator = Nominatim(user_agent="geoapiExercises")
df['Coordinates'] = df['REGION'].apply(geolocator.geocode).apply(lambda loc: (loc.latitude, loc.longitude))

# Display map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(latitude=37.76, longitude=-122.4, zoom=11, pitch=50),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='Coordinates',
            get_color='[200, 30, 0, 160]',
            get_radius='Score',
        )
    ]
))

# Display top-ranked areas
st.header('Top-ranked areas')
st.write(df.nlargest(5, 'Score'))