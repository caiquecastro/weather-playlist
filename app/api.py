from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.errors import AppError
from app.core.config import settings
from app.services.stats import stats_service
from app.services.spotify import spotify_service
from app.services.openweather import openweather_service
from app.models import CityPlaylist, CityStats, Error


def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.exception_handler(AppError)
    async def app_exception_handler(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'detail': exc.message,
            }
        )

    @app.get('/stats', response_model=List[CityStats])
    def city_stats():
        return stats_service.top_access()

    @app.get(
        '/cities/{city}/playlists',
        response_model=CityPlaylist,
        responses={
            404: {
                'description': 'Resource not found',
                'model': Error,
            },
        },
    )
    def city_playlists(city: str):
        temperature = openweather_service.get_temperature(city)

        playlist = spotify_service.get_playlist_for_temperature(temperature)

        stats_service.register_access(city)

        return {
            'city': city,
            'temperature': temperature,
            'playlist': playlist,
        }

    return app
