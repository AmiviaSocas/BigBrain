
class SystemeFeedback:
    def __init__(self, reinforcement_sensitivity=0.5, decay_factor=0.1, max_strength=2.0):
        """
        Initialise un système de feedback pour ajuster les connexions en fonction de l'activation.

        Parameters:
        reinforcement_sensitivity (float): Intensité du renforcement en fonction de l'activation répétée.
        decay_factor (float): Facteur d'oubli, réduisant progressivement la force de la connexion.
        max_strength (float): Force maximale de la connexion après renforcement.
        """
        self.reinforcement_sensitivity = reinforcement_sensitivity
        self.decay_factor = decay_factor
        self.connection_strength = 1.0  # Force de connexion initiale
        self.max_strength = max_strength

    def apply_feedback(self, is_activated):
        """
        Applique un feedback en fonction de l'activation du neurone.

        Parameters:
        is_activated (bool): Indique si le neurone est activé (True) ou non (False).
        Returns:
        float: Nouvelle force de connexion après application du feedback.
        """
        if is_activated:
            # Renforcement de la connexion en cas d'activation
            self.connection_strength += self.reinforcement_sensitivity
            # Limite la force de connexion à la valeur maximale
            if self.connection_strength > self.max_strength:
                self.connection_strength = self.max_strength
        else:
            # Décroît la connexion progressivement en l'absence d'activation
            self.connection_strength *= (1 - self.decay_factor)
        
        return self.connection_strength

    def __repr__(self):
        """
        Représente le système de feedback pour une identification facile.
        """
        return (f"SystemeFeedback(reinforcement_sensitivity={self.reinforcement_sensitivity}, "
                f"decay_factor={self.decay_factor}, max_strength={self.max_strength})")


# Simulation d'un système de feedback avec une série d'activations
def simulate_feedback_system():
    # Créer un système de feedback pour le test
    feedback_system = SystemeFeedback(reinforcement_sensitivity=0.3, decay_factor=0.1, max_strength=1.5)

    # Simuler une série d'activation/désactivation pour observer le renforcement
    for cycle in range(10):
        # Génère aléatoirement une activation (True/False)
        is_activated = np.random.choice([True, False])
        new_strength = feedback_system.apply_feedback(is_activated)
        print(f"Cycle {cycle}: Activation = {is_activated}, Force de connexion = {new_strength:.2f}")

# Exécute la simulation
simulate_feedback_system()
