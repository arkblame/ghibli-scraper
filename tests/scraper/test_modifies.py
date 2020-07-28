import pytest

from scraper.modifier import modify_person_movies_list


@pytest.mark.parametrize("all_people, expectation",
                         [
                             ([], []),
                             (
                                     [{"name": "John Doe", "films": ["123"]}],
                                     [{"name": "John Doe", "films": ["123"]}]
                             ),
                             (
                                     [
                                         {"name": "John Doe",
                                          "films": ["123/456"]}
                                     ],
                                     [{"name": "John Doe", "films": ["456"]}]
                             )
                         ])
def test_modify_person_movies_list(all_people, expectation):
    modify_person_movies_list(all_people)
    assert all_people == expectation


@pytest.mark.parametrize("all_people, raise_excepation",
                         [
                             (None, TypeError),
                             ([{"name": "John Doe"}], TypeError),
                             ("string value", TypeError),
                             (["string value"], TypeError)
                         ])
def test_raising_errors__modify_person_movies_list(
        all_people, raise_excepation):
    with pytest.raises(raise_excepation):
        modify_person_movies_list(all_people)
