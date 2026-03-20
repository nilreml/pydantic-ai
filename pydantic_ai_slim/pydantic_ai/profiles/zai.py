from __future__ import annotations as _annotations

from . import ModelProfile


def zai_model_profile(model_name: str) -> ModelProfile | None:
    """Get the model profile for a Z.ai model."""
    # New models/providers tend to support native structured outputs without schema instructions
    # Assume full support, only add special handling for cases known to require it

    return ModelProfile(
        supports_json_schema_output='glm-4.5v' not in model_name,
        # NOTE: glm-4-32b and glm-4.6(non-v) require schema instructions, 4.5, 4.5-air, 4.6v and 4.7 don't
        # native_output_requires_schema_in_instructions=model_name.endswith(('glm-4-32b', 'glm-4.6')),
        native_output_requires_schema_in_instructions=True,
    )
    # return None
