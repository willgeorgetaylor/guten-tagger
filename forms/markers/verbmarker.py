from forms.markers.marker import Marker


class VerbMarker(Marker):

    def __init__(self, form, position, person, number):
        super(VerbMarker, self).__init__(form, position)
        self.person = person
        self.number = number
