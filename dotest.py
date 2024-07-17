import pytest
if __name__ == '__main__':

    pytest_args = [
        "--cov=src",    # Replace with your package/module name
        "--cov-report=term-missing",       # Generates the terminal report with missing lines
        "--cov-report=html",               # Generates the HTML report
        # Add more arguments as needed
    ]
    pytest.main(pytest_args)