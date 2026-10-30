import os
from tutor import hooks

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(TEMPLATES_DIR)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("lumen", "build/openedx/themes"),
    ]
)

# Force the rendering of scss files included in partials directories
hooks.Filters.ENV_PATTERNS_INCLUDE.add_items(
    [
        r"lumen/lms/static/sass/partials/lms/theme/",
        r"lumen/cms/static/sass/partials/cms/theme/",
    ]
)

# Register comprehensive theme directory in LMS and CMS settings
hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "openedx-lms-common-settings",
            """
ENABLE_COMPREHENSIVE_THEMING = True
if "/openedx/themes" not in COMPREHENSIVE_THEME_DIRS:
    COMPREHENSIVE_THEME_DIRS.append("/openedx/themes")
""",
        ),
        (
            "openedx-cms-common-settings",
            """
ENABLE_COMPREHENSIVE_THEMING = True
if "/openedx/themes" not in COMPREHENSIVE_THEME_DIRS:
    COMPREHENSIVE_THEME_DIRS.append("/openedx/themes")
""",
        ),
    ]
)
