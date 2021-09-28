import requests

from environments.environmental_services import EnvironmentalService
from onboarding.exceptions import RequestNotSigned
from revoking.headers import RevokingHeader
from revoking.parameters import RevokingParameter
from revoking.request import RevokingRequest
from revoking.request_body import RevokingBody
from revoking.response import RevokingResponse


class Revoking(EnvironmentalService):

    def __init__(self, *args, **kwargs):
        self._public_key = kwargs.pop("public_key")
        self._private_key = kwargs.pop("private_key")
        super(Revoking, self).__init__(*args, **kwargs)

    def _create_request(self, params: RevokingParameter, url: str) -> RevokingRequest:
        body_params = params.get_body_params()
        request_body = RevokingBody(**body_params)

        header_params = params.get_header_params()
        request_header = RevokingHeader(**header_params)

        return RevokingRequest(header=request_header, body=request_body, url=url)

    def _perform_request(self, params: RevokingParameter, url: str) -> requests.Response:
        request = self._create_request(params, url)
        request.sign(self._private_key)
        if request.is_signed:
            return requests.post(
                url=request.get_url(),
                data=request.get_data(),
                headers=request.get_header()
            )
        raise RequestNotSigned

    def revoke(self, params: RevokingParameter) -> RevokingResponse:
        url = self._environment.get_revoke_url()
        http_response = self._perform_request(params=params, url=url)

        return RevokingResponse(http_response)