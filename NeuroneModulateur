
class NeuroneModulateur:
    def __init__(self, balance_threshold=1.0, adjustment_factor=0.5):
        """
        Initialise un neurone de modulation pour ajuster l'activité des neurones connectés.

        Parameters:
        balance_threshold (float): Niveau d'excitation cible à maintenir.
        adjustment_factor (float): Sensibilité de l'ajustement pour la modulation de l'activité.
        """
        self.balance_threshold = balance_threshold
        self.adjustment_factor = adjustment_factor
        self.output_signal = 0.0  # Signal de sortie modulé

    def receive_input(self, input_signal):
        """
        Reçoit un signal d'entrée et modifie son intensité pour atteindre le seuil d'équilibre.

        Parameters:
        input_signal (float): Signal reçu pour être ajusté.
        Returns:
        float: Signal ajusté pour réguler l'activité des neurones cibles.
        """
        # Calcule l'ajustement basé sur la déviation par rapport au seuil d'équilibre
        deviation = input_signal - self.balance_threshold
        self.output_signal = input_signal - (deviation * self.adjustment_factor)
        return self.output_signal

    def __repr__(self):
        """
        Représente le neurone de modulation pour une identification facile.
        """
        return (f"NeuroneModulateur(balance_threshold={self.balance_threshold}, "
                f"adjustment_factor={self.adjustment_factor})")

# Simulation d'un neurone modulateur pour ajuster une série de signaux
def simulate_neurone_modulateur():
    # Créer un neurone de modulation pour le test
    modulator_neuron = NeuroneModulateur(balance_threshold=1.0, adjustment_factor=0.3)

    # Simuler des signaux d'entrée avec des ajustements pour maintenir l'équilibre
    for cycle in range(5):
        input_signal = np.random.rand() * 2  # Signal d'entrée aléatoire
        adjusted_signal = modulator_neuron.receive_input(input_signal)
        print(f"Cycle {cycle}: Signal d'entrée = {input_signal:.2f}, Signal ajusté = {adjusted_signal:.2f}")

# Exécute la simulation
simulate_neurone_modulateur()
