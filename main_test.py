import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "python_main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_load():
    """tests the load() function"""
    result = subprocess.run(
        ["python", "python_main.py", "load"],  # Assuming your main script is `main.py`
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming and loading data..." in result.stdout


def test_query():
    """tests the query() function"""
    result = subprocess.run(
        ["python", "python_main.py", "query"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Top 5 rows of the MatchResultsDB table:" in result.stdout


def test_create():
    """tests the create() function"""
    result = subprocess.run(
        [
            "python",
            "python_main.py",
            "create",
            "40",
            "2024-06-01",
            "Team A",
            "Team B",
            "3-2",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Create Record" in result.stdout


def test_delete():
    """tests the delete() function"""
    result = subprocess.run(
        ["python", "python_main.py", "delete", "23"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Delete Record" in result.stdout


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
    test_create()
    test_delete()
