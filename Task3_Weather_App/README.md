# Task 3: Weather App

## Internship
Oasis Infobyte – Python Programming Internship

## Project Description
This project is a command-line based Weather Application developed using Python.
It fetches real-time weather data from the OpenWeatherMap API based on the city entered by the user.
The program displays temperature (in Celsius), humidity, and weather condition in a clean format.

## Features
- Accepts city name as input
- Fetches real-time weather data using OpenWeatherMap API
- Converts temperature from Kelvin to Celsius
- Displays:
  - City name
  - Temperature
  - Humidity
  - Weather condition
- Handles invalid city names
- Handles network/API errors using exception handling

## Concepts Used
- Functions and modular programming
- API integration using `requests` module
- JSON data handling
- Dictionary and list indexing
- Conditional statements
- Exception handling (try-except)
- Unit conversion logic

## Temperature Conversion Formula
- Celsius = Kelvin - 273.15

## How It Works
1. User enters the city name.
2. Program sends a request to the OpenWeatherMap API.
3. API returns weather data in JSON format.
4. Program extracts required information from the JSON response.
5. Temperature is converted from Kelvin to Celsius.
6. Weather details are displayed to the user.

## File Structure
- `weather_app.py` - Main Python program
- `README.md` - Project documentation
