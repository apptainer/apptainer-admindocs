def variableReplace(app, docname, source):
    """
    Takes the source on rst and replaces all the needed variables declared on
    variable_replacements structure
    """
    result = source[0]
    for key in app.config.variable_replacements:
        result = result.replace(key, app.config.variable_replacements[key])
    source[0] = result


# Add the needed variables to be replaced either on code or on text on the next
# dictionary structure.
variable_replacements = {
    # This is used in install instructions, so should be a full version
    "{InstallationVersion}" : "1.0.0",
    "{userdocs}" : "https://apptainer.org/docs/user/1.0",
    "{adminversion}": "1.0",
    "{userversion}": "1.0",
    "{Project}": "Apptainer",
    "{AProject}": "An Apptainer",
    "{aProject}": "an Apptainer",
    # Version of Go to be used in install instructions
    "{GoVersion}": "1.17.6",
    "{ENVPREFIX}": "APPTAINER",
    "{orgrepo}": "apptainer/apptainer",
    "{command}": "apptainer"
}


def setup(app):
    app.add_config_value('variable_replacements', {}, True)
    app.connect('source-read', variableReplace)
    app.add_css_file('custom.css')
