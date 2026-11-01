# Lumen

Lumen is a lightweight branding and theme plugin for Open edX (Sumac / Tutor 19).

## Quick Start
```bash
# 1. Install & enable (ensure tutor-indigo is disabled)
pip install -e ./tutor-lumen
tutor plugins disable indigo
tutor plugins enable lumen
tutor config save

# 2. Launch & set theme for LMS/Studio
tutor dev launch
tutor dev do settheme lumen

# 3. Build MFE images with Lumen branding
tutor images build mfe
tutor dev restart
```

## Changing the Primary Color
To change the primary color (`#0F766E`) in one place across:
- **LMS/Studio**: Update `$primary` in `tutor-lumen/tutorlumen/templates/lumen/{lms,cms}/static/sass/partials/{lms,cms}/theme/_extras.scss`.
- **MFEs**: Update `$primary` in `paragon/_variables.scss` in the `brand-lumen` repository, push the update, update the commit pin in `plugin.py`, and rebuild the MFE image (`tutor images build mfe`).

## Production Note
The MFE build installs `@edx/brand` from a remote Git URL or npm package. For `tutor local` builds, host `brand-lumen` in its own repository (e.g. `https://github.com/anan-d272/brand-lumen.git`) or publish it to an npm registry.
