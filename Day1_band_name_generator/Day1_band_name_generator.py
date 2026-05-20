def band_name_generator() -> None:
	print("Welcome to the Band Name Generator.")
	first_name = str(input("What's the city that you live in?\n"))
	second_name = str(input("What's your pet's name?\n"))
	print(f"Your band name could be {first_name} {second_name}")

band_name_generator()