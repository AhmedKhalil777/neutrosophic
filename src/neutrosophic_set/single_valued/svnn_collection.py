# In the Name of ALLAH

from svnn import SingleValuedNeutrosophicNumber

class SVNNCollection:
    """This class has association relationship with SVNN - Remember to add that to UML
    """

    def __init__(self):
        self._items = []
        self.__idx = -1

    def add_svnn(self, svnn):
        self._items.append(svnn)

    def delete_svnn(self, svnn):
        #TODO: Notify user about Exception handling
        self._items.remove(svnn)

    def get_all_svnns(self):
        return self._items

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        if len(self) == 0:
            return True
        return False


    def __iter__(self):
        return self

    def __next__(self):
        self.__idx += 1
        try:
            return self._items[self.__idx]
        except IndexError:
            self.__idx = 0
            raise StopIteration

    def __getitem__(self, id):
        try:
            return self._items[id]
        except IndexError:
            raise StopIteration

    def weighted_arithmetic_average(self, weights):
        """
        single-valued neutrosophic number weighted arithmetic average (SVNNWAA)
        weights: List of weights of each item - list length must be equal to the length of the items
        For more information: Google weighted arithmetic average
        or watch https://www.youtube.com/watch?reload=9&v=IuuBU6fwtNo
        :return: Three values: T, U, V
        """
        assert len(weights) == len(self._items), 'Weights List Length Does Not Match Collection SVNN Items'
        weights_sum = 0.0
        for weight in weights:
            weights_sum += weight
        assert weights_sum == 1, 'Weight\'s sum does not equal 1'
        truth_total = 1.0
        indetermenacy_total = 1.0
        falsehood_total = 1.0
        for item, weight in zip(self._items, weights):
            truth_total         *= pow(1 - item._truth, weight)
            indetermenacy_total *= pow(item._indeterminacy, weight)
            falsehood_total     *= pow(item._falsehood, weight)
        return 1 - truth_total, indetermenacy_total, falsehood_total


    def weighted_geometric_average(self, weights):
        """single-valued neutrosophic number weighted geometric average
        """
        weights_sum = 0.0
        for weight in weights:
            weights_sum += weight
        assert weights_sum == 1, 'Weight\'s sum does not equal 1'
        truth_total = 1.0
        indetermenacy_total = 1.0
        falsehood_total = 1.0
        weights.sort()
        for item, weight in zip(self._items, weights):
            truth_total         *= pow(item._truth, weight)
            indetermenacy_total *= pow(1 - item._indeterminacy, weight)
            falsehood_total     *= pow(1 - item._falsehood, weight)
        return truth_total, 1 - indetermenacy_total, 1 - falsehood_total


    def ordered_weighted_arithmetic_average(self, weights, ordered_by_position = False):
        assert len(weights) == len(self._items), 'Weights List Length Does Not Match Collection SVNN Items'
        weights_sum = 0.0
        for weight in weights:
            weights_sum += weight
        assert weights_sum == 1, 'Weight\'s sum does not equal 1'
        truth_total = 1.0
        indetermenacy_total = 1.0
        falsehood_total = 1.0
        for item, weight in zip(self._items, weights):
            truth_total         *= pow(1 - item._truth, weight)
            indetermenacy_total *= pow(item._indeterminacy, weight)
            falsehood_total     *= pow(item._falsehood, weight)
        return 1 - truth_total, indetermenacy_total, falsehood_total


    def ordered_weighted_geometric_average(self, weights):
        """single-valued neutrosophic number weighted geometric average
        """
        weights_sum = 0.0
        for weight in weights:
            weights_sum += weight
        assert weights_sum == 1, 'Weight\'s sum does not equal 1'
        truth_total = 1.0
        indetermenacy_total = 1.0
        falsehood_total = 1.0
        # The following line is the only difference
        weights.sort()
        for item, weight in zip(self._items, weights):
            truth_total         *= pow(item._truth, weight)
            indetermenacy_total *= pow(1 - item._indeterminacy, weight)
            falsehood_total     *= pow(1 - item._falsehood, weight)
        return truth_total, 1 - indetermenacy_total, 1 - falsehood_total
