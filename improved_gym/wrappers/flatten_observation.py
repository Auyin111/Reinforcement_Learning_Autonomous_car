"""Wrapper for flattening observations of an environment."""
import improved_gym
import improved_gym.spaces as spaces


class FlattenObservation(improved_gym.ObservationWrapper):
    """Observation wrapper that flattens the observation.

    Example:
        >>> import improved_gym
        >>> env = improved_gym.make('CarRacing-v1')
        >>> env.observation_space.shape
        (96, 96, 3)
        >>> env = FlattenObservation(env)
        >>> env.observation_space.shape
        (27648,)
        >>> obs = env.reset()
        >>> obs.shape
        (27648,)
    """

    def __init__(self, env: improved_gym.Env):
        """Flattens the observations of an environment.

        Args:
            env: The environment to apply the wrapper
        """
        super().__init__(env)
        self.observation_space = spaces.flatten_space(env.observation_space)

    def observation(self, observation):
        """Flattens an observation.

        Args:
            observation: The observation to flatten

        Returns:
            The flattened observation
        """
        return spaces.flatten(self.env.observation_space, observation)
