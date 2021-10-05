from week_7.vector import Vector


class Matrix:
    """
    A class used to represent a matrix.
    :attribute vectors: a list of element of type Vector.
    """

    def __init__(self, vectors):
        """
        Constructor for Matrix class.
        :param vectors: a list of Vectors
        """
        self.vectors = vectors

    def __repr__(self):
        """
        print function override
        """
        m = ""
        for vec in self:
            m = m + str(vec) + "\n"
        return m.strip()

    def __add__(self, other):
        """
        addition operator overload
        :param other: a Matrix to be added to self
        """
        return Matrix(
            [self[i] + other[i] for i in range(len(self))]
        )

    def __len__(self):
        """
        len function override
        """
        return len(self.vectors)

    def __getitem__(self, i):
        """
        indexing operator overload
        :param i: index
        """
        return self.vectors[i]

    def transpose(self):
        """
        a method that return the transposed matrix of self
        """
        vecs_lst = []
        for j in range(len(self[0])):  # iterate over columns
            vec_lst = []
            for i in range(len(self)):  # iterate over rows
                vec_lst.append(self[i][j])
            vecs_lst.append(Vector(vec_lst))
        return Matrix(vecs_lst)


vec1 = Vector([1, 2, 3])
vec2 = Vector([4, 5, 6])
mx = Matrix([vec1, vec2])
print(mx)
print("transpose")
print(mx.transpose())
