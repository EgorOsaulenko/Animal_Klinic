import json

from app.data import list_files, open_files


def remove_animal(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тварину '{animal}' успішно видалено."
    return msg


def heal_animal(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    heal_animals = open_files.get_heal_animals()
    heal_animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.HEAL_ANIMALS, "w", encoding="utf-8") as file:
        json.dump(heal_animals, file)

    msg = f"Тварину '{animal}' успішно вилікувано"
