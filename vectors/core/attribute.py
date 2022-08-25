from OpenGL.GL import *
import numpy as np


class Attribute(object):
    def __init__(self, dataType, data):
        # type of elements in data array
        self.data_type = dataType

        # array of data to be stored in buffer
        self.data = data

        # reference of available buffer from GPU
        self.bufferRef = glGenBuffers(1)

        # upload data immediately
        self.upload_data()

    def upload_data(self):
        # convert data to numpy array format
        # convert numbers to 32-bit floats
        data = np.array(self.data).astype(np.float32)

        # select buffer used by the following function
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    # associate variable in program with this buffer
    def associate_variable(self, program_ref, variable_name):
        # get reference for program variable with given name
        variable_ref = glGetAttribLocation(program_ref, variable_name)

        # if the program does not reference the variable, then exit
        if variable_ref == -1:
            return

        # select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # specify how data will be read
        # from the currently bound buffer into specified variable
        if self.data_type == 'int':
            glVertexAttribPointer(variable_ref, 1, GL_INT, False, 0, None)
        elif self.data_type == 'vec2':
            glVertexAttribPointer(variable_ref, 2, GL_FLOAT, False, 0, None)
        elif self.data_type == 'vec3':
            glVertexAttribPointer(variable_ref, 3, GL_FLOAT, False, 0, None)
        elif self.data_type == 'vec4':
            glVertexAttribPointer(variable_ref, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception('Attribute ' + variable_name + ' has unknown type ' + self.data_type)

        # indicate that data will be streamed to this variable
        glEnableVertexAttribArray(variable_ref)
