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

# Register comprehensive theme and MFE branding patches
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
        (
            "mfe-dockerfile-post-npm-install",
            """
RUN npm install '@edx/brand@git+https://github.com/anan-d272/brand-lumen.git#e8519359d1da0eb200cfbf6aa43e264f86542364'
""",
        ),
        (
            "mfe-lms-common-settings",
            """
MFE_CONFIG["LOGO_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo.svg"
MFE_CONFIG["LOGO_WHITE_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo-white.svg"
MFE_CONFIG["LOGO_TRADEMARK_URL"] = LMS_ROOT_URL + "/theming/asset/images/logo.svg"
MFE_CONFIG["FAVICON_URL"] = LMS_ROOT_URL + "/theming/asset/images/favicon.svg"
""",
        ),
    ]
)
