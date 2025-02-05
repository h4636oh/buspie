# URL: tickets.paytm.com.com/bus/search/{SOURCE}/{DESTINATION}/{JOURNEY-DATE}/1?URL
# DATE_FORMAT: YYYY-MM-DD
# SOURCE: First letter of city is capital
# DESTINATION: First letter of city is capital

def generate_paytm_bus_url(source, destination, journey_date):
    from datetime import datetime
    
    try:
        datetime.strptime(journey_date, "%Y-%m-%d")
        
        source = source.capitalize()
        destination = destination.capitalize()
        
        url = f"https://tickets.paytm.com/bus/search/{source}/{destination}/{journey_date}/1"
        return url
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."
