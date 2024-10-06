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

### Update Record will have all Wigan Athletic FC set to record 42

**Command:** `python python_main.py update Wigan Athletic FC 42`

**Return code:** 0

**STDOUT:**
```plaintext
Update Record
Post Update
+---------+-----------------+-------------------+----------+----------------------------+
|   Round | Date            | Team 1            | Team 2   | FT                         |
+=========+=================+===================+==========+============================+
|      42 | Sat Aug 14 2010 | Wigan Athletic FC | 0-4      | Blackpool FC               |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Aug 21 2010 | Wigan Athletic FC | 0-6      | Chelsea FC                 |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Sep 11 2010 | Wigan Athletic FC | 1-1      | Sunderland AFC             |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sun Sep 19 2010 | Wigan Athletic FC | 0-2      | Manchester City FC         |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Oct 2 2010  | Wigan Athletic FC | 2-0      | Wolverhampton Wanderers FC |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Oct 23 2010 | Wigan Athletic FC | 1-1      | Bolton Wanderers FC        |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Wed Nov 10 2010 | Wigan Athletic FC | 1-1      | Liverpool FC               |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Nov 13 2010 | Wigan Athletic FC | 1-0      | West Bromwich Albion FC    |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Dec 4 2010  | Wigan Athletic FC | 2-2      | Stoke City FC              |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Wed Dec 29 2010 | Wigan Athletic FC | 2-2      | Arsenal FC                 |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sun Jan 2 2011  | Wigan Athletic FC | 0-1      | Newcastle United FC        |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Tue Jan 25 2011 | Wigan Athletic FC | 1-2      | Aston Villa FC             |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Feb 5 2011  | Wigan Athletic FC | 4-3      | Blackburn Rovers FC        |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Feb 26 2011 | Wigan Athletic FC | 0-4      | Manchester United FC       |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Mar 19 2011 | Wigan Athletic FC | 2-1      | Birmingham City FC         |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Apr 2 2011  | Wigan Athletic FC | 0-0      | Tottenham Hotspur FC       |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sat Apr 30 2011 | Wigan Athletic FC | 1-1      | Everton FC                 |
+---------+-----------------+-------------------+----------+----------------------------+
|      42 | Sun May 15 2011 | Wigan Athletic FC | 3-2      | West Ham United FC         |
+---------+-----------------+-------------------+----------+----------------------------+

```

