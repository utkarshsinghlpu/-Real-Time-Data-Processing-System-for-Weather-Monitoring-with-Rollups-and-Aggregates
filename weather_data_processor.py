import requests
import time
import pandas as pd
import sqlite3
import plotly.graph_objects as go
from datetime import datetime
from collections import defaultdict

API_KEY = 'fcc8de7015bbb202209bbf0261babf4c'  # OpenWeatherMap API key
CITIES = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}
INTERVAL = 300  # 5 minutes interval for data fetch

weather_data = defaultdict(list)

# SQLite database setup
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create a table for weather data if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY,
    city TEXT,
    timestamp TEXT,
    temperature REAL,
    feels_like REAL,
    humidity REAL,
    wind_speed REAL,
    pressure REAL,
    weather_condition TEXT
)''')
conn.commit()


def kelvin_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin_temp - 273.15


def fetch_weather(city_id):
    """Fetch current weather data from OpenWeatherMap for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def process_weather_data(data, city):
    """Process and store real-time weather data."""
    main_data = data['main']
    weather_condition = data['weather'][0]['main']
    temp_celsius = kelvin_to_celsius(main_data['temp'])
    feels_like_celsius = kelvin_to_celsius(main_data['feels_like'])
    humidity = main_data['humidity']
    wind_speed = data['wind']['speed']
    pressure = main_data['pressure']

    timestamp = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

    # Append data to storage
    weather_data[city].append({
        "timestamp": timestamp,
        "temperature": temp_celsius,
        "feels_like": feels_like_celsius,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "pressure": pressure,
        "weather_condition": weather_condition,
    })

    cursor.execute('''INSERT INTO weather (city, timestamp, temperature, feels_like, humidity, wind_speed, pressure, weather_condition)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (city, timestamp, temp_celsius, feels_like_celsius, humidity, wind_speed, pressure,
                    weather_condition))
    conn.commit()


def aggregate_daily(city):
    """Calculate daily weather summary aggregates."""
    df = pd.DataFrame(weather_data[city])
    if len(df) > 0:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')

        daily_summary = {
            'avg_temp': df['temperature'].mean(),
            'max_temp': df['temperature'].max(),
            'min_temp': df['temperature'].min(),
            'dominant_condition': df['weather_condition'].mode()[0]
        }
        return daily_summary
    return None


def check_threshold(city, temp, threshold=35):
    """Check if temperature exceeds the threshold and trigger an alert."""
    if temp > threshold:
        print(f"Alert: Temperature in {city} exceeded {threshold}°C!")


def plot_weather(city):
    """Enhanced real-time colorful visualization with additional parameters."""
    df = pd.DataFrame(weather_data[city])
    if len(df) > 0:
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'], mode='lines+markers', name='Temperature (°C)',
                                 line=dict(color='firebrick', width=2)))

        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['feels_like'], mode='lines+markers', name='Feels Like (°C)',
                                 line=dict(color='royalblue', width=2, dash='dash')))

        fig.add_trace(go.Bar(x=df['timestamp'], y=df['humidity'], name='Humidity (%)', marker_color='lightblue'))

        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['wind_speed'], mode='lines', name='Wind Speed (m/s)',
                                 line=dict(color='green', width=2)))

        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['pressure'], mode='lines', name='Pressure (hPa)',
                                 line=dict(color='purple', width=2)))

        fig.update_layout(
            title=f"Real-Time Weather Data for {city}",
            xaxis_title="Time",
            yaxis_title="Value",
            template="plotly_dark",
            plot_bgcolor='rgba(0,0,0,0)',
            legend_title="Weather Metrics",
            font=dict(size=14)
        )

        # Show the plot
        fig.show()


def display_aggregates(city):
    """Display daily aggregate weather summary."""
    summary = aggregate_daily(city)
    if summary:
        print(f"Daily Weather Summary for {city}:")
        print(f"Avg Temp: {summary['avg_temp']:.2f}°C")
        print(f"Max Temp: {summary['max_temp']:.2f}°C")
        print(f"Min Temp: {summary['min_temp']:.2f}°C")
        print(f"Dominant Condition: {summary['dominant_condition']}")


def run_weather_monitoring():
    while True:
        for city, city_id in CITIES.items():
            try:
                # Fetch real-time weather data
                data = fetch_weather(city_id)
                process_weather_data(data, city)

                temp = kelvin_to_celsius(data['main']['temp'])
                check_threshold(city, temp, threshold=35)

                plot_weather(city)

                display_aggregates(city)

            except Exception as e:
                print(f"Error fetching data for {city}: {e}")

        # Sleep for the defined interval (e.g., 5 minutes)
        time.sleep(INTERVAL)


# Start the system
run_weather_monitoring()