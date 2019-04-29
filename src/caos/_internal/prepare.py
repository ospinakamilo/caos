"""prepare - Create and prepare the virtual environment for the project"""

import os
import venv
import json
import common.constants
from caos._internal.exceptions import VenvExistsError

_console_messages={
    "success":"Success: Virtual environment created",
    "fail": "Fail: Virtual environment could not be created",
    "venv_exists": "Fail: Virtual environment folder already exists",
    "permission_error": "Fail: Virtual environment could not be created due to permission errors",
}

def create_venv():
    try:
        exists = os.path.isdir(common.constants._CAOS_VENV_DIR)
        if exists:
            raise VenvExistsError()        
        venv.create(env_dir=common.constants._CAOS_VENV_DIR, with_pip=True, system_site_packages=True)

        print(_console_messages["success"])
    except VenvExistsError:
        print (_console_messages["venv_exists"])
    except PermissionError:
        print(_console_messages["permission_error"])
    except Exception:
        print(_console_messages["fail"])