#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(type(my_model.my_number), int)

        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

        my_model_json = my_model.to_dict()
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertEqual(type(my_model_json["__class__"]), str)
        self.assertEqual(type(my_model_json["id"]), str)
        self.assertEqual(type(my_model_json["name"]), str)
        self.assertEqual(type(my_model_json["my_number"]), int)


if __name__ == "__main__":
    unittest.main()
