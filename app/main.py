class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    # def set_spouse(self, spouse_name: str, is_husband: bool) -> None:
    #     spouse = Person.people[spouse_name]
    #     if spouse:
    #         if is_husband:
    #             self.husband = spouse
    #             # spouse.wife = self
    #         else:
    #             self.wife = spouse
    #             # spouse.husband = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]

        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return person_list
