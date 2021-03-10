import random

YEARS = 10


def main():
    population = 1000
    count = 1
    count_dead = 0
    count_born = 0
    print(f"Starting population: {population}")
    simulate_gophers(count, count_born, count_dead, population)


def simulate_gophers(count, count_born, count_dead, population):
    for i in range(YEARS):
        gophers_born = random_gopher_births(population)
        gophers_dead = random_gopher_deaths(population)
        count_dead += gophers_dead * -1
        count_born += gophers_born
        population += gophers_born + gophers_dead
        print(f"Yeah {count}\n")
        print(f"{gophers_born} gophers born. {gophers_dead * -1} died. \nPopulation: {population}")
        count += 1


def random_gopher_deaths(population):
    dead_gophers = 0
    min_death_percentage = int(population * .05)
    max_death_percentage = int(population * .25)
    for gophers in range(0, population):
        death_chance = random.randint(0, population)
        if death_chance in range(min_death_percentage, max_death_percentage):
            dead_gophers += 1
    return dead_gophers * -1


def random_gopher_births(population):
    gophers_born = 0
    min_birth_percentage = int(population * .1)
    max_birth_percentage = int(population * .2)
    for gophers in range(0, population):
        birth_chance = random.randint(0, population)
        if birth_chance in range(min_birth_percentage, max_birth_percentage):
            gophers_born += 1
    return gophers_born


def calculate_year(population):
    if population > 3:
        return False
    return True


main()
