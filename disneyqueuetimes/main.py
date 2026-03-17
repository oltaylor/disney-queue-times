import requests

# Park IDs, as available on Queue-Times.com website.
PARK_IDS = {
    "Magic Kingdom": 6,
    "EPCOT": 5,
    "Disney's Hollywood Studios": 7,
    "Disney's Animal Kingdom": 8,
    "Disneyland Park Paris": 4,
    "Disney Adventure World": 28,
    "Disneyland Park": 16,
    "Disney California Adventure": 17,
    "Hong Kong Disneyland": 31,
    "Shanghai Disneyland": 30,
    "Tokyo Disneyland": 274,
    "Tokyo DisneySea": 275
}

def getParkAttractionInfo(park: str): # Returns info directly from request with no formatting.
    if park in PARK_IDS:
        request = requests.get(f"https://queue-times.com/parks/{PARK_IDS[park]}/queue_times.json")

        if request.status_code == 200:
            return request.json()

    return False


def getParkAttractions(park: str): # Return all ride names from a specific park
    if park.lower() in [pid.lower() for pid in PARK_IDS]:
        request = requests.get(f"https://queue-times.com/parks/{PARK_IDS[park]}/queue_times.json")

        if request.status_code == 200:
            rides = []

            for land in request.json()["lands"]:
                for attraction in land["rides"]:
                    rides.append(attraction["name"])

            return rides

    return False

def getParkWaits(park: str): # Similar to getParkAttractionsInfo, but formats to include only the attraction names and wait times.
    attractionInfo = getParkAttractionInfo(park)
    if attractionInfo:
        ridesDict = {}

        for land in attractionInfo["lands"]:
            for attraction in land["rides"]:
                ridesDict[attraction["name"]] = attraction["wait_time"]

        return ridesDict

    return False

def getRideWait(ride: str, park: str): # getParkWaits but searches for a single attraction
    attractions = getParkAttractions(park)

    if attractions and (ride.lower() in [attr.lower() for attr in attractions]):
        parkWaits = getParkWaits(park)

        if parkWaits:
            if ride in parkWaits:
                return parkWaits[ride]

    return False

def getParkStatuses(park: str): # Similar to getParkAttractionsInfo, but formats to include only the attraction names and whether it is 'Open' or 'Closed'.
    attractionInfo = getParkAttractionInfo(park)
    if attractionInfo:
        ridesDict = {}

        for land in attractionInfo["lands"]:
            for attraction in land["rides"]:
                ridesDict[attraction["name"]] = ("Open" if attraction["is_open"] == True else "Closed")

        return ridesDict

    return False

def getRideStatus(ride: str, park: str): # getParkStatuses but searches for a single attraction
    attractions = getParkAttractions(park)

    if attractions and (ride.lower() in [attr.lower() for attr in attractions]):
        parkStatuses = getParkStatuses(park)

        if parkStatuses:
            if ride in parkStatuses:
                return parkStatuses[ride]

    return False



if __name__ == "__main__":
    print("This script is not designed to be run standalone.")