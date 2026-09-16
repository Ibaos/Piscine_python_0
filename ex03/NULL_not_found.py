from typing import Any

def NULL_not_found(object: Any) -> int:
	obj_type = type(object)

	if object is None:
		print(f"Nothing: None {obj_type}")
	elif object != object:
		print(f"Cheese: nan {obj_type}")
	elif type(object) is int and object == 0:
		print(f"Zero: 0 {obj_type}")
	elif object == "":
		print(f"Empty:  {obj_type}")
	elif object is False:
		print(f"Fake: False {obj_type}")
	else:
		print("Type not Found")
		return 1

	return 0
	