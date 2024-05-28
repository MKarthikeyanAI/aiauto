import csv

class TouristDestination:
    def __init__(self, name, location, type, rating):
        self.name = name
        self.location = location
        self.type = type
        self.rating = rating

class TouristDestinations:
    def __init__(self):
        self.destinations = []

    def load_destinations(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            #headers = reader.fieldnames
            #print("Headers:", headers)
            for item in reader:
                destination = TouristDestination(
                    name=item['name'],
                    location=item['location'],
                    type=item['type'],
                    rating=float(item['rating'])
                )
                self.destinations.append(destination)

    def get_recommendations(self, location, spot, min_rating):
        recommendations = []
        for destination in self.destinations:
            if (not location or location.lower() in destination.location.lower()) and \
               (not spot or destination.type.lower() == spot.lower()) and \
               (min_rating is None or destination.rating >= min_rating):
                recommendations.append(destination)
        
        recommendations.sort(key=lambda x: x.rating, reverse=True)
        return recommendations

# Example usage:
if __name__ == "__main__":
    tourist_destinations = TouristDestinations()
    tourist_destinations.load_destinations('destinations.csv')

    location = input("Enter your preferred location (or press Enter to skip): ").strip()
    spot = input("Enter your preferred spot type (or press Enter to skip): ").strip()
    min_rating_str = input("Enter the minimum rating you prefer (or press Enter to skip): ").strip()

    if min_rating_str:
        min_rating = float(min_rating_str)
    else:
        min_rating = None

    recommendations = tourist_destinations.get_recommendations(location, spot, min_rating)
    if recommendations:
        print("Recommended tourist destinations:")
        for destination in recommendations:
            print(f"Name: {destination.name}, Location: {destination.location}, Type: {destination.type}, Rating: {destination.rating}")
    else:
        print("No destinations match your preferences.")
