from PIL import Image               
import numpy as np                   
import os                           

def load_image(image_path, size=(16, 16)):             
    image = Image.open(image_path)                    
    if image.mode != 'L':                             
        print("[INFO] Convertim imaginea la grayscale.") 
        image = image.convert('L')                   
    image = image.resize(size)                       
    return np.array(image)                           


def load_ascii_characters(file_path):                 
    with open(file_path, 'r') as f:                   
        chars = f.read().strip()                      
    return list(chars)                                


def create_ascii_lut(ascii_chars):                     
    gray_levels = np.linspace(0, 1, len(ascii_chars))  
    return dict(zip(ascii_chars, gray_levels))         


def generate_population(pop_size, width, height, ascii_chars):  
    return [np.random.choice(ascii_chars, size=(height, width)) for _ in range(pop_size)]  


def compute_fitness(ascii_image, grayscale_image, ascii_lut): 
    fitness = 0                                                
    height, width = grayscale_image.shape                      
    for y in range(height):                                    
        for x in range(width):                                 
            pixel_val = grayscale_image[y, x] / 255.0         
            char_val = ascii_lut[ascii_image[y, x]]            
            fitness -= abs(pixel_val - char_val)              
    return fitness                                             


def display_ascii_image(ascii_image):                          
    return "\n".join("".join(row) for row in ascii_image)      

def tournament_selection(scored_population, tournament_size=3):  
    
    tournament = np.random.choice(len(scored_population), tournament_size, replace=False)
    best_idx = max(tournament, key=lambda i: scored_population[i][0])
    return scored_population[best_idx][1]

def crossover(parent1, parent2, crossover_rate=0.8):  
    
    if np.random.random() > crossover_rate:
        return parent1.copy(), parent2.copy()
    
    height, width = parent1.shape
    crossover_point = np.random.randint(1, height)
    
    child1 = parent1.copy()
    child2 = parent2.copy()
    
    child1[crossover_point:] = parent2[crossover_point:]
    child2[crossover_point:] = parent1[crossover_point:]
    
    return child1, child2

def mutate(individual, ascii_chars, mutation_rate=0.1):  
    
    mutated = individual.copy()
    height, width = individual.shape
    
    for y in range(height):
        for x in range(width):
            if np.random.random() < mutation_rate:
                mutated[y, x] = np.random.choice(ascii_chars)
    
    return mutated

def save_ascii_to_file(ascii_image, filename):  
    
    with open(filename, 'w') as f:
        f.write(display_ascii_image(ascii_image))
    print(f"[INFO] Imaginea ASCII a fost salvata in {filename}")


if __name__ == "__main__":                                    
    import matplotlib.pyplot as plt                            
    
    image_path = "input.png"                                  
    ascii_file_path = "ascii_chars.txt"                       

    if not os.path.exists(image_path):                        
        print("[EROARE] Imaginea nu a fost gasita!")           
        exit()                                                 

    image = load_image(image_path, size=(24, 16))            
    ascii_chars = load_ascii_characters(ascii_file_path)       
    ascii_lut = create_ascii_lut(ascii_chars)                 

    print(f"[INFO] Imaginea incarcata: {image.shape}")
    print(f"[INFO] Caractere ASCII: {''.join(ascii_chars)}")

    population_size = 100                                     
    max_generations = 150                                     
    mutation_rate = 0.05                                       
   
    population = generate_population(population_size, image.shape[1], image.shape[0], ascii_chars)
    
    best_fitness_history = []
    avg_fitness_history = []
    
    print(f"[INFO] Incepe evolutia cu {population_size} indivizi pentru {max_generations} generatii")
    
    #algoritmul genetic
    for generation in range(max_generations):

        scored_population = [(compute_fitness(indiv, image, ascii_lut), indiv) for indiv in population]
        scored_population.sort(reverse=True, key=lambda x: x[0])
        
        best_fitness = scored_population[0][0]
        avg_fitness = np.mean([score for score, _ in scored_population])
        best_fitness_history.append(best_fitness)
        avg_fitness_history.append(avg_fitness)
        
        if generation % 10 == 0:
            print(f"Generatia {generation:2d}: Best = {best_fitness:7.3f}, Avg = {avg_fitness:7.3f}")
        
        new_population = []
        
        new_population.append(scored_population[0][1].copy())
        new_population.append(scored_population[1][1].copy())
        
        while len(new_population) < population_size:
            parent1 = tournament_selection(scored_population)
            parent2 = tournament_selection(scored_population)
            
            child1, child2 = crossover(parent1, parent2)
            
            child1 = mutate(child1, ascii_chars, mutation_rate)
            child2 = mutate(child2, ascii_chars, mutation_rate)
            
            new_population.extend([child1, child2])
        
        population = new_population[:population_size]
    
    scored_population = [(compute_fitness(indiv, image, ascii_lut), indiv) for indiv in population]
    scored_population.sort(reverse=True, key=lambda x: x[0])
    
    best_individual = scored_population[0][1]
    best_fitness = scored_population[0][0]
    
    print("\n" + "="*50)
    print("REZULTATUL FINAL:")
    print("="*50)
    print(display_ascii_image(best_individual))
    print("="*50)
    print(f"Fitness final: {best_fitness:.4f}")
    
    save_ascii_to_file(best_individual, "ascii_art_output.txt")
    
    plt.figure(figsize=(10, 5))
    plt.plot(best_fitness_history, 'b-', label='Best Fitness', linewidth=2)
    plt.plot(avg_fitness_history, 'r--', label='Average Fitness', linewidth=1)
    plt.xlabel('Generatia')
    plt.ylabel('Fitness')
    plt.title('Evolutia Fitness-ului in Algoritmul Genetic')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('fitness_evolution.png', dpi=200, bbox_inches='tight')
    plt.show()
    
    print(f"\n[INFO] Graficul evolutiei salvat in 'fitness_evolution.png'")
