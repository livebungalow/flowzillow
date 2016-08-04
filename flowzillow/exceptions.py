class ZillowError(Exception):
    def __init__(self, response):
        super(ZillowError, self).__init__(
            "There was a problem with your request. Status code {}, Content {}".
            format(response.status_code, response.content)
        )


class CaptchaError(Exception):
    def __init__(self, response):
        super(CaptchaError, self).__init__(
            "The request was captcha'd! Status code {}, Content {}"
            .format(response.status_code, response.content)
        )
