from uuid import uuid4
from sys import argv
from faker import Faker


def export_data(arr: list[str]) -> None:
    raise NotImplementedError()

def generate_objects(count= 50):
    arr: list[dict] = []
    
    for _ in range(count):
        obj: dict = {
            "template_id": str(uuid4),
            "template_category": fake.first_name(),
            "template_title": fake.text(),
            "template_text": fake.text()
        }
        arr.append(obj)
    
    return arr

if __name__ == "__main__":

    fake = Faker()

    object_arr = None

    if len(argv) > 1:
        if str(argv[1]).isdigit():
            print(f"Generating {argv[1]} objects")
            object_arr = generate_objects(argv[1])

    if len(argv) <= 1:
        print("No number given, generating 50 objects...")
        object_arr = generate_objects()
    
    print(object_arr)