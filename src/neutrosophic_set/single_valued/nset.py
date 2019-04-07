# In the Name of ALLAH

from element import Element

class NSet:

    def __init__(self):
        """Inner data structure to hold the elements will be Dictionary
        with key as item ID
        and value is object of type element"""
        self._items = {}

        # used for iterable
        self.__idx = -1

    def add_element(self, element):
        self._items[element._id] = element

    def delete_element(self, element_id):
        """delete element and returns value only"""
        self._items.pop(element_id)

    def get_element_by_id(self, element_id):
        """:rtype: element object
        """
        return self._items[element_id]

    def get_all_elements(self):
        return self._items

    def is_empty(self):
        if len(self) == 0:
            return True

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        self.__idx += 1
        self.__keys = list(self._items)
        try:
            # returns key and value (that is the object)
            return self.__keys[self.__idx], self._items[self.__keys[self.__idx]]
        except IndexError:
            self.__idx = 0
            raise StopIteration

    # def __eq__(self, nset):
    #     if self._items == nset._items: return True
    #     return False

    def __str__(self):
        output = '==== Start of Set Elements ==\n'
        #output = f'Neutrosophic Set Memory Address: {id(self)} \n'
        for item_id in self._items:
            output += str(self._items[item_id])
            output += '\n'
        output += '==== End of Set Elements ===='
        return output

    def contains(self, item):
        if self._items.keys:
            return True
        else:
            return False

    def subset_of(self, nset):
        """
        Condition-01: compare number of elements in each nset
        Condition-02: compare elements' keys
        Condition-03: compare elements' values
        """
        # Condition-01
        if len(self) > len(nset):
            return False

        # Condition-02: for key, item in nset:
        for item in self._items:
            if item not in nset._items:
                return False

        # Condition-03
        for item_key in self._items:
            remote_element = nset.get_element_by_id(item_key)
            local_element = self.get_element_by_id(item_key)
            if local_element._truth > remote_element._truth \
                    or local_element._indeterminacy < remote_element._indeterminacy \
                    or local_element._falsehood > remote_element._falsehood:
                return False
        return True

    def __eq__(self, nset):
        """
        Condition-01: compare number of elements in each nset
        Condition-02: compare elements' keys
        Condition-03: compare elements' values
        """
        # Condition-01
        if len(self) != len(nset):
            return False

        # Condition-02: equality requires bi-directional check:
        remote_elements = nset.get_all_elements()
        for item in self._items:
            if item not in remote_elements:
                return False
        for item in remote_elements:
            if item not in self._items:
                return False

        # Condition-03
        for item_key in self._items:
            remote_element = remote_elements[item_key]
            local_element = self.get_element_by_id(item_key)
            if local_element._truth == remote_element._truth \
                    and local_element._indeterminacy == remote_element._indeterminacy \
                    and local_element._falsehood == remote_element._falsehood:
                return True
        return False

    def intersect(self, nset):
        result = {}
        remote_elements = nset.get_all_elements()
        # if an item doesn't exist locally, I don't care about its intersection
        for item_key in self._items:
            try:
                local_element = self.get_element_by_id(item_key)
                remote_element = remote_elements[item_key]
                _truth = min(local_element._truth, remote_element._truth)
                _indeterminacy = max(local_element._indeterminacy, remote_element._indeterminacy)
                _falsehood = max(local_element._falsehood, remote_element._falsehood)
                result[item_key] = Element(item_key, _truth, _indeterminacy, _falsehood)
            except:
                pass
        return result

    def union(self, nset):
        result = {}
        remote_elements = nset.get_all_elements()
        # if an item doesn't exist locally, I don't care about its intersection
        for item_key in self._items:
            try:
                local_element = self.get_element_by_id(item_key)
                remote_element = remote_elements[item_key]
                _truth = max(local_element._truth, remote_element._truth)
                _indeterminacy = min(local_element._indeterminacy, remote_element._indeterminacy)
                _falsehood = max(local_element._falsehood, remote_element._falsehood)
                result[item_key] = Element(item_key, _truth, _indeterminacy, _falsehood)
            except:
                pass
        return result




