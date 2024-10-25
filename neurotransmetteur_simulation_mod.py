class NeuroneBase:
    def __init__(self, potential=0.0):
        self.potential = potential  # Potentiel de membrane initial

    def apply_neurotransmitter(self, neurotransmitter, strength):
        """
        Applique l'effet d'un neurotransmetteur avec une intensité donnée.
       
        Parameters:
        neurotransmitter (function): Fonction neurotransmetteur à appliquer.
        strength (float): Intensité du signal de neurotransmetteur.
        """
        effect = neurotransmitter(strength)
        self.potential += effect
        return self.potential

# Fonctions des neurotransmetteurs

def glutamate(strength):
    """Excitateur : Augmente le potentiel de membrane"""
    return strength

def gaba(strength):
    """Inhibiteur : Diminue le potentiel de membrane"""
    return -strength

def dopamine(strength):
    """Modulateur : Excitateur léger"""
    return strength * 0.5

def serotonine(strength):
    """Modulateur léger : Augmente légèrement le potentiel"""
    return strength * 0.3

def acetylcholine(strength):
    """Excitateur : Facilite l'attention et la mémoire"""
    return strength * 1.2

def noradrenaline(strength):
    """Modulateur : Augmente la vigilance"""
    return strength * 0.8

def endorphines(strength):
    """Inhibiteur : Réduction de la douleur"""
    return -strength * 0.5

def glutamine(strength):
    """Précurseur : Pas d'effet direct"""
    return 0.0

# Simulation d'application de neurotransmetteurs sur divers types de neurones
def simulate_with_neurons(neurons, neurotransmitter_name, strength=1.0):
    """
    Simule l'application d'un neurotransmetteur spécifique sur une liste de neurones.
   
    Parameters:
    neurons (list): Liste de neurones où chaque neurone est une instance de classe dérivée de NeuroneBase.
    neurotransmitter_name (str): Nom du neurotransmetteur à appliquer.
    strength (float): Intensité du neurotransmetteur.
    """
    neurotransmitters = {
        'glutamate': glutamate,
        'gaba': gaba,
        'dopamine': dopamine,
        'serotonine': serotonine,
        'acetylcholine': acetylcholine,
        'noradrenaline': noradrenaline,
        'endorphines': endorphines,
        'glutamine': glutamine
    }
   
    neurotransmitter = neurotransmitters.get(neurotransmitter_name)
    if neurotransmitter:
        for i, neuron in enumerate(neurons):
            new_potential = neuron.apply_neurotransmitter(neurotransmitter, strength)
            print(f"Neurone {i + 1} potentiel après {neurotransmitter_name}: {new_potential:.2f}")
    else:
        print(f"Neurotransmetteur '{neurotransmitter_name}' non trouvé.")

# Exemple de simulation
if __name__ == "__main__":
    # Exemples de neurones basiques ou dérivés
    class NeuroneSensoriel(NeuroneBase): pass
    class NeuroneMoteur(NeuroneBase): pass
   
    # Créer quelques neurones pour la simulation
    neurons = [NeuroneSensoriel(), NeuroneMoteur()]
   
    # Appliquer un neurotransmetteur sur les neurones
    simulate_with_neurons(neurons, 'glutamate', strength=1.0)
