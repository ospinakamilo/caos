import os
import sys
import shutil
import unittest
from io import StringIO
from caos.cli_commands import command_init
from caos.style.console.tools import escape_ansi
from caos.utils.os import is_posix_os, is_win_os
from caos.utils.working_directory import get_current_dir


_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE = "[caos] init --> Creating virtual environment..."
_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE = "[caos] init --> SUCCESS: Virtual environment created"
_VIRTUAL_ENVIRONMENT_EXISTS_MESSAGE = "[caos] init --> INFO: Virtual environment already exists"
_CREATING_YAML_MESSAGE = "[caos] init --> Creating 'caos.yml'..."
_YAML_CREATED_MESSAGE = "[caos] init --> SUCCESS: 'caos.yml' created"
_YAML_EXISTS_MESSAGE = "[caos] init --> INFO: 'caos.yml' already exists"
_UPDATE_YAML_REMINDER_MESSAGE = "[caos] init --> INFO: Don't forget to update the 'caos.yml' file to point to the right virtual environment"

_CURRENT_DIR = get_current_dir()
_PYTHON_PATH_VENV_POSIX = os.path.abspath(_CURRENT_DIR+"/venv/bin/python")
_PYTHON_PATH_VENV_WIN = os.path.abspath(_CURRENT_DIR+"/venv/Scripts/python.exe")
_PIP_PATH_VENV_POSIX = os.path.abspath(_CURRENT_DIR+"/venv/bin/pip")
_PIP_PATH_VENV_WIN = os.path.abspath(_CURRENT_DIR+"/venv/Scripts/pip.exe")

class TestCommandInit(unittest.TestCase):

    def setUp(self) -> None:
        self.new_stdout, self.old_stdout = StringIO(), sys.stdout
        self.new_stderr, self.old_stderr = StringIO(), sys.stderr
        sys.stdout, sys.stderr = self.new_stdout, self.new_stderr
        if os.path.isdir("tmp"):
            shutil.rmtree("tmp")

    def tearDown(self) -> None:
        sys.stdout, sys.stderr = self.old_stdout, self.old_stderr

    def test_init_no_args(self):
        exit_code: int = command_init.entry_point(args=[])
        messages: str = escape_ansi(self.new_stdout.getvalue())

        if exit_code != 0:
            self.tearDown()
            print(messages)
            self.fail("There was a problem creating the environment")

        self.assertTrue(os.path.isdir(os.path.abspath(_CURRENT_DIR+"/venv")))
        self.assertTrue(os.path.isfile(os.path.abspath(_CURRENT_DIR+"/caos.yml")))

        self.assertIn(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, "", 1)

        self.assertIn(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, "", 1)

        self.assertIn(_CREATING_YAML_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_YAML_MESSAGE, "", 1)

        self.assertIn(_YAML_CREATED_MESSAGE, messages)

    def test_init_my_env(self):
        exit_code: int = command_init.entry_point(args=["my_env"])
        messages: str = escape_ansi(self.new_stdout.getvalue())

        if exit_code != 0:
            self.tearDown()
            print(messages)
            self.fail("There was a problem creating the environment")

        self.assertTrue(os.path.isdir(os.path.abspath(_CURRENT_DIR+"/my_env")))
        self.assertTrue(os.path.isfile(os.path.abspath(_CURRENT_DIR+"/caos.yml")))

        self.assertIn(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, "", 1)

        self.assertIn(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, "", 1)

        self.assertIn(_CREATING_YAML_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_YAML_MESSAGE, "", 1)

        self.assertIn(_YAML_CREATED_MESSAGE, messages)

    def test_init_venv_twice(self):
        command_init.entry_point(args=[])
        exit_code: int = command_init.entry_point(args=[])
        messages: str = escape_ansi(self.new_stdout.getvalue())

        if exit_code != 0:
            self.tearDown()
            print(messages)
            self.fail("There was a problem creating the environment")

        self.assertTrue(os.path.isdir(os.path.abspath(_CURRENT_DIR+"/venv")))
        self.assertTrue(os.path.isfile(os.path.abspath(_CURRENT_DIR+"/caos.yml")))
        
        self.assertIn(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, "", 1)
        
        self.assertIn(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, "", 1)
        
        self.assertIn(_CREATING_YAML_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_YAML_MESSAGE, "", 1)
        
        self.assertIn(_YAML_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_YAML_CREATED_MESSAGE, "", 1)
        
        self.assertIn(_VIRTUAL_ENVIRONMENT_EXISTS_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_EXISTS_MESSAGE, "", 1)
        
        self.assertIn(_YAML_EXISTS_MESSAGE, messages)

    def test_init_existing_json(self):
        command_init.entry_point(args=[])
        exit_code: int = command_init.entry_point(args=["my_env"])
        messages: str = escape_ansi(self.new_stdout.getvalue())

        if exit_code != 0:
            self.tearDown()
            print(messages)
            self.fail("There was a problem creating the environment")

        self.assertTrue(os.path.isdir(os.path.abspath(_CURRENT_DIR+"/venv")))
        self.assertTrue(os.path.isfile(os.path.abspath(_CURRENT_DIR+"/caos.yml")))
        
        self.assertIn(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, "", 1)
        
        self.assertIn(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, "", 1)
        
        self.assertIn(_CREATING_YAML_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_YAML_MESSAGE, "", 1)
        
        self.assertIn(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, messages)
        messages: str = messages.replace(_CREATING_VIRTUAL_ENVIRONMENT_MESSAGE, "", 1)
        
        self.assertIn(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_VIRTUAL_ENVIRONMENT_CREATED_MESSAGE, "", 1)
        
        self.assertIn(_YAML_CREATED_MESSAGE, messages)
        messages: str = messages.replace(_YAML_CREATED_MESSAGE, "", 1)
        
        self.assertIn(_YAML_EXISTS_MESSAGE, messages)
        messages: str = messages.replace(_YAML_EXISTS_MESSAGE, "", 1)
        
        self.assertIn(_UPDATE_YAML_REMINDER_MESSAGE, messages)

    def test_venv_binaries(self):
        exit_code: int = command_init.entry_point(args=[])
        messages: str = escape_ansi(self.new_stdout.getvalue())

        if exit_code != 0:
            self.tearDown()
            print(messages)
            self.fail("There was a problem creating the environment")

        if is_win_os():
            self.assertTrue(os.path.isfile(_PYTHON_PATH_VENV_WIN))
            self.assertTrue(os.path.isfile(_PIP_PATH_VENV_WIN))
        elif is_posix_os():
            self.assertTrue(os.path.isfile(_PYTHON_PATH_VENV_POSIX))
            self.assertTrue(os.path.isfile(_PIP_PATH_VENV_POSIX))
        else:
            self.fail("Invalid OS")


if __name__ == '__main__':
    unittest.main()