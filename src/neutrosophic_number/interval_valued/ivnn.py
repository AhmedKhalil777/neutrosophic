# In the Name of ALLAH

from math import sqrt

class IVNN:

    def __init__(self, id, t_lower, t_upper, i_lower, i_upper, f_lower, f_upper):

        assert 0 <= t_lower <= 1
        assert 0 <= t_upper <= 1
        assert 0 <= i_lower <= 1
        assert 0 <= i_upper <= 1
        assert 0 <= f_lower <= 1
        assert 0 <= f_upper <= 1

        assert 0 <= t_lower + i_lower + f_lower <= 3

        self._id = id
        self._t_lower = t_lower
        self._t_upper = t_upper
        self._i_lower = i_lower
        self._i_upper = i_upper
        self._f_lower = f_lower
        self._f_upper = f_upper


    def complement(self):
        # return IVNN(f'{self._id}_complement',
        # self._t_lower,
        # self._t_upper,
        # 1 - self._i_upper, 
        # 1 - self._i_upper,
        # self._f_lower, self._f_lower)
        return IVNN(f'{self._id}_complement',
        self._f_lower,
        self._f_upper,
        self._i_lower, 
        self._i_upper,
        self._t_lower,
        self._t_upper)

    def __add__(self, ivnn):
        return IVNN(f'{self._id} + {ivnn._id}',
                    self._t_lower + ivnn._t_lower - self._t_lower * ivnn._t_lower,
                    self._t_upper + ivnn._t_upper - self._t_upper * ivnn._t_upper,
                    self._i_lower * ivnn._i_lower,
                    self._i_upper * ivnn._i_upper,
                    self._f_lower * ivnn._f_lower,
                    self._f_upper * ivnn._f_upper)

    def __mul__(self, ivnn):
        return IVNN(f'P{self._id} * {ivnn._id}',
                    self._t_lower * ivnn._t_lower,
                    self._t_upper * ivnn._t_upper,
                    self._i_lower + ivnn._i_lower - self._i_lower * ivnn._i_lower,
                    self._i_upper + ivnn._i_upper - self._i_upper * ivnn._i_upper,
                    self._f_lower + ivnn._f_lower - self._f_lower * ivnn._f_lower,
                    self._f_upper + ivnn._f_upper - self._f_upper * ivnn._f_upper)

    def multiply_by(self, alpha):
        return IVNN(f'{alpha} * {self._id}',
                    1 - pow((1 - self._t_lower),alpha),
                    1 - pow((1 - self._t_upper),alpha),
                    pow(self._i_lower, alpha),
                    pow(self._i_upper, alpha),
                    pow(self._f_lower, alpha),
                    pow(self._i_upper, alpha))

    def divide(self, ivnn):
        raise NotImplementedError

    def __sub__(self, ivnn):
        return ivnn(f'{self._id} - {ivnn._id}',
                    self._t_lower - ivnn._t_upper,
                    self._t_upper - ivnn._t_lower,
                    max(self._i_lower, ivnn._i_lower),
                    max(self._i_upper, ivnn._i_upper),
                    self._f_lower - ivnn._f_upper,
                    self._f_upper - ivnn._f_lower)

    def deneutrosophy(self):
        return (self._t_lower + self._t_upper + (1 - self._f_lower) + (1 - self._t_upper) + self._t_lower * self._t_upper - sqrt((1 - self._f_lower) * (1 - self._f_upper))) / 4 * ((1 - ((self._i_lower + self._i_upper)/2))-(sqrt(self._i_lower * self._i_upper)))


