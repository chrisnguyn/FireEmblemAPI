from fe13 import FE13

mapping = {
    'fe13': FE13
}


def get_games() -> dict:
    return {
        'fe13': 'Fire Emblem Awakening'
    }


def get_character(game: str, character: str) -> dict:
    return mapping[game].get_character(character)


def get_characters(game: str) -> dict:
    return mapping[game].get_characters()


def get_items(game: str) -> dict:
    return mapping[game].get_items()


def get_skills(game: str) -> dict:
    return mapping[game].get_skills()


def get_base_growths_for_character(game: str, character: str) -> dict:
    return mapping[game].get_base_growths_for_character(character)


def get_base_growths(game: str) -> dict:
    return mapping[game].get_base_growths()


def get_meta(game: str) -> dict:
    return mapping[game].get_meta()
