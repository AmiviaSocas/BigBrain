
class NeuroneRenforcementPositif:
    def __init__(self, threshold=1.0, dopamine_sensitivity=0.5, retention_factor=0.9):
        """
        Initialise un neurone de renforcement positif sensible à la dopamine.

        Parameters:
        threshold (float): Seuil d'activation du neurone.
        dopamine_sensitivity (float): Sensibilité à la dopamine, influençant l'activation.
        retention_factor (float): Facteur de rétention, permettant de garder l'excitation plus longtemps.
        """
        self.threshold = threshold
        self.membrane_potential = 0.0  # Potentiel de membrane initial
        self.dopamine_sensitivity = dopamine_sensitivity
        self.retention_factor = retention_factor
        self.amplification = 1.0  # Facteur d'amplification basé sur la dopamine

    def receive_input(self, input_signal, dopamine_level=0.0):
        """
        Reçoit un signal d'entrée et met à jour le potentiel de membrane.
        
        Parameters:
        input_signal (float): Signal reçu d'un autre neurone ou d'un stimulus.
        dopamine_level (float): Niveau de dopamine, influençant le renforcement.
        """
        # Amplification en fonction de la dopamine reçue
        self.amplification += dopamine_level * self.dopamine_sensitivity
        self.membrane_potential += input_signal * self.amplification

    def activate(self):
        """
        Active le neurone si le seuil est atteint, puis applique le facteur de rétention.

        Returns:
        float: Signal d'activation, 1.0 si activé, 0.0 sinon.
        """
        if self.membrane_potential >= self.threshold:
            self.membrane_potential *= self.retention_factor  # Rétention de l'excitation
            return 1.0  # Activation positive
        else:
            return 0.0  # Pas d'activation

    def __repr__(self):
        """
        Représente le neurone de renforcement positif pour une identification facile.
        """
        return (f"NeuroneRenforcementPositif(threshold={self.threshold}, "
                f"dopamine_sensitivity={self.dopamine_sensitivity}, "
                f"retention_factor={self.retention_factor})")


# Simulation d'un neurone de renforcement positif avec des niveaux de dopamine variables
def simulate_neurone_renforcement_positif():
    # Créer un neurone de renforcement positif pour le test
    positive_neuron = NeuroneRenforcementPositif(threshold=1.0, dopamine_sensitivity=0.5, retention_factor=0.9)

    # Simuler des cycles d'activation avec un niveau de dopamine variable
    for cycle in range(5):
        input_signal = np.random.rand() * 1.5  # Signal d'entrée aléatoire
        dopamine_level = np.random.rand()  # Niveau de dopamine aléatoire
        positive_neuron.receive_input(input_signal, dopamine_level=dopamine_level)
        activation = positive_neuron.activate()
        print(f"Cycle {cycle}: Signal d'entrée = {input_signal:.2f}, Dopamine = {dopamine_level:.2f}, Activation = {activation}")

# Exécute la simulation
simulate_neurone_renforcement_positif()
