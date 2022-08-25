

class Vector3:
    # def __init__(self, x, y, z):
    #     self.__coordinates = [x, y, z]

    def __init__(self, coordinates):
        if len(coordinates) != 3:
            raise ValueError(f'coordinates must be of length 3. Provided {len(coordinates)}')
        self.__coordinates = coordinates

    def __add__(self, other):
        new_coords = [entry[0] + entry[1] for entry in zip(self.__coordinates, other.__coordinates)]
        return Vector3(new_coords)

    def __sub__(self, other):
        new_coords = [entry[0] - entry[1] for entry in zip(self.__coordinates, other.__coordinates)]
        return Vector3(new_coords)

    def __iadd__(self, other):
        new_coords = [entry[0] + entry[1] for entry in zip(self.__coordinates, other.__coordinates)]
        return Vector3(new_coords)

    def dot(self, vector):
        return sum(coord[0] * coord[1] for coord in zip(self.__coordinates, vector.__coordinates))

    def cross(self, vector):
        return Vector3(
            [self.__coordinates[1] * vector.__coordinates[2] - self.__coordinates[2] * vector.__coordinates[1],
            self.__coordinates[2] * vector.__coordinates[0] - self.__coordinates[0] * vector.__coordinates[2],
            self.__coordinates[0] * vector.__coordinates[1] - self.__coordinates[1] * vector.__coordinates[0]]
        )

    def magnitude(self):
        return pow(sum([coord * coord for coord in self.__coordinates]), 0.5)

    def projection(self, vect_to_project):
        return self.dot(vect_to_project)

    def num_mult(self, num):
        return Vector3([coord * num for coord in self.__coordinates])

    @classmethod
    def gram_schmidt(cls, li_vectors):
        basis = [li_vectors[0]]
        for i in range(1, len(li_vectors)):
            v = Vector3([0, 0, 0])
            for j in range(0, i):
                k = li_vectors[i].dot(basis[j]) / basis[j].dot(basis[j])
                v += basis[j].num_mult(k)
            basis.append(li_vectors[i] - v)
        return basis

    def __str__(self):
        return f'Vector3({self.__coordinates[0]},{self.__coordinates[1]},{self.__coordinates[2]})'

