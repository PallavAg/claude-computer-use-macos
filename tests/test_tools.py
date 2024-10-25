import pytest
from computer_use_demo.tools import BashTool, ComputerTool, EditTool, ToolCollection, ToolError

@pytest.fixture
def bash_tool():
    return BashTool()

@pytest.fixture
def computer_tool():
    return ComputerTool()

@pytest.fixture
def edit_tool():
    return EditTool()

@pytest.fixture
def tool_collection(bash_tool, computer_tool, edit_tool):
    return ToolCollection(bash_tool, computer_tool, edit_tool)

def test_bash_tool_restart(bash_tool):
    result = pytest.run(bash_tool(restart=True))
    assert result.system == "tool has been restarted."

def test_bash_tool_command(bash_tool):
    pytest.run(bash_tool(restart=True))
    result = pytest.run(bash_tool(command="echo 'Hello, World!'"))
    assert result.output.strip() == "Hello, World!"

def test_computer_tool_screenshot(computer_tool):
    result = pytest.run(computer_tool(action="screenshot"))
    assert result.base64_image is not None

def test_edit_tool_create(edit_tool):
    path = "/tmp/test_file.txt"
    result = pytest.run(edit_tool(command="create", path=path, file_text="Hello, World!"))
    assert result.output == f"File created successfully at: {path}"

def test_edit_tool_view(edit_tool):
    path = "/tmp/test_file.txt"
    pytest.run(edit_tool(command="create", path=path, file_text="Hello, World!"))
    result = pytest.run(edit_tool(command="view", path=path))
    assert "Hello, World!" in result.output

def test_tool_collection_run(tool_collection):
    result = pytest.run(tool_collection.run(name="bash", tool_input={"command": "echo 'Hello, World!'"}))
    assert result.output.strip() == "Hello, World!"

def test_tool_collection_invalid(tool_collection):
    result = pytest.run(tool_collection.run(name="invalid_tool", tool_input={}))
    assert result.error == "Tool invalid_tool is invalid"
