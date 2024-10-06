import subprocess
import os


def write_to_md(content):
    with open("test_results.md", "a") as f:
        f.write(content + "\n\n")


def log_subprocess_result(result, description):
    """Helper function to log subprocess result into a markdown file."""
    write_to_md(f"### {description}")
    write_to_md(f"**Command:** `{ ' '.join(result.args) }`")
    write_to_md(f"**Return code:** {result.returncode}")
    write_to_md(f"**STDOUT:**\n```plaintext\n{result.stdout}\n```")


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
    log_subprocess_result(result, "Query MatchResultsDB")


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
    log_subprocess_result(result, "Create Record")


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
    log_subprocess_result(result, "Delete Record")


def test_update():
    result = subprocess.run(
        ["python", "python_main.py", "update", "Wigan Athletic FC", "42"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Update Record" in result.stdout
    log_subprocess_result(
        result, "Update Record will have all Wigan Athletic FC set to record 42"
    )


if __name__ == "__main__":
    # Clear the existing .md file if it exists
    if os.path.exists("test_results.md"):
        os.remove("test_results.md")

    test_extract()
    test_load()
    test_query()
    test_create()
    test_delete()
    test_update()
