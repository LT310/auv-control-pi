# from navio import pwm


class Motor:

    def __init__(self, channel):
        """

        Args:
            channel (int): PWM 0-13 channels are available
        """
        self._pwm_channel = channel
        self._pwm = None  # TODO use actual pwm here
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        """Must be value betweeon 0 and 100"""
        # clamp the speed between 0 and 100
        value = max(0, value)
        value = min(100, value)
        # TODO set duty cycle of pwm that maps to speed
        self._speed = value
