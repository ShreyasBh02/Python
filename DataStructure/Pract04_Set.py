## Handling Permissions (Allow/Deny)
allowed_permissions = {"read", "write", "execute"}
user_permissions = {"read", "execute"}

if "write" in allowed_permissions and "write" not in user_permissions:
    print("User does not have write permission.")
else:
    print("User has write permission.")


## Performing Set Operations
class_a = {"John", "Alice", "Bob"}
class_b = {"Alice", "David", "Eve"}
all_students = class_a | class_b
print("All Students:", all_students)
common_students = class_a & class_b
print("Common Students:", common_students)
only_class_a = class_a - class_b
print("Students only in Class A:", only_class_a)