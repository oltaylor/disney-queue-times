import requests

# Park IDs, "translating" from words to IDs.
PARK_IDS = {
    "Magic Kingdom": "75ea578a-adc8-4116-a54d-dccb60765ef9",
    "EPCOT": "47f90d2c-e191-4239-a466-5892ef59a88b",
    "Disney's Hollywood Studios": "288747d1-8b4f-4a64-867e-ea7c9b27bad8",
    "Disney's Animal Kingdom": "1c84a229-8862-4648-9c71-378ddd2c7693",
    "Disneyland Park Paris": "dae968d5-630d-4719-8b06-3d107e944401",
    "Disney Adventure World": "ca888437-ebb4-4d50-aed2-d227f7096968",
    "Tokyo Disneyland": "3cc919f1-d16d-43e0-8c3f-1dd269bd1a42",
    "Tokyo DisneySea": "67b290d5-3478-4f23-b601-2f8fb71ba803",
    "Shanghai Disneyland": "ddc4357c-c148-4b36-9888-07894fe75e83",
    "Disneyland Park": "7340550b-c14d-4def-80bb-acdb51d49a66",
    "Disney California Adventure": "832fcd51-ea19-4e77-85c7-75d5843b127c",
    "Hong Kong Disneyland": "bd0eb47b-2f02-4d4d-90fa-cb3a68988e3b"
}

BASE_URL = "https://api.themeparks.wiki/v1"


def getParkAttractionsInfo(park: str):
    if park in PARK_IDS:
        request = requests.get(f"{BASE_URL}/entity/{PARK_IDS[park]}/live")

        if request.status_code == 200:
            infoDict = [attr for attr in request.json()["liveData"] if attr["entityType"] == "ATTRACTION"]

            return infoDict

    return False


def getParkAttractions(park: str): # Return all ride names from a specific park
    info = getParkAttractionsInfo(park)
    if info:
        attrs = [attr["name"] for attr in info]

        return attrs

    return False


def getParkWaits(park: str): # Similar to getParkAttractionsInfo, but formats to include only the attraction names and wait times.
    info = getParkAttractionsInfo(park)

    if info:
        attrDict = {}

        for attr in info:
            qLength = attr.get("queue", {}).get("STANDBY", {}).get("waitTime")

            if qLength:
                attrDict[attr["name"]] = qLength

        return attrDict

    return False


def getRideWait(ride: str, park: str): # getParkWaits but searches for a single attraction
    attractions = getParkAttractions(park)

    if attractions and (ride.lower() in [attr.lower() for attr in attractions]):
        parkWaits = getParkWaits(park)

        if parkWaits:
            if ride in parkWaits:
                return parkWaits[ride]

    return False


def getParkAttractionStatuses(park: str): # Similar to getParkAttractionsInfo, but formats to include only the attraction names and whether it is 'Open', 'Closed' or 'Down'.
    info = getParkAttractionsInfo(park)
    if info:
        ridesDict = {}

        for attr in info:
            if attr["status"] == "OPERATING":
                ridesDict[attr["name"]] = "Open"
            elif attr["status"] == "CLOSED":
                ridesDict[attr["name"]] = "Closed"
            elif attr["status"] == "DOWN":
                ridesDict[attr["name"]] = "Down"
            elif attr["status"] == "REFURBISHMENT":
                ridesDict[attr["name"]] = "Under refurbishment"
            else:
                ridesDict[attr["name"]] = "Unknown"

        return ridesDict

    return False

def getRideStatus(ride: str, park: str): # getParkAttractionStatuses but searches for a single attraction
    attractions = getParkAttractions(park)

    if attractions and (ride.lower() in [attr.lower() for attr in attractions]):
        parkStatuses = getParkAttractionStatuses(park)

        if parkStatuses:
            if ride in parkStatuses:
                return parkStatuses[ride]

    return False



if __name__ == "__main__":
    print("This script is not designed to be run standalone.")