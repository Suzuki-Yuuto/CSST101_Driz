class SimpleWeatherAI:
    def __init__(self):
        self.weather_conditions = {
            "sunny": "Go for a walk.",
            "rainy": "Stay indoors and read a book.",
            "snowy": "Build a snowman.",
            "cloudy": "Go for a run.",
        }

    def recommend_activity(self, weather):
        # Get the recommended activity based on the weather
        return self.weather_conditions.get(weather.lower(), "No activity recommended.")

# Example
if __name__ == "__main__":
    ai_agent = SimpleWeatherAI()
    
    # Simulate different weather conditions
    weather_conditions = ["sunny", "rainy", "snowy", "cloudy", "windy"]
    
    for weather in weather_conditions:
        activity = ai_agent.recommend_activity(weather)
        print(f"Weather: {weather.capitalize()} - Activity: {activity}")