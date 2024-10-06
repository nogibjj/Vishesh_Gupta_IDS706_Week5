from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query, create, delete, update
import sys

# Main script entry point
def main():
    if len(sys.argv) < 2:
        print("Please specify an operation: extract, load, query, create, delete.")
    else:
        operation = sys.argv[1]

        if operation == "extract":
            print("Extracting data...")
            extract()

        elif operation == "load":
            print("Transforming and loading data...")
            load()

        elif operation == "query":
            print("Querying data...")
            query()

        elif operation == "create":
            # Ensure enough arguments are passed to create a new record
            if len(sys.argv) == 7:
                gameweek = int(sys.argv[2])
                date = sys.argv[3]
                team1 = sys.argv[4]
                team2 = sys.argv[5]
                score = sys.argv[6]
                print("Create Record")
                create(gameweek, date, team1, team2, score)
            else:
                print(
                    "Insufficient arguments. Usage: python main.py create <gameweek> <date> <team1> <team2> <score>"
                )

        elif operation == "delete":
            # Ensure a gameweek argument is passed for deletion
            if len(sys.argv) == 3:
                gameweek = int(sys.argv[2])
                print("Delete Record")
                delete(gameweek)
            else:
                print("Insufficient arguments. Usage: python main.py delete <gameweek>")

        elif operation == "update":
            # Ensure enough arguments are passed to update the round number for a specific Team 1
            if len(sys.argv) == 4:
                team1 = sys.argv[2]
                new_round = int(sys.argv[3])
                print("Update Record")
                update(team1, new_round)
            else:
                print("Insufficient arguments. Usage: python main.py update_round <team1> <new_round>")


        else:
            print(
                "Unknown operation. Please use one of the following: extract, load, query, create, delete."
            )


if __name__ == "__main__":
    main()
