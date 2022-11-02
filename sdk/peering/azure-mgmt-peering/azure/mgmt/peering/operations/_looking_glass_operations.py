# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import PeeringManagementClientMixinABC, _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_invoke_request(
    subscription_id: str,
    *,
    command: Union[str, _models.LookingGlassCommand],
    source_type: Union[str, _models.LookingGlassSourceType],
    source_location: str,
    destination_ip: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Peering/lookingGlass")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["command"] = _SERIALIZER.query("command", command, "str")
    _params["sourceType"] = _SERIALIZER.query("source_type", source_type, "str")
    _params["sourceLocation"] = _SERIALIZER.query("source_location", source_location, "str")
    _params["destinationIP"] = _SERIALIZER.query("destination_ip", destination_ip, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class LookingGlassOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.peering.PeeringManagementClient`'s
        :attr:`looking_glass` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def invoke(
        self,
        command: Union[str, _models.LookingGlassCommand],
        source_type: Union[str, _models.LookingGlassSourceType],
        source_location: str,
        destination_ip: str,
        **kwargs: Any
    ) -> _models.LookingGlassOutput:
        """Run looking glass functionality.

        :param command: The command to be executed: ping, traceroute, bgpRoute. Known values are:
         "Traceroute", "Ping", and "BgpRoute". Required.
        :type command: str or ~azure.mgmt.peering.models.LookingGlassCommand
        :param source_type: The type of the source: Edge site or Azure Region. Known values are:
         "EdgeSite" and "AzureRegion". Required.
        :type source_type: str or ~azure.mgmt.peering.models.LookingGlassSourceType
        :param source_location: The location of the source. Required.
        :type source_location: str
        :param destination_ip: The IP address of the destination. Required.
        :type destination_ip: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LookingGlassOutput or the result of cls(response)
        :rtype: ~azure.mgmt.peering.models.LookingGlassOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.LookingGlassOutput]

        request = build_invoke_request(
            subscription_id=self._config.subscription_id,
            command=command,
            source_type=source_type,
            source_location=source_location,
            destination_ip=destination_ip,
            api_version=api_version,
            template_url=self.invoke.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LookingGlassOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    invoke.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Peering/lookingGlass"}  # type: ignore