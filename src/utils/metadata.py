from typing import Dict

from src.models.chat import ResponseMetadata


def build_metadata(response_metadata: Dict) -> ResponseMetadata:
    """Build response metadata.

    :param response_metadata: model response metadata
    :return: metadata
    """
    metadata = ResponseMetadata(
        model_name=response_metadata["model_name"],
        completion_time=response_metadata["token_usage"]["completion_time"],
        prompt_time=response_metadata["token_usage"]["prompt_time"],
        prompt_tokens=response_metadata["token_usage"]["prompt_tokens"],
        total_tokens=response_metadata["token_usage"]["total_tokens"],
    )
    return metadata
