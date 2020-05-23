class AppError(Exception):
    def __init__(self, message, status_code):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


class NotFoundError(AppError):
    def __init__(self, message='Resource was not found'):
        AppError.__init__(self, message, 404)
