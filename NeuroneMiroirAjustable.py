
class NeuroneMiroirAjustable(NeuroneBase):
    def __init__(self, threshold=1.0, imitation_sensitivity=0.5, activation_type='self', **kwargs):
        """
        Initialise un neurone en miroir ajustable pour imiter et réagir à des actions observées.

        Parameters:
        threshold (float): Seuil d'activation du neurone miroir.
        imitation_sensitivity (float): Sensibilité de l'imitation (pour les actions observées).
        activation_type (str): Type d'activation ('self' pour action propre, 'observed' pour actions observées).
        """
        super().__init__(**kwargs)
        self.threshold = threshold
        self.imitation_sensitivity = imitation_sensitivity
        self.activation_type = activation_type
        self.observed_signal = 0.0  # Signal observé pour l'imitation

    def receive_input(self, input_signal, observed=False):
        """
        Reçoit un signal d'entrée et l'ajuste en fonction de l'activation en miroir.

        Parameters:
        input_signal (float): Signal reçu d'une action propre ou observée.
        observed (bool): Si True, traite le signal comme une action observée.
        """
        if observed and self.activation_type == 'observed':
            # Sensibilité pour une action observée
            self.observed_signal = input_signal * self.imitation_sensitivity
        else:
            # Utilisation de Hodgkin-Huxley pour les actions propres
            super().compute_dynamics(input_signal)

    def activate(self):
        """
        Active le neurone miroir si le potentiel de membrane dépasse le seuil.

        Returns:
        bool: True si activé, False sinon.
        """
        # Si le neurone atteint le seuil ou imite l'observation
        if self.v_membrane >= self.threshold or self.observed_signal >= self.threshold:
            # Réinitialisation après un potentiel d'action ou une imitation
            self.v_membrane = self.v_rest
            return True
        return False

    def __repr__(self):
        """
        Représente le neurone en miroir ajustable pour une identification facile.
        """
        return (f"NeuroneMiroirAjustable(threshold={self.threshold}, "
                f"imitation_sensitivity={self.imitation_sensitivity}, "
                f"activation_type={self.activation_type})")
