from decimal import Decimal

import psycopg2


class DBManager:
    """Класс для работы с БД"""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname="dbproject", **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получаем список всех компаний и количество вакансий у каждой компании."""

        self.cur.execute(
            """
                    SELECT employer_name, COUNT(vacancies.employer_id)
                    FROM employers
                    INNER JOIN vacancies USING (employer_id)
                    GROUP BY employer_name
                    ORDER BY COUNT DESC
            """
        )

        return self.cur.fetchall()

    def get_all_vacancies(self):
        """Получаем список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""

        self.cur.execute(
            """
                    SELECT e.employer_name, v.vacancy_name, v.salary, v.vacancy_url
                    FROM vacancies v
                    INNER JOIN employers e USING (employer_id)
                    WHERE v.salary IS NOT NULL AND v.salary != 0
                    ORDER BY v.salary DESC
            """
        )

        return self.cur.fetchall()

    def get_avg_salary(self):
        """Получаем среднюю зарплату по вакансиям"""

        self.cur.execute(
            """
                    SELECT AVG(salary)
                    FROM vacancies
            """
        )

        result = self.cur.fetchone()
        avg_salary = Decimal(result[0])
        formatted_avg_salary = format(avg_salary, ".2f")
        return formatted_avg_salary

    def get_vacancies_with_higher_salary(self):
        """Получаем список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

        avg_salary = self.get_avg_salary()[0][0]

        self.cur.execute(
            """
            SELECT v.vacancy_name, v.salary
            FROM vacancies v
            WHERE v.salary > %s
            """,
            (avg_salary,),
        )
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получаем список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""

        self.cur.execute(
            f"""
                    SELECT vacancy_name
                    FROM vacancies
                    WHERE vacancy_name LIKE '%{keyword.lower()}%'
            """
        )

        return self.cur.fetchall()
