# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates




















## Key Features
1. **Real-Time Data**: Fetch weather data for six Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) every 5 minutes.
2. **Weather Parameters**: Includes temperature, feels-like, humidity, wind speed, and pressure.
3. **Daily Aggregates**: Calculates daily averages, maximum, minimum temperatures, and dominant weather condition.
4. **Alerts**: Supports user-defined temperature thresholds with real-time alerts.
5. **SQLite Database**: Stores historical weather data for further analysis.
6. **Visualizations**: Provides colorful real-time graphs for temperature, humidity, wind speed, etc.

## Build Instructions

1. **Install Dependencies**:
   ```bash
   pip install requests plotly pandas
   
2. **Add your OpenWeatherMap API Key in main.py**:
      ```bash
   API_KEY = 'your_api_key'
      
3. **Run the Application**:
      ```bash
   python main.py


## Design Choices
1. **SQLite: Used for lightweight, embedded database storage**:
2. **Plotly: Chosen for interactive, easy-to-use visualizations**:
3. **Threshold Alerts: Customizable by users to trigger alerts based on weather conditions**:


## Test Cases
1. **API Connection: Validate the connection to the OpenWeatherMap API and ensure data retrieval for all six cities**:
2. **Temperature Conversion: Ensure correct conversion from Kelvin to Celsius and Fahrenheit based on user preference**:
3. **Daily Summaries: Simulate multiple weather updates and verify that daily summaries (average, max, min temperatures, dominant weather) are calculated correctly**:
4. **Alerting System: Set thresholds and validate that alerts are triggered correctly when conditions are breached**:
