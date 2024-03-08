# tests/test_base_model.py
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        model = BaseModel()
        self.assertTrue(isinstance(model, BaseModel))
        self.assertTrue(isinstance(model.id, str))
        self.assertTrue(isinstance(model.created_at, datetime))
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_serialization(self):
        model = BaseModel()
        serialized_data = model.to_dict()

        self.assertTrue("__class__" in serialized_data)
        self.assertTrue("id" in serialized_data)
        self.assertTrue("created_at" in serialized_data)
        self.assertTrue("updated_at" in serialized_data)

        self.assertEqual(serialized_data["__class__"], "BaseModel")
        self.assertEqual(serialized_data["id"], model.id)
        self.assertEqual(serialized_data["created_at"], model.created_at.isoformat())
        self.assertEqual(serialized_data["updated_at"], model.updated_at.isoformat())

    def test_deserialization(self):
        model = BaseModel()
        serialized_data = model.to_dict()

        new_model = BaseModel(**serialized_data)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
