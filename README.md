# Disney Wait Times - Python
Simple Python library for accessing live Disney Parks' wait time data.
***
## What?
This project is designed to make it easy to incorporate Disney Wait Times in your projects from all the parks around the world.

## Installation
The project is available on [PyPI](https://pypi.org/project/disneyqueuetimes/).
<br>`pip install disneyqueuetimes`

## How?
### Quick Start
`import disneyqueuetimes as dqt`
<br>`if __name__ == "__main__":`
<br>`    print(dqt.getParkWaits("Magic Kingdom"))`
<br>This returns a dictionary of all current wait times in the Magic Kingdom.
<br>See the [wiki](https://github.com/oltaylor/disney-queue-times/wiki/) for all features!

## Features
- View the wait time(s) for any/all attraction(s) in any Disney Park
- View the status (i.e. open or closed) for any/all attraction(s) in any Disney Park
- Get general overview information for all rides in any Disney Park

## Valid Parks
Any Disney Theme Park worldwide. For keys and other information, see [this wiki page](https://github.com/oltaylor/disney-queue-times/wiki/Parks).

## Attribution
The library uses data from [ThemeParks.wiki API](https://api.themeparks.wiki/). Please be respectful and avoid excessive requests where possible.
