# In the Name of ALLAH

class SingleValuedNeutrosophicNumber:

    def __init__(self, id, truth, indeterminacy, falsehood):
        """Initialize neutrosophic element
        :truth:
        :indeterminacy:
        :falsehood:"""
        assert id is not None, 'provide id for element to be initialized'
        assert 0 <= truth <= 1, 'invalid truth value'
        assert 0 <= indeterminacy <= 1, 'invalid indeterminacy value'
        assert 0 <= falsehood <= 1, 'invalid falsihood value'
        assert 0 <= truth + falsehood + indeterminacy <= 3, 'invalid combined sum values'
        self._id = id
        self._truth = truth
        self._indeterminacy = indeterminacy
        self._falsehood = falsehood

    def __str__(self):
        return f'ID: {self._id} - Truth: {self._truth} - Indeterminacy: {self._indeterminacy} - Falsehood: {self._falsehood}'

    def __repr__(self):
        return f'ID: {self._id} - Truth: {self._truth} - Indeterminacy: {self._indeterminacy} - Falsehood: {self._falsehood}'

    def complement(self):
        """based on the formula: (z 1 ) c = <V 1 , 1 − U 1 , T 1 >
        :return: svnn object with the new values
        """
        return SingleValuedNeutrosophicNumber \
            (f'{self._id}_complement', self._falsehood,
             1 - self._indeterminacy, self._truth)

    def is_subset_of(self, svnn):
        """Check if number is a subset of another svnn
        :param svnn: Single Value Neutrosohpic Number to compare with
        :return: True or False
        """
        if self._truth <= svnn._truth and self._indeterminacy >= \
                svnn._indeterminacy and self._falsehood >= svnn._falsehood:
            return True
        return False

    def __eq__(self, svnn):
        if self.is_subset_of(svnn) and svnn.is_subset_of(self):
            return True
        return False

    def __add__(self, svnn):
        return svnn(f'{self._id} + {svnn._id}',
                    (self._truth + svnn._truth) - (self._truth * svnn._truth),
                    self._indeterminacy * svnn._indeterminacy,
                    self._falsehood * svnn._falsehood)

    def __mul__(self, svnn):
        return svnn(f'{self._id} * {svnn._id}',
                    self._truth * svnn._truth,
                    svnn._indeterminacy - (self._indeterminacy * svnn._indeterminacy),
                    (self._falsehood + svnn._falsehood) - (self._falsehood * svnn._falsehood))

    def multiply_by_alpha(self, alpha):
        assert alpha > 0, 'Alpha must be larger than zero'
        return svnn(f'{self._id}_multiplied_by_{alpha}',
                    1 - pow(1 - self._truth), alpha,
                    pow(self._indeterminacy, alpha),
                    pow(self._falsehood, alpha))

    # def __pow__(self, power, modulo=None):
    def power(self, alpha):
        """Contact the paper author to ask about it
        """
        assert alpha > 0, 'Alpha must be larger than zero'
        raise NotImplementedError

    def score(self):
        return ( 2 + self._truth - self._indeterminacy - self._falsehood ) / 3

    def accuracy(self):
        return self._truth - self._falsehood

    def ranking_compared_to(self, svnn):
        """
        :param svnn:
        :return: -1 -> Not Applicable, 0 -> equal ranking, 1 -> higher ranking
        """
        if self.score() > svnn.score():
            return 1
        if self.score() == svnn.score() and self.accuracy() > svnn.accuracy():
            return 1
        if self.score() == svnn.score() and self.accuracy() == svnn.accuracy():
            return 0
        return -1

    def deneutrosophy(self):
        from math import sqrt, pow
        return 1 - (sqrt (((pow(1 - self._truth),2) + pow(self._indeterminacy,2) + pow(self._falsehood,2)) / 3))
