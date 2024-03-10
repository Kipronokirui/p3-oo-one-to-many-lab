class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self):
        return self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        self.pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda x: x.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.owner = owner
        self.all_pets.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type")
        self.owner = owner