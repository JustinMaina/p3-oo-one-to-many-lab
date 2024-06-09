class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def __str__(self):
        return f"{self.name} ({self.pet_type})"


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")

        self.name = name
        self.pets = []

    def pets(self):
        return self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)