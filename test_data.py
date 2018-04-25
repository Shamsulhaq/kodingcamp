from faker import Faker
import random
import csv
import pprint


pp = pprint.PrettyPrinter(indent=4)
fake = Faker()


def get_all_skills():
    """
    Skills data are from stackexchange data explorer.
    SQL query:
    SELECT TOP 100
        t.tagName
    FROM tags t
    WHERE t.Count > 100000
    ORDER BY t.tagName
    """
    skills = []
    with open('fixtures/skills.csv', newline='') as csvfile:
        skillreader = csv.reader(csvfile)
        for row in skillreader:
            skills.append(row[0])
    return skills


def create_user_data(n):
    user_data = []
    skills = get_all_skills()
    for _ in range(0,n):
        person = {'0': [fake.first_name_male(), fake.last_name_male(), 'M'],
                  '1': [fake.first_name_female(), fake.last_name_female(), 'F']}
        rand = random.randint(0,1)
        start_skill = random.randint(0, len(skills))
        end_skill = random.randint(0, len(skills))
        d = {
            'first_name': person[str(rand)][0],
            'last_name': person[str(rand)][1],
            'email': fake.email(),
            'birthdate': fake.date_between(start_date='-60y', end_date='-18y'),
            'sex': person[str(rand)][2],
            'contact': fake.phone_number(),
            'address': fake.address(),
            'skills': skills[min(start_skill, end_skill):max(start_skill, end_skill)],
            'interests': skills[0:min(start_skill, end_skill)] or skills[max(start_skill, end_skill):-1],
            'date_joined': fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
        }
        user_data.append(d)
    return user_data


def write_test_data_csv():
    test_data = create_user_data(10)
    pp.pprint(test_data)
    with open('test_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'sex', 'email', 'birthdate', 
                      'contact', 'address', 'date_joined',
                      'interests', 'skills']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in test_data:
            writer.writerow(row)
    print("Data write done!")


if __name__ == '__main__':
    write_test_data_csv()