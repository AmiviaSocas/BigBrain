
class NeuroneMnesique(NeuroneBase):
    def __init__(self, memory_factor=0.8, retention_time=5, **kwargs):
        """
        Initialise un neurone mnésique pour stocker l'activation dans le temps.

        Parameters:
        memory_factor (float): Facteur de mémorisation influençant la rétention d'activation.
        retention_time (int): Durée pendant laquelle l'activation est retenue.
        """
        super().__init__(**kwargs)
        self.memory_factor = memory_factor
        self.retention_time = retention_time
        self.activation_history = []  # Historique d'activation pour simuler la mémoire

    def receive_input(self, input_signal):
        """
        Reçoit un signal d'entrée et met à jour le potentiel de membrane tout en ajoutant la mémoire.

        Parameters:
        input_signal (float): Signal reçu pour stimuler le neurone.
        """
        # Utilisation du modèle de Hodgkin-Huxley pour mettre à jour la membrane
        current_potential = super().compute_dynamics(input_signal)

        # Ajouter l'activation à l'historique pour la mémoire
        self.activation_history.append(current_potential)
        if len(self.activation_history) > self.retention_time:
            self.activation_history.pop(0)

        # Calcul de la rétention via le facteur de mémoire
        memory_effect = sum(self.activation_history) * self.memory_factor
        self.v_membrane += memory_effect  # Ajout de l'effet de mémoire

    def activate(self):
        """
        Active le neurone en utilisant le modèle de Hodgkin-Huxley, avec mémoire.

        Returns:
        bool: True si activé, False sinon.
        """
        # Vérifie si le seuil d'activation est atteint, en prenant en compte la mémoire
        return super().activate(self.v_membrane)

    def __repr__(self):
        """
        Représente le neurone mnésique pour une identification facile.
        """
        return (f"NeuroneMnesique(memory_factor={self.memory_factor}, "
                f"retention_time={self.retention_time}, "
                f"v_membrane={self.v_membrane})")
