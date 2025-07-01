# step 1
cookbook = []

# step 2
def create(recipe):
    cookbook.append(recipe)
    print(f'"{recipe}" has been added to the cookbook.')

# step 3
def read(index):
    if 0 <= index < len(cookbook):
        print(f'Recipe at index {index}: {cookbook[index]}')
        return cookbook[index]
    else:
        print("Invalid index. No recipe found.")

# step 4
def update(index, recipe):
    if 0 <= index < len(cookbook):
        print(f'Updating recipe at index {index} from "{cookbook[index]}" to "{recipe}".')
        cookbook[index] = recipe
    else:
        print("Invalid index. Cannot update recipe.")

# step 5
def destroy(index):
    if 0 <= index < len(cookbook):
        removed = cookbook.pop(index)
        print(f'"{removed}" has been removed from the cookbook.')
    else:
        print("Invalid index. Cannot delete recipe.")

# sstep 6
def list_all_recipes():
    if cookbook:
        print("All recipes in the cookbook:")
        for i, recipe in enumerate(cookbook):
            print(f"{i}: {recipe}")
    else:
        print("The cookbook is empty.")

# step 7
def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            index = int(index)
            recipe = input("Enter the new name for the recipe: ")
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()