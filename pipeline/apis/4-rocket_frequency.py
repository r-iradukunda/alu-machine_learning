import requests

def get_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the SpaceX API")
        return []

def count_launches_per_rocket(launches):
    rocket_count = {}
    for launch in launches:
        rocket_name = launch['rocket']['name']
        if rocket_name in rocket_count:
            rocket_count[rocket_name] += 1
        else:
            rocket_count[rocket_name] = 1
    return rocket_count

def sort_rockets(rocket_count):
    # First sort by name (A to Z)
    sorted_by_name = sorted(rocket_count.items(), key=lambda x: x[0])
    # Then sort by number of launches (descending)
    sorted_by_launches = sorted(sorted_by_name, key=lambda x: x[1], reverse=True)
    return sorted_by_launches

def main():
    launches = get_launches()
    rocket_count = count_launches_per_rocket(launches)
    sorted_rockets = sort_rockets(rocket_count)
    
    for rocket, count in sorted_rockets:
        print(f"{rocket}: {count}")

if __name__ == "__main__":
    main()