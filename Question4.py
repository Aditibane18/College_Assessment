import re

def validate_number_plate(plate):
    pattern = r"^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$"
    if re.match(pattern, plate):
        return "The number plate is valid."
    else:
        return "The number plate is invalid."

if __name__ == "__main__":
    test_plates = [
        "MH 12 AB 1234",  
        "MH12AB1234",   
        "MHA 12 AB 1234", 
        "MH 123 AB 1234", 
        "MH 12 AB 12345", 
    ]
    for plate in test_plates:
        print(f"Number Plate: {plate} -> {validate_number_plate(plate)}")
