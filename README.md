# Disney Wait Times - Python
Powered by [Queue-Times.com](https://queue-times.com).
***
## Attribution
As stated above, the library uses data from [Queue-Times.com](https://queue-times.com). It's important to read their API page before using this project for yourself. These can be found [here](https://queue-times.com/pages/api).

## What?
This project is designed to make it easy to incorporate Disney Wait Times in your projects from all the parks around the world.

## Installation
The project is available on [PyPI](https://pypi.org/project/disneyqueuetimes/).
`pip install disneyqueuetimes`

## How?
### Quick Start
`import disneyqueuetimes as dqt
if __name__ == "__main__":
    print(dqt.getParkWaits("Magic Kingdom"))`
This returns a dictionary of all current wait times in the Magic Kingdom.

See the [wiki](https://github.com/oltaylor/disney-queue-times/wiki/) for all features!

## Features
- View the wait time(s) for any/all attraction(s) in any Disney Park
- View the status (i.e. open or closed) for any/all attraction(s) in any Disney Park
- Get general overview information for all rides in any Disney Park (as provided from Queue-Times.com API, no formatting.)

## Notes
This is an unofficial wrapper for data provided by [Queue-Times.com](https://queue-times.com). Please respect their service and avoid excessive requests.
