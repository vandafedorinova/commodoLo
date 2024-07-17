import uuid

prefix = "ITEM-"
unique_id = uuid.uuid4().hex[:6]  # Using the first 6 characters of a UUID for uniqueness

code_name_identifier = prefix + unique_id
print(code_name_identifier)
