import pytest
from dataclasses import dataclass
from typing import List

# Датакласс для представления строки таблицы
@dataclass
class LanguageInfo:
    website: str
    popularity: int
    front_end: str
    back_end: str
    database: str
    notes: str

# Фиктивная функция, которая представляет получение данных из таблицы
def get_languages_data() -> List[LanguageInfo]:
    data = [
        LanguageInfo("Google", 2800000000, "JavaScript, TypeScript", "C, C++", "Bigtable", "The most used search engine in the world."),
        LanguageInfo("Facebook", 1120000000, "JavaScript, Typescript, Flow", "Hack/HHVM, Python, C++", "MariaDB, MySQL, HBase", "The most visited social networking site."),
        LanguageInfo("YouTube", 1100000000, "JavaScript, TypeScript", "Python, C, C++, Java, Go", "Vitess, BigTable, MariaDB", "The most popular video sharing site."),
        LanguageInfo("Yahoo", 750000000, "JavaScript", "PHP", "PostgreSQL, HBase, Cassandra", ""),
        LanguageInfo("Amazon", 2400000000, "JavaScript", "Java, C++, Perl", "DynamoDB, RDS/Aurora", "The most used e-commerce site in the world."),
    ]
    return data

# Параметризованный тест
@pytest.mark.parametrize("popularity_threshold", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_popularity_threshold(popularity_threshold):
    data = get_languages_data()
    errors = []

    for entry in data:
        if entry.popularity < popularity_threshold:
            error_message = (
                f"{entry.website} (Frontend:{entry.front_end}|Backend:{entry.back_end}) "
                f"has {entry.popularity} unique visitors per month. (Expected more than {popularity_threshold})"
            )
            errors.append(error_message)

    if errors:
        pytest.fail("\n".join(errors))


