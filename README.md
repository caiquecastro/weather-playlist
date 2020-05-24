# Weather Playlist

Web service to suggest a music playlist based on the current weather.

## Online Demo

http://weather-playlist.herokuapp.com/docs

## Requirements

- REST API
- Provide an endpoint to suggest a music playlist based on the city current weather.
- Provide an endpoint to show the requested city playlists stats.

## Installation

### Requirements to install

- Python (3.8)
- Docker
- Docker Compose
- OpenWeatherMap API key [Docs](https://openweathermap.org/api)
- Spotify API key [Docs](https://developer.spotify.com/documentation/web-api/) -
[Dashboard](https://developer.spotify.com/dashboard/)

### Instructions

1. Create the .env file. You can copy it from the example.

```
cp .env.example .env
```

2. Fill the environment variables

3. Start the containers from docker-compose manifest file

```
docker-compose up -d
```

## Endpoints

```
GET /cities/{city_name}/playlists   - Playlist suggestion
GET /stats                          - Service stats
```

## Architecture

This webservice uses two external services. We need to ensure not to exceed their API calls.
Considering that the temperature for a city does not suddenly change we can cache its value
for a time. We are caching it for one hour. The same applies for the playlist for a genre.
The caching strategy helps for latency, fault tolerancy, scalability.
It uses [Sentry](https://sentry.io/) for application monitoring and error tracking.

```
--------------------    ----------------------    -----------------------     ------------------------
|                  |    |  This application  |    |                     |     |                      |
| Browser (Client) | -> |     App Server     | -> |    Cache (Redis)    |  -> |   External Service   |
|                  |    | (weather playlist) |    |                     |     |                      |
--------------------    ----------------------    -----------------------     ------------------------

```

## TODO

- Improve docs
- Rate Limit
- Auth
