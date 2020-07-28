import json
import logging
from typing import List, Optional
from urllib.request import urlopen

from scraper import GHIBLI_URL, SUPPORTED_DATA_TYPES, PEOPLE
from scraper.modifier import modify_person_movies_list

logger = logging.getLogger("Ghibli-scrapper")


def get_all_data(data_type: str) -> List[dict]:
    """
        Method is responsible to get all data based on type passed.

        :param data_type: string. Supported values: "people", "films"

        :return:
    """
    logger.info("Getting data from server.")
    if data_type not in SUPPORTED_DATA_TYPES:
        raise ValueError(
            f"Not supported data type."
            f"Data type should be one of: {SUPPORTED_DATA_TYPES}")

    url = "/".join([GHIBLI_URL, data_type, "?limit=250"])
    response = urlopen(url).read().decode("utf-8")

    data = json.loads(response)

    return data


def get_cast_for_movie(
        movie_data: dict,
        all_people: Optional[List[dict]]) -> None:
    """
        Method is responsible for getting full cast for given movie.

        :param movie_data: dictionary that contains movie data from API
        :param all_people: optional argument that contains list of all people
    """
    if not all_people:
        logger.debug("No data provided for cast. Getting data from API.")
        all_people = get_all_data(PEOPLE)

    modify_person_movies_list(all_people)

    movie_data['cast'] = [person for person in all_people if
                          movie_data.get("id") in person.get("films")]
