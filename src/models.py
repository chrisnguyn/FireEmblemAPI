import json


class Game():

    def __init__(self, title: str):
        self.title = title

    def __load_json(self, json_file: str) -> list[dict]:
        with open(json_file, 'r') as f:
            return json.load(f)

    def get_character(self, name: str) -> dict or None:
        characters = self.get_characters()

        for character in characters:
            if character['name'].replace('\'', '').lower() == name.lower():
                return character
        else:
            return None

    def get_characters(self) -> list[dict]:
        characters = self.__load_json('%s/characters.json' % self.title)

        return characters

    def get_skills(self) -> list[dict]:
        skills = self.__load_json('%s/skills.json' % self.title)

        return skills

    def get_base_growths_for_character(self, character: str) -> dict or None:
        base_growths = self.get_base_growths()

        for base_growth in base_growths:
            if base_growth['name'].replace('\'', '').lower() == character.lower():
                return base_growth
        else:
            return None

    def get_base_growths(self) -> list[dict]:
        base_growths = self.__load_json('%s/base_growths.json' % self.title)

        return base_growths

    def get_meta(self) -> list[dict]:
        meta = self.__load_json('%s/meta.json' % self.title)

        return meta
