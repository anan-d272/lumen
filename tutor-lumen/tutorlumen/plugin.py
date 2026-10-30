import os
from tutor import hooks

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(TEMPLATES_DIR)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("lumen", "build/openedx/themes"),
    ]
)
