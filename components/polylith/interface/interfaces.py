from pathlib import Path

from polylith.files import create_file

template_docstring = """\
\"\"\"
{description}
\"\"\"

"""

template_content = """\
from . import {modulename}

__all__ = ["{modulename}"]
"""


init_template_content = """\
from .src.{namespace_path}.{package} import {modulename}
from .test.{namespace_path}.{package} import test_{modulename}

__all__ = ["{modulename}", "test_{modulename}"]
"""


def to_namespaced_path(package: str) -> str:
    parts = package.split("/")

    return ".".join(parts)


def create_interface(path: Path, options: dict) -> None:
    interface = create_file(path, "__init__.py")

    namespace = options["namespace"]
    package = options["package"]
    description = options["description"]
    modulename = options["modulename"]

    package_path = to_namespaced_path(package)

    docstring = (
        template_docstring.format(description=description) if description else ""
    )

    content = template_content.format(
        namespace=namespace, package=package_path, modulename=modulename
    )

    interface.write_text(docstring + content)


def create_init(path: Path, options: dict) -> None:
    interface = create_file(path, "__init__.py")

    namespace_path = options["namespace_path"].replace("/", ".")
    package = options["package"]
    description = options["description"]
    modulename = options["modulename"]

    package_path = to_namespaced_path(package)

    docstring = (
        template_docstring.format(description=description) if description else ""
    )

    content = init_template_content.format(
        namespace_path=namespace_path, package=package_path, modulename=modulename
    )

    interface.write_text(docstring + content)
