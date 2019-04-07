# In the Name of ALLAH

from ivnn import IVNN

class IVNNSet:

    def __init__(self):
        self._ivnns = []

    def add_ivnn(self, ivnn):
        self._ivnns.append(ivnn)

    def weighted_average(self, weights):
        """Interval Neutrosophic Number Weighted Average Operator
        (INNWA) defined by Zhang et al.
        :return: IVNN
        """
        weights_sum = 0
        for weight in weights:
            assert 0 <= weight <= 1
            weights_sum += weight
        assert weights_sum == 1

        t_lower_dot_product = 1.0
        t_upper_dot_product = 1.0
        i_lower_dot_product = 1.0
        i_upper_dot_product = 1.0
        f_lower_dot_product = 1.0
        f_upper_dot_product = 1.0

        for ivnn, weight in zip(self._ivnns, weights):
            t_lower_dot_product *= pow(1 - ivnn._t_lower, weight)
            t_upper_dot_product *= pow(1 - ivnn._t_upper, weight)
            i_lower_dot_product *= pow(ivnn._i_lower, weight)
            i_upper_dot_product *= pow(ivnn._i_upper, weight)
            f_lower_dot_product *= pow(ivnn._f_lower, weight)
            f_upper_dot_product *= pow(ivnn._i_upper, weight)

        return IVNN(1 - t_lower_dot_product, 1 - t_upper_dot_product,
                    i_lower_dot_product, i_upper_dot_product,
                    f_lower_dot_product, f_upper_dot_product)

