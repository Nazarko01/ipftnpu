recipes = []

while True:
    print("\n1 - Додати рецепт")
    print("2 - Показати рецепти")
    print("3 - Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Назва рецепта: ")
        ingredients = input("Інгредієнти: ")
        recipes.append({"name": name, "ingredients": ingredients})
        print("Рецепт додано!")

    elif choice == "2":
        if len(recipes) == 0:
            print("Рецептів немає")
        else:
            for r in recipes:
                print("Назва:", r["name"])
                print("Інгредієнти:", r["ingredients"])
                print()

    elif choice == "3":
        break

    else:
        print("Невірна команда")