from typing import List


def modify_person_movies_list(all_people: List[dict]) -> List[dict]:
    """
        Method is responsible to modify persons movie list to contains only movie ID.

        :param all_people: contains list of all people

        :return: list of all people with modified "films" field.
    """
    for person in all_people:
        movie_list = [movie_id.split("/")[-1] for movie_id in person.get("films")]
        person["films"] = movie_list
