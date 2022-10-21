class Cow:
    def __init__(self, name: str):  # Initializes the Cow constructor
        self.__name = name
        self._image = []

    def get_name(self):  # Returns the name of the Cow object
        return self.__name

    def get_image(self):  # Returns the image of the Cow object
        return self._image

    def set_image(self, _image: str):  # Changes the image of the Cow object to a specified image
        self._image = _image
