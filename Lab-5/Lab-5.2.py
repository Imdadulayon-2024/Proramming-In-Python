def display_resources(resources):
    print("\nRESOURCE DETAILS")
    print("-" * 75)

    for resource in resources:
        print(f"ID: {resource.get('id', 'N/A')}")
        print(f"Name: {resource.get('name', 'Unknown')}")
        print(f"Type: {resource.get('type', 'N/A')}")
        print(f"Quantity: {resource.get('quantity', 'N/A')}")
        print("-" * 75)



resources = [
    {"id": 101, "name": "Laptop", "type": "Electronics", "quantity": 10},
    {"id": 102, "name": "Projector", "type": "Electronics", "quantity": 5},
    {"id": 103, "name": "Whiteboard", "type": "Classroom", "quantity": 8}
]

display_resources(resources)