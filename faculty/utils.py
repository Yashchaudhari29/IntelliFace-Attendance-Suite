import psycopg2
from college_admin.models import *
import pandas as pd

db_params = {
    "host": "monorail.proxy.rlwy.net",
    "database": "railway",
    "user": "postgres",
    "password": "f6gca4GaC46E-BGeAA6f1c554BEg2Cdg",
    "port": "42384",
}


def MakePK(tn,cn):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                    ALTER TABLE {tn}
                    ADD PRIMARY KEY ({cn});"""
                )
                connection.commit()
    except psycopg2.Error as e:
        print("Error updating data:", e)


def fetch_data_from_postgres(db_params, query):
    try:
        with psycopg2.connect(**db_params) as connection:
            data_frame = pd.read_sql_query(query, connection)
        return data_frame
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def row_column(attendance_data, en_no, date):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                    UPDATE attendance_system
                    SET "{date}" = %s
                    WHERE en_no = %s;
                    """,
                    (attendance_data, en_no),
                )
                connection.commit()
    except psycopg2.Error as e:
        print("Error updating data:", e)


def AddData(data_db):
    for iter in data_db:
        try:
            with psycopg2.connect(**db_params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT 1 FROM attendance_system WHERE en_no = %s;
                        """,
                        (iter["en_no"],),
                    )
                    if not cursor.fetchone():
                        cursor.execute(
                            """
                            INSERT INTO attendance_system (name, en_no)
                            VALUES (%s, %s);
                            """,
                            (iter["name"], iter["en_no"]),
                        )
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)


# ***************************


def DropTable(table_name):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                DROP TABLE {table_name};
                """
                )

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# ***************************


def DropColumn(table_name, column_name):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                ALTER TABLE {table_name}
                DROP COLUMN "{column_name}";
                """
                )
                print("column droped!")

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# ***************************


def CreateColumn(table_name, column_name, d_type):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                ALTER TABLE {table_name}
                ADD COLUMN "{column_name}" {d_type};
                """
                )
                print("column creatred!")

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# ***************************


def FetchData(table_name):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                data = cursor.execute(
                    f"""
                SELECT * FROM {table_name};
                """
                )
                return data

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# ***************************


def FetchColumn(table_name, column_name):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                    SELECT {column_name}
                    FROM {table_name};
                    """
                )
                data = cursor.fetchall()
                return data

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


# ***************************


def Truncate_column(table_name, column_name):
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                data = cursor.execute(
                    f"""
                UPDATE {table_name}
                SET "{column_name}" = NULL;
                """
                )
                return data

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
import os

def SetFalse():
    register.objects.all().update(attended=False)
