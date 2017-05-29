from forms.markers.marker import Marker


class VerbMarker(Marker):

    def __init__(self, form, position, person, number):
        super(VerbMarker, self).__init__(form, position)
        self._person = person
        self._number = number

    @property
    def person(self):
        return self._person

    @property
    def number(self):
        return self._number
