import numpy as np
import matplotlib.pyplot as plt

def disease_spread_simulation_custom(population, mortality_rate, recovery_rate):
    cumulative_risk = 0

    # Simulation logic
    # Assuming a single-day simulation
    # If you want to remove the simulation for multiple days, set simulation_days = 1
    for _ in range(1):
        # Calculate the probability of infection for each susceptible individual
        infection_probabilities = mortality_rate * np.sum(population == 0) / population_size
        
        # Infect susceptible individuals based on calculated probabilities
        new_infections = np.random.rand(population_size) < infection_probabilities
        population[new_infections & (population == 0)] = 1

        # Calculate and store cumulative risk for the day
        cumulative_risk = np.sum(infection_probabilities)

        # Determine outcomes (recover or die) for infected individuals
        infected_individuals = (population == 1)
        outcomes = np.random.rand(np.sum(infected_individuals)) < mortality_rate
        population[infected_individuals] = 0  # Recovered individuals
        population[infected_individuals & outcomes] = -1  # Mark individuals who die

    # Calculate survival rate
    survival_rate = np.sum(population == 0) / population_size

    return population, cumulative_risk, survival_rate

# User input for simulation parameters
num_cities = int(input("Enter the number of cities: "))

# Arrays to store data for each city
cumulative_risks = []
survival_rates = []

# Plotting data
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Predefined list of colors
city_colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

for city in range(1, num_cities + 1):
    print(f"\nCity {city}:")
    area_name = input("Enter the name of the area: ")
    population_size = int(input("Enter the population size for the area: "))

    # User input for mortality rate and recovery rate
    mortality_rate = float(input("Enter the mortality rate for the area (0-1): "))
    recovery_rate = float(input("Enter the recovery rate for the area (0-1): "))

    # Generate synthetic dataset
    synthetic_dataset = np.zeros(population_size)

    # Run simulation using the synthetic dataset
    result, cumulative_risk, survival_rate = disease_spread_simulation_custom(synthetic_dataset, mortality_rate, recovery_rate)

    # Append data to arrays
    cumulative_risks.append(cumulative_risk)
    survival_rates.append(survival_rate)

    # Add jitter to x-coordinates for better visualization
    jittered_city = city + np.random.normal(0, 0.1)

    # Plot for Cumulative Risk
    ax1.plot(jittered_city, cumulative_risk, marker='o', linestyle='-', label=area_name, color=city_colors[city - 1])

    # Plot for Mortality Rate
    ax2.plot(jittered_city, mortality_rate, marker='o', linestyle='-', label=area_name, color=city_colors[city - 1])

    # Plot for Survival Rate
    ax3.plot(jittered_city, survival_rate, marker='o', linestyle='-', label=area_name, color=city_colors[city - 1])

# Set x-axis labels
ax1.set_xticks(range(1, num_cities + 1))
ax1.set_xticklabels([f'City {i}' for i in range(1, num_cities + 1)])

ax2.set_xticks(range(1, num_cities + 1))
ax2.set_xticklabels([f'City {i}' for i in range(1, num_cities + 1)])

ax3.set_xticks(range(1, num_cities + 1))
ax3.set_xticklabels([f'City {i}' for i in range(1, num_cities + 1)])

# Set titles and labels
ax1.set_title('Cumulative Risk for Cities')
ax1.set_ylabel('Cumulative Risk')
ax1.legend()

ax2.set_title('Mortality Rate for Cities')
ax2.set_ylabel('Mortality Rate')
ax2.legend()

ax3.set_title('Survival Rate for Cities')
ax3.set_ylabel('Survival Rate')
ax3.legend()

plt.tight_layout()
plt.show()
