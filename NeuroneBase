
import numpy as np

class NeuroneBase:
    def __init__(self, v_rest=-65, v_threshold=-55, g_na=120, g_k=36, g_leak=0.3, e_na=50, e_k=-77, e_leak=-54.4):
        """
        Initialise un modèle de Hodgkin-Huxley pour servir de base à tous les neurones.

        Parameters:
        v_rest (float): Potentiel de repos.
        v_threshold (float): Seuil d'activation du neurone.
        g_na (float): Conductance maximale pour le sodium.
        g_k (float): Conductance maximale pour le potassium.
        g_leak (float): Conductance de fuite.
        e_na (float): Potentiel d'équilibre du sodium.
        e_k (float): Potentiel d'équilibre du potassium.
        e_leak (float): Potentiel d'équilibre de fuite.
        """
        self.v_rest = v_rest
        self.v_threshold = v_threshold
        self.v_membrane = v_rest  # Potentiel de membrane initial
        self.g_na = g_na
        self.g_k = g_k
        self.g_leak = g_leak
        self.e_na = e_na
        self.e_k = e_k
        self.e_leak = e_leak

    def compute_dynamics(self, i_ext, dt=0.01):
        """
        Calcule la dynamique du neurone pour une durée définie.

        Parameters:
        i_ext (float): Courant externe appliqué.
        dt (float): Pas de temps pour la simulation.
        Returns:
        float: Potentiel de membrane mis à jour.
        """
        # Calcul des courants ioniques (simplification)
        i_na = self.g_na * (self.v_membrane - self.e_na)
        i_k = self.g_k * (self.v_membrane - self.e_k)
        i_leak = self.g_leak * (self.v_membrane - self.e_leak)

        # Équation de mise à jour du potentiel de membrane
        dv_dt = (i_ext - (i_na + i_k + i_leak)) * dt
        self.v_membrane += dv_dt

        return self.v_membrane

    def activate(self, i_ext):
        """
        Vérifie si le potentiel de membrane atteint le seuil et simule l'activation.

        Parameters:
        i_ext (float): Courant externe appliqué.
        Returns:
        bool: True si le neurone est activé, False sinon.
        """
        self.compute_dynamics(i_ext)
        if self.v_membrane >= self.v_threshold:
            # Réinitialisation après un potentiel d'action (repolarisation)
            self.v_membrane = self.v_rest
            return True
        return False

    def __repr__(self):
        """
        Représente le neurone de base avec le modèle de Hodgkin-Huxley.
        """
        return (f"NeuroneBase(v_rest={self.v_rest}, v_threshold={self.v_threshold}, "
                f"g_na={self.g_na}, g_k={self.g_k}, g_leak={self.g_leak})")
