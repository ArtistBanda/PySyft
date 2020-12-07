from ..blueprint import dcfl_blueprint as dcfl_route
from flask import request, Response
import json

from syft.core.node.common.service.repr_service import ReprMessage
from ...auth import error_handler, token_required

@dcfl_route.route("/requests", methods=["POST"])
@token_required
def create_request():
    def route_logic():
        # Get request body
        content = loads(request.data)

        syft_message = {}
        syft_message["message_class"] = ReprMessage # TODO: Create a new data request Message
        syft_message["message_content"] = content
        syft_message["sign_key"] =  # TODO: Method to map token into sign-key

        # Execute task
        status_code, response_body = task_handler(
            route_function=process_as_syft_message,
            data=syft_message,
            mandatory={
                "message_class": MissingRequestKeyError,
                "message_content": MissingRequestKeyError,
                "sign_key": MissingRequestKeyError,
            },
        )
        return response_body

    status_code, response_body = error_handler(process_as_syft_message)

    return Response(
        dumps(response_body), status=status_code, mimetype="application/json"
    )

@dcfl_route.route("/requests/<request_id>", methods=["GET"])
@token_required
def get_specific_request(request_id):
    def route_logic():
        # Get request body
        content = loads(request.data)

        syft_message = {}
        syft_message["message_class"] = ReprMessage # TODO: Get Specific Request Messages
        syft_message["message_content"] = content
        syft_message["sign_key"] =  # TODO: Method to map token into sign-key

        # Execute task
        status_code, response_body = task_handler(
            route_function=process_as_syft_message,
            data=syft_message,
            mandatory={
                "message_class": MissingRequestKeyError,
                "message_content": MissingRequestKeyError,
                "sign_key": MissingRequestKeyError,
            },
        )
        return response_body

    status_code, response_body = error_handler(process_as_syft_message)

    return Response(
        dumps(response_body), status=status_code, mimetype="application/json"
    )


@dcfl_route.route("/requests", methods=["GET"])
@token_required
def get_all_requests():
    def route_logic():
        # Get request body
        content = loads(request.data)

        syft_message = {}
        syft_message["message_class"] = ReprMessage # TODO: Get All Requests Message
        syft_message["message_content"] = content
        syft_message["sign_key"] =  # TODO: Method to map token into sign-key

        # Execute task
        status_code, response_body = task_handler(
            route_function=process_as_syft_message,
            data=syft_message,
            mandatory={
                "message_class": MissingRequestKeyError,
                "message_content": MissingRequestKeyError,
                "sign_key": MissingRequestKeyError,
            },
        )
        return response_body

    status_code, response_body = error_handler(process_as_syft_message)

    return Response(
        dumps(response_body), status=status_code, mimetype="application/json"
    )


@dcfl_route.route("/requests/<request_id>", methods=["PUT"])
@token_required
def update_request(request_id):
    def route_logic():
        # Get request body
        content = loads(request.data)

        syft_message = {}
        syft_message["message_class"] = ReprMessage # TODO: Update a data request
        syft_message["message_content"] = content
        syft_message["sign_key"] =  # TODO: Method to map token into sign-key

        # Execute task
        status_code, response_body = task_handler(
            route_function=process_as_syft_message,
            data=syft_message,
            mandatory={
                "message_class": MissingRequestKeyError,
                "message_content": MissingRequestKeyError,
                "sign_key": MissingRequestKeyError,
            },
        )
        return response_body

    status_code, response_body = error_handler(process_as_syft_message)

    return Response(
        dumps(response_body), status=status_code, mimetype="application/json"
    )


@dcfl_route.route("/requests/<request_id>", methods=["DELETE"])
@token_required
def delete_request(request_id):
    def route_logic():
        # Get request body
        content = loads(request.data)

        syft_message = {}
        syft_message["message_class"] = ReprMessage # TODO: Delete a Request Message
        syft_message["message_content"] = content
        syft_message["sign_key"] =  # TODO: Method to map token into sign-key

        # Execute task
        status_code, response_body = task_handler(
            route_function=process_as_syft_message,
            data=syft_message,
            mandatory={
                "message_class": MissingRequestKeyError,
                "message_content": MissingRequestKeyError,
                "sign_key": MissingRequestKeyError,
            },
        )
        return response_body

    status_code, response_body = error_handler(process_as_syft_message)

    return Response(
        dumps(response_body), status=status_code, mimetype="application/json"
    )