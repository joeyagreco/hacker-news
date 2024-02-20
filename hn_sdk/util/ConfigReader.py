import configparser
import os
from typing import Optional


class ConfigReader:
    """
    Used to read from .properties files
    """

    @staticmethod
    def get(
        propertyFile: str, section: str, name: Optional[str] = None, as_type: type = str
    ) -> str | int | float | bool | dict:
        configParser = configparser.ConfigParser(
            converters={"list": lambda x: [i.strip() for i in x.split(",")]}
        )
        propertiesDirectory = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "../property")
        )
        configParser.read(os.path.join(propertiesDirectory, f"{propertyFile}.properties"))
        # if name is not given, return the entire section as a dictionary
        if name is None:
            return dict(configParser[section])
        value = None
        # cast as type
        if as_type == list:
            value = configParser.getlist(section, name)
        elif as_type in (str, int, float):
            value = as_type(configParser[section][name])
        else:
            raise ValueError(f"Type '{as_type}' not supported for conversion.")
        return value
