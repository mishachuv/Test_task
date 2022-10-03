import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask import Flask, jsonify, make_response, json

app = Flask(__name__)

DB_NAME = "manager"
DB_USER = "postgres"
DB_PASS = "nazankera"
DB_HOST = "localhost"
DB_PORT = 5432

# conn = psycopg2.connect(
#     user=DB_USER,
#     password=DB_PASS,
#     host=DB_HOST,
#     port=DB_PORT)
#
# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cur = conn.cursor()
# cur.execute('Drop database if exists Manager')
# cur.execute('Create database Manager')
#
# print("Database created successfully")
# cur.close()
# conn.close()

conn2 = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT)
cur2 = conn2.cursor()

print("Database connected successfully")

qdepartments = f"""CREATE TABLE IF NOT EXISTS manager.public.departments
                (
                    id integer generated always as identity not null,
                    department character varying(20) COLLATE pg_catalog."default",
                    location_id integer,
                    CONSTRAINT departments_pkey PRIMARY KEY (id),
                    CONSTRAINT fk_loc FOREIGN KEY (location_id)
                        REFERENCES public.locations (id) MATCH SIMPLE
                        ON UPDATE NO ACTION
                        ON DELETE NO ACTION
                 )"""

qdepartments_insert = f"""INSERT INTO manager.public.departments(department, location_id) \
                          VALUES ('HR', 1),
                                 ('Sales', 1),
                                 ('IT', 2),
                                 ('Accounting', 1),
                                 ('Manufacturing', 3),
                                 ('Shipping', 3)"""

qemployees = f""" CREATE TABLE IF NOT EXISTS manager.public.employees
            (
                id integer generated always as identity not null ,
                name character varying(20) COLLATE pg_catalog."default",
                hire_date date,
                gender character varying(20) COLLATE pg_catalog."default",
                age integer,
                salary integer,
                manager_id integer,
                department_id integer,
                CONSTRAINT employees_pkey PRIMARY KEY (id)
            ) """

qemployees_insert = f"""INSERT INTO manager.public.employees(name, hire_date, gender, age, salary, manager_id, department_id ) \
	                    VALUES ('Maslov Denis', '20010101', 'M', 50, 100000, null, null),
                               ('Ivanov Fedor', '20020413', 'M', 45, 80000, 1, 2),
                               ('Vlasov German', '20071103', 'M', 39, 75000, 1, 3),
                               ('Fedorov Sergey', '20050801', 'M', 42, 82000, 1, 5),
                               ('Andreev Oleg', '20080610', 'M', 35, 78000, 1, 6),
                               ('Pavlova Svetlana', '20090910', 'F', 39, 75000, 1, 1),
                               ('Zakharova Anna', '20050511', 'F', 48, 75000, 1, 4),
                               ('Moiseev Stepan', '20101010', 'M', 35, 52000, 2, 2),
                               ('Smirnova Ekaterina', '20121201', 'F', 30, 45000, 2, 2),
                               ('Kulikov Alexandr', '20090901', 'M', 32, 60000, 3, 3),
                               ('Alexeev Ivan', '20130725', 'M', 27, 53000, 4, 5),
                               ('Sorokin Ivan', '20150507', 'M', 25, 45000, 4, 1),
                               ('Romanov Maksim', '20070622', 'M', 30, 55000, 4, 5),
                               ('Kovalenko Petr', null, 'M', 22, 32000, 5, 6),
                               ('Filatov Andrey', '20090601', 'M', 24, 40000, 6, 1),
                               ('Savenko Inna', '20070201', 'F', 25, 45000, 6, 1),
                               ('Dorofeeva Inna', '20101110', 'F', 27, 48000, 7, 4)"""

qlocations = f""" CREATE TABLE IF NOT EXISTS manager.public.locations
                (
                    id integer generated always as identity not null ,
                    location character varying(20) COLLATE pg_catalog."default",
                    CONSTRAINT locations_pkey PRIMARY KEY (id)
                ) """

qlocations_insert = f"""INSERT INTO manager.public.locations(location) \
                        VALUES ('Northwest'),
                               ('South'),
                               ('East')"""

cur2.execute(qlocations)
print("Table locations created successfully")
cur2.execute(qlocations_insert)
cur2.execute(qdepartments)
print("Table departments created successfully")
cur2.execute(qdepartments_insert)
cur2.execute(qemployees)
print("Table employees created successfully")
cur2.execute(qemployees_insert)


conn2.commit()
q = f"""select name, department from employees e
        left join  departments d  on e.department_id = d.id
     """

q2 = f"""select location, sum(salary) from employees e
        inner join departments d  on e.department_id = d.id
        inner join locations l on l.id = d.location_id
        group by location
      """
cur2.execute(q2)
record2 = cur2.fetchall()
# for row in record2:
#     print(row)

q3 = f"""select * from employees"""
cur2.execute(q3)
record3 = cur2.fetchall()


@app.route('/', methods=['GET'])
def json():
    cur2.execute(q)
    data = cur2.fetchall()
    record = []
    content = {}
    for result in data:
        content = {'name': result[0], 'department': result[1]}
        record.append(content)
        content = {}
    return jsonify(record)

@app.route('/pandas', methods=['GET'])
def pandas():
    return record3


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1")

# cur2.close()
# conn2.commit()
