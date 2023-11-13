#!/usr/bin/python3
"""Base Class"""
import json
import csv


class Base:
    """Base Class"""
    __nb__objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = self.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ls = []
        if list_objs:
            for obj in list_objs:
                ls.append(obj.to_dictionary())
        with open(cls.__name__ + ".json",
                  "w", encoding="utf8") as file:
            file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ls = []
        try:
            with open(cls.__name__ + ".json",
                      "r", encoding="utf8") as file:
                list_dicts = Base.from_json_string(file.read())
                ls = [cls.create(**obj) for obj in list_dicts]
        finally:
            return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + ".csv",
                  "w", encoding="utf8") as file:
            if len(list_objs) > 0:
                column_order = [['id', 'width', 'height', 'x', 'y']]
                column_order.append(['id', 'size', 'x', 'y'])
                use = column_order[0 if cls.__name__ == "Rectangle" else 1]
                writer = csv.DictWriter(file, fieldnames=use)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        ls = []
        try:
            with open(cls.__name__ + ".csv",
                      "r", encoding="utf8") as file:
                column_order = [['id', 'width', 'height', 'x', 'y']]
                column_order.append(['id', 'size', 'x', 'y'])
                int_cols = ['id', 'width', 'height', 'size', 'x', 'y']
                use = column_order[0 if cls.__name__ == "Rectangle" else 1]
                reader = csv.DictReader(file, fieldnames=use)

                for col in int_cols:
                    reader.fieldtypes[col] = int
                for row in reader:
                    print(type(row))
                    print(row)
                exit()
                ls.append(cls.create(**row))

                # ls = [cls.create(**obj) for obj in reader]
        finally:
            ls
