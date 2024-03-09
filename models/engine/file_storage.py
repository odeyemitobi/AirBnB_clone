import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
