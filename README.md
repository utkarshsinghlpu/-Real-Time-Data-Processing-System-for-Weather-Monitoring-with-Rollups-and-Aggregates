# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates
## Screenshots
![Screenshot 2024-10-24 223702](https://github.com/user-attachments/assets/6b32f35d-5825-45ec-aa8a-dd662942a06c)
![Screenshot 2024-10-24 223644](https://github.com/user-attachments/assets/b43e5b71-1391-430a-986d-c22785979ce5)
![Screenshot 2024-10-24 223620](https://github.com/user-attachments/assets/8635a5a8-37b2-4244-ad47-93a43f9a62df)
![Screenshot 2024-10-24 223555](https://github.com/user-attachments/assets/ce9bccf8-c935-42c7-9020-42064b8b22b2)
![Screenshot 2024-10-24 223533](https://github.com/user-attachments/assets/4406b730-acc6-4451-b3e7-3a84a9a3b826)
![Screenshot 2024-10-24 223511](https://github.com/user-attachments/assets/4e55c151-7d0c-4a5a-9048-f0996a4b2bd2)


































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
