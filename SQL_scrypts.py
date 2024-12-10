"""
1.

SELECT
    d.id AS department_id,
    d.name AS department_name
FROM
    department d
LEFT JOIN
    employee e
ON
    d.id = e.department_id
WHERE
    e.id IS NULL;
"""

"""
The query selects two columns from the department table (d is the initial for the department): 
To have a clear new table the names of the rows are changed, respectively: 
id = department_id and name = department_name.
By using "LEFT JOIN" the table (d) and the employee table (e) are joined together.
The WHERE clause filters the results to include only departments with no employees associated with the department. 
Since a LEFT JOIN produces NULL values for the no match, using the expression "e.id IS NULL"
filters the result to show departments that have no employees assigned to them.
"""



"""

2.

SELECT 
    e.id AS employee_id,
    d.id AS department_id,
    d.name AS department_name
FROM 
    employee e
INNER JOIN 
    department d
ON 
    e.department_id = d.id
GROUP BY 
    d.id, d.name 
HAVING 
	count(e.id)<3
"""

"""
Here the difference is mostly in "GROUP BY"
It aggregates rows into groups based on the department_id and department_name.
"HAVING" is used to filter groups created by GROUP BY.
And "COUNT(e.id)" counts the number of employees (e.id) in each department.
"""