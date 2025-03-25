# -*- coding: utf-8 -*-
from re import compile, sub, MULTILINE


class QVariableStyleSheet(object):
    """
    QVariableStyleSheet class.
    """

    def __init__(self, stylesheet):
        """
        Initialize QVariableStyleSheet with the provided stylesheet.
        :param stylesheet: (str | unicode | QString) The stylesheet content.
        """
        self.__m_stylesheet = stylesheet  # type: str

    def setStyleSheet(self, stylesheet):
        """
        Set the stylesheet for the QVariableStyleSheet.
        :param stylesheet: (str | unicode | QString) The new stylesheet content.
        :return:
        """
        self.__m_stylesheet = stylesheet  # type: str

    def styleSheet(self):
        """
        Get the stylesheet for the QVariableStyleSheet.
        :return: str | unicode | QString
        """
        return self.__m_stylesheet

    def process(self):
        """
        Process the CSS variables in the QSS.
        :return: (str | unicode | QString) The processed stylesheet content.
        """
        theme = self.__m_stylesheet  # type: str
        # Process CSS variables in QSS.
        rootExpression = compile(r":root\s*\n*\s*\{\n*\s*(--.*:.*;\n*)*\n*\s*\}", MULTILINE)  # type: compile
        variableExpression = compile(r"--[a-zA-Z0-9\-\_]+:\s*[a-zA-Z0-9\-\_\#]+;")  # type: compile
        variableUsageExpression = compile(r"var\(--([a-zA-Z0-9\-]*)*[\)]{1}")  # type: compile
        commentExpression = compile(r"\/\*[^*]*\*+([^/*][^*]*\*+)*\/")  # type: compile
        theme = commentExpression.sub("", theme)  # type: str
        theme = sub(r"[\n]{2,}", "\n", theme)  # type: str
        theme = sub(r"[\s]{2,}", " ", theme)  # type: str
        iterator = rootExpression.finditer(theme)  # type: iter
        variables = {}  # type: dict[str, str]
        for rootMatch in iterator:
            root = rootMatch.group(0)  # type: str
            theme = rootExpression.sub("", theme)  # type: str
            variableIterator = variableExpression.finditer(root)  # type: iter
            for variableMatch in variableIterator:
                variable = variableMatch.group(0)  # type: str
                split = variable.split(":")  # type: list[str]
                if len(split) == 2:
                    key = split[0]  # type: str
                    value = split[1]  # type: str
                    while value.startswith(" "):
                        value = value[1:]  # type: str
                    while key.startswith(" "):
                        key = key[1:]  # type: str
                    value = sub(r";$", "", value)  # type: str
                    variables[key] = value  # type: str
        iterator = variableUsageExpression.finditer(theme)  # type: iter
        for variableMatch in iterator:
            variable = variableMatch.group(0)  # type: str
            variable = variable.replace("var(", "")  # type: str
            variable = sub(r"\)$", "", variable)  # type: str
            replacement = variables.get(variable, "")  # type: str
            theme = theme.replace(variableMatch.group(0), replacement)  # type: str
        # theme = sub("", theme, variableUsageExpression) # type: str
        return theme
