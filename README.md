# Weather Playlist

Web service to suggest a music playlist based on the current weather.

## Online Demo

http://weather-playlist.herokuapp.com/docs

## Requirements

- REST API
- Provide an endpoint to suggest a music playlist based on the city current weather.
- Provide an endpoint to show the requested city playlists stats.

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
