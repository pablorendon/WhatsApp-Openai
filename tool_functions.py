def get_current_weather(function_args: dict) -> str:
    # Extracting information from the input dictionary
    location = function_args.get('location', 'Unknown location')
    unit = function_args.get('unit', 'celsius')
    
    # Generating a dummy temperature for demonstration
    dummy_temperature = 25  # This can be adjusted or randomized as needed
    
    # Correcting the typo in 'city' and 'Ahmedabad', and making the response dynamic
    response_message = f"The weather in {location} is currently {dummy_temperature} degrees {unit}."
    
    return response_message


def get_current_weather_for_ndays(function_args: dict) -> str:
    # Extracting information from the input dictionary
    location = function_args.get('location', 'Unknown location')
    n_days = function_args.get('n_days', 0)
    unit = function_args.get('unit', 'celsius')
    
    # Generating a dummy temperature for demonstration
    dummy_temperature = 69  # This can be randomized or adjusted as needed
    
    # Constructing a dynamic response message
    response_message = (f"The weather in {location} for the upcoming {n_days} days will be approximately "
                        f"{dummy_temperature} degrees {unit}.")
    
    return response_message


available_functions = {
    "get_current_weather": get_current_weather,
    "get_current_weather_for_ndays": get_current_weather_for_ndays
}
