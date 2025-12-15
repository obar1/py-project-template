import re


def test_app_name(app_config):
    assert app_config["app_name"] == "py-project-template"


def test_app_description(app_config):
    """match `template` and any text around"""
    regex_desc = app_config["app_description"]
    assert re.search(r"\btemplate\b", regex_desc, flags=re.IGNORECASE)
