### Query MatchResultsDB

**Command:** `python python_main.py query`

**Return code:** 0

**STDOUT:**
```plaintext
Querying data...
Top 5 rows of the MatchResultsDB table:
+---------+-----------------+----------------------------+----------+--------------------+
|   Round | Date            | Team 1                     | Team 2   | FT                 |
+=========+=================+============================+==========+====================+
|       1 | Sat Aug 14 2010 | Bolton Wanderers FC        | 0-0      | Fulham FC          |
+---------+-----------------+----------------------------+----------+--------------------+
|       1 | Sat Aug 14 2010 | Wigan Athletic FC          | 0-4      | Blackpool FC       |
+---------+-----------------+----------------------------+----------+--------------------+
|       1 | Sat Aug 14 2010 | Aston Villa FC             | 3-0      | West Ham United FC |
+---------+-----------------+----------------------------+----------+--------------------+
|       1 | Sat Aug 14 2010 | Wolverhampton Wanderers FC | 2-1      | Stoke City FC      |
+---------+-----------------+----------------------------+----------+--------------------+
|       1 | Sat Aug 14 2010 | Sunderland AFC             | 2-2      | Birmingham City FC |
+---------+-----------------+----------------------------+----------+--------------------+

```

### Create Record

**Command:** `python python_main.py create 40 2024-06-01 Team A Team B 3-2`

**Return code:** 0

**STDOUT:**
```plaintext
Create Record
We should either have a new gameweek or an extra row in existing gameweeks
+---------+------------+----------+----------+------+
|   Round | Date       | Team 1   | Team 2   | FT   |
+=========+============+==========+==========+======+
|      40 | 2024-06-01 | Team A   | Team B   | 3-2  |
+---------+------------+----------+----------+------+

```

### Delete Record

**Command:** `python python_main.py delete 23`

**Return code:** 0

**STDOUT:**
```plaintext
Delete Record
Since we have deleted that gameweek it should be empty

```

