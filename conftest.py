import pytest
from xprocess import ProcessStarter

@pytest.fixture(scope="session", autouse=True)

def start_server(xprocess):
    class Starter(ProcessStarter):
        
        # The command to start your local server
        args = ["python", "-m", "http.server", "8080"]
        
        # This tells Pytest to wait until it sees this text in the logs 
        # before starting your tests (Python's server prints this on boot)
        pattern = "Serving HTTP on"

    # Start the process under the name "my_http_server"
    xprocess.ensure("my_http_server", Starter)
    
    yield
    
    # Safely terminate the process when all tests finish
    xprocess.getinfo("my_http_server").terminate()
