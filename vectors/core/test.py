import math
import random

import numpy as np

from core.attribute import Attribute
from core.base import Base
from core.matrix import Matrix
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

from core.uniform import Uniform


class Test(Base):
    def initialize(self):
        print('Initializing program...')

    def update(self):
        pass


class Test2(Base):

    def initialize(self):
        print('Initializing program...')

        ### Initialize program ###

        # vertex shader code
        vs_code = """
        void main()
        {
            gl_Position = vec4(0.5, 0.0, 0.0, 1.0);
        }
        """

        # fragment shader code
        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 0.5, 0.0, 1.0);
        }
        """

        # send code to GPU and compile; store program reference
        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### set up vertex array object ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # set point width and height
        glPointSize(300)

    def update(self):
        # select program to use when rendering
        glUseProgram(self.program_ref)

        # renders geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)


class Test3(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###

        vs_code = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glLineWidth(4)

        ### set up vertex array object ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        ### set up vertex attribute ###
        position_data = [
            [0.8, 0.0, 0.0],
            [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],
            [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [0.4, -0.6, 0.0]
        ]

        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)


class Test4(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fs_code = """
            out vec4 fragColor;
            void main() 
            {
                fragColor = vec4(1.0, 1.0, 0.0, 1.0);
            }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glLineWidth(4)

        ### set up vao - triangle ###
        self.vao_triangle = glGenVertexArrays(1)
        glBindVertexArray(self.vao_triangle)
        position_data_triangle = [
            [-0.5, 0.8, 0.0],
            [-0.2, 0.2, 0.0],
            [-0.8, 0.2, 0.0],
        ]
        self.vertex_count_triangle = len(position_data_triangle)
        position_attribute_triangle = Attribute('vec3', position_data_triangle)
        position_attribute_triangle.associate_variable(self.program_ref, 'position')

        ### set up vao - square ###
        self.vao_square = glGenVertexArrays(1)
        glBindVertexArray(self.vao_square)
        position_data_square = [
            [0.8, 0.8, 0.0],
            [0.8, 0.2, 0.0],
            [0.2, 0.2, 0.0],
            [0.2, 0.8, 0.0],
        ]
        self.vertex_count_square = len(position_data_square)
        position_attribute_square = Attribute('vec3', position_data_square)
        position_attribute_square.associate_variable(self.program_ref, 'position')

    def update(self):
        # using the same program to draw both shapes
        glUseProgram(self.program_ref)

        # draw triangle
        glBindVertexArray(self.vao_triangle)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_triangle)

        # draw square
        glBindVertexArray(self.vao_square)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_square)


class Test5(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
                in vec3 position;
                in vec3 vertexColor;
                out vec3 color;
                void main()
                {
                    gl_Position = vec4(position.x, position.y, position.z, 1.0);
                    color = vertexColor;
                }
                """

        fs_code = """
                    in vec3 color;
                    out vec4 fragColor;
                    void main() 
                    {
                        fragColor = vec4(color.r, color.g, color.b, 1.0);
                    }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        glPointSize(10)
        glLineWidth(4)

        ### set up vao ###
        self.vao_position = glGenVertexArrays(1)
        glBindVertexArray(self.vao_position)
        position_data = [
            [0.8, 0.0, 0.0],
            [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],
            [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [0.4, -0.6, 0.0],
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        color_data = [
            [1.0, 0.0, 0.0],
            [1.0, 0.5, 0.0],
            [1.0, 1.0, 0.0],
            [0.5, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.5, 0.0, 1.0],
        ]
        color_attribute = Attribute('vec3', color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)


class Test6(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
                in vec3 position;
                in vec3 vertexColor;
                out vec3 color;
                void main()
                {
                    gl_Position = vec4(position.x, position.y, position.z, 1.0);
                    color = vertexColor;
                }
                """

        fs_code = """
                    in vec3 color;
                    out vec4 fragColor;
                    void main() 
                    {
                        fragColor = vec4(color.r, color.g, color.b, 1.0);
                    }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        glPointSize(10)
        glLineWidth(4)

        def get_circle_points():
            res = []
            for x in np.linspace(-0.5, 0.5, 10000):
                res.append([x, math.sqrt(0.25 - pow(x, 2)), 0.0])
                res.append([x, -math.sqrt(0.25 - pow(x, 2)), 0.0])
            return res



        ### set up vao ###
        self.vao_position = glGenVertexArrays(1)
        glBindVertexArray(self.vao_position)
        position_data = get_circle_points()
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        color_data = np.full((len(position_data), 3), [random.uniform(0, 1),  1.0, random.uniform(0, 1)])
        color_attribute = Attribute('vec3', color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)


class Test7(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
                in vec3 position;
                in vec3 vertexColor;
                out vec3 color;
                void main()
                {
                    gl_Position = vec4(position.x, position.y, position.z, 1.0);
                    color = vertexColor;
                }
                """

        fs_code = """
                    in vec3 color;
                    out vec4 fragColor;
                    void main() 
                    {
                        fragColor = vec4(color.r, color.g, color.b, 1.0);
                    }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        glPointSize(10)
        glLineWidth(4)

        def get_points():
            res = [[0.0, 0.0, 0.0]]
            for x in np.linspace(0.001, 1, 100):
                res.append(
                    [
                        x,
                        -(x * math.log(x) - 0.05 * math.exp(-pow(30 * x - 12, 6))),
                        0.0
                    ]
                )
            return res

        ### set up vao ###
        self.vao_position = glGenVertexArrays(1)
        glBindVertexArray(self.vao_position)
        position_data = np.array(get_points())
        rotation = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        position_data = np.array(list(map(lambda v: rotation @ v, position_data)))
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        color_data = np.full((len(position_data), 3), [1.0, 1.0, 1.0])
        color_attribute = Attribute('vec3', color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)


class Test8(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
                in vec3 position;
                in vec3 vertexColor;
                out vec3 color;
                void main()
                {
                    gl_Position = vec4(position.x, position.y, position.z, 1.0);
                    color = vertexColor;
                }
                """

        fs_code = """
                    in vec3 color;
                    out vec4 fragColor;
                    void main() 
                    {
                        fragColor = vec4(color.r, color.g, color.b, 1.0);
                    }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        glPointSize(10)
        glLineWidth(4)

        def get_points():
            res = [[0.0, 0.0, 0.0]]
            for x in np.linspace(-2, 0.0001, 1000):
                res.append(
                    [
                        x,
                        math.sqrt(1 - pow(math.fabs(x) - 1, 2)),
                        0.0
                    ]
                )
                res.append(
                    [
                        x,
                        math.acos(1 - math.fabs(x)) - math.pi,
                        0.0
                    ]
                )
                for x in np.linspace(0.0001, 2, 1000):
                    res.append(
                        [
                            x,
                            math.sqrt(1 - pow(math.fabs(x) - 1, 2)),
                            0.0
                        ]
                    )
                    res.append(
                        [
                            x,
                            math.acos(1 - math.fabs(x)) - math.pi,
                            0.0
                        ]
                    )
            return res

        ### set up vao ###
        self.vao_position = glGenVertexArrays(1)
        glBindVertexArray(self.vao_position)
        position_data = np.array(get_points())
        shrink = np.array([
            [1/5, 0, 0],
            [0, 1/5, 0],
            [0, 0, 1/5]
        ])
        position_data = np.array(list(map(lambda v: shrink @ v, position_data)))
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        color_data = np.full((len(position_data), 3), [1.0, 0.411, 0.705])
        color_attribute = Attribute('vec3', color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_POINTS, 0, self.vertex_count)


class Test9(Base):

    def initialize(self):
        print('Initializing program...')

        ### initializing program ###
        vs_code = """
                in vec4 position;
                in vec3 vertexColor;
                out vec3 color;
                void main()
                {
                    gl_Position = vec4(position.x, position.y, position.z, 1.0);
                    color = vertexColor;
                }
                """

        fs_code = """
                    in vec3 color;
                    out vec4 fragColor;
                    void main() 
                    {
                        fragColor = vec4(color.r, color.g, color.b, 1.0);
                    }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        glPointSize(10)
        glLineWidth(4)

        def get_points():
            res = [[0.0, 0.0, 0.0, 1.0]]
            for x in np.linspace(-2, 0.0001, 1000):
                res.append(
                    [
                        x,
                        math.sqrt(1 - pow(math.fabs(x) - 1, 2)),
                        0.0,
                        1.0
                    ]
                )
                res.append(
                    [
                        x,
                        math.acos(1 - math.fabs(x)) - math.pi,
                        0.0,
                        1.0
                    ]
                )
                for x in np.linspace(0.0001, 2, 1000):
                    res.append(
                        [
                            x,
                            math.sqrt(1 - pow(math.fabs(x) - 1, 2)),
                            0.0,
                            1.0
                        ]
                    )
                    res.append(
                        [
                            x,
                            math.acos(1 - math.fabs(x)) - math.pi,
                            0.0,
                            1.0
                        ]
                    )
            return res

        ### set up vao ###
        self.vao_position = glGenVertexArrays(1)
        glBindVertexArray(self.vao_position)
        position_data = np.array(get_points())
        homogeneous_rotation = np.array([
            [-1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])
        shrink = np.array([
            [1/5, 0, 0, 0],
            [0, 1/5, 0, 0],
            [0, 0, 1/5, 0],
            [0, 0, 0, 1],
        ])
        position_data = np.array(list(map(lambda v: homogeneous_rotation @ shrink @ v, position_data)))
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec4', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        color_data = np.full((len(position_data), 3), [1.0, 0.411, 0.705])
        color_attribute = Attribute('vec3', color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_POINTS, 0, self.vertex_count)


class Test10(Base):
    def initialize(self):
        print('Initializing program...')

        vs_code = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {  
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        fs_code = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        ### set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0],
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')


        ### set up uniforms ###
        self.translation1 = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation1.locate_variable(self.program_ref, 'translation')

        self.translation2 = Uniform('vec3', [0.5, 0.0, 0.0])
        self.translation2.locate_variable(self.program_ref, 'translation')

        self.base_color1 = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color1.locate_variable(self.program_ref, 'baseColor')

        self.base_color2 = Uniform('vec3', [0.0, 0.0, 1.0])
        self.base_color2.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        glUseProgram(self.program_ref)

        # draw the first triangle
        self.translation1.upload_data()
        self.base_color1.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

        # draw the second triangle
        self.translation2.upload_data()
        self.base_color2.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


class Test11(Base):
    def initialize(self):
        print('Initialize program...')

        ### initialize program ###
        vs_code = """
                in vec3 position;
                uniform vec3 translation;
                void main()
                {  
                    vec3 pos = position + translation;
                    gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
                }
                """

        fs_code = """
                uniform vec3 baseColor;
                out vec4 fragColor;
                void main()
                {
                    fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
                }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)
        ## set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### set up uniforms ###
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        ### update data ###
        # increase x coordinate of translation
        self.translation.data[0] += 0.01
        # if triangle passes off-screen on the right, change translation
        # so it reappears on the left
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2
        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


class Test12(Base):
    def initialize(self):
        print('Initialize program...')

        ### initialize program ###
        vs_code = """
                in vec3 position;
                uniform vec3 translation;
                void main()
                {  
                    vec3 pos = position + translation;
                    gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
                }
                """

        fs_code = """
                uniform vec3 baseColor;
                out vec4 fragColor;
                void main()
                {
                    fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
                }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)
        ## set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### set up uniforms ###
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        ### update data ###
        self.translation.data[0] = 0.75 * math.cos(self.time)
        self.translation.data[1] = 0.75 * math.sin(self.time)
        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


class Test13(Base):
    def initialize(self):
        print('Initialize program...')

        ### initialize program ###
        vs_code = """
                in vec3 position;
                uniform vec3 translation;
                void main()
                {  
                    vec3 pos = position + translation;
                    gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
                }
                """

        fs_code = """
                uniform vec3 baseColor;
                out vec4 fragColor;
                void main()
                {
                    fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
                }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)
        ## set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### set up uniforms ###
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        ### update data ###
        self.translation.data[0] = 0.75 * math.cos(self.time)
        self.translation.data[1] = 0.75 * math.sin(self.time)
        self.base_color.data[0] = ((math.sin(3 * self.time) + 1) / 2)
        self.base_color.data[1] = ((math.sin(3 * self.time + 2.1) + 1) / 2)
        self.base_color.data[2] = ((math.sin(3 * self.time + 4.2) + 1) / 2)
        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


# check input
class Test14(Base):
    def initialize(self):
        print('Initializing program...')

    def update(self):
        # debug printing
        if len(self.input.key_down_list) > 0:
            print('Keys down:', self.input.key_down_list)

        if len(self.input.key_pressed_list) > 0:
            print('Keys pressed:', self.input.key_pressed_list)

        if len(self.input.key_up_list) > 0:
            print('Keys up:', self.input.key_up_list)


class Test15(Base):
    def initialize(self):
        print('Initialize program...')

        ### initialize program ###
        vs_code = """
                in vec3 position;
                uniform vec3 translation;
                void main()
                {  
                    vec3 pos = position + translation;
                    gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
                }
                """

        fs_code = """
                uniform vec3 baseColor;
                out vec4 fragColor;
                void main()
                {
                    fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
                }
                """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)
        ## set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### set up uniforms ###
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

        self.speed = 0.5

    def update(self):
        ### update data ###
        distance = self.speed * self.delta_time
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2
        if self.translation.data[0] < -1.2:
            self.translation.data[0] = 1.2
        if self.translation.data[1] > 1.2:
            self.translation.data[1] = -1.2
        if self.translation.data[1] < -1.2:
            self.translation.data[1] = 1.2
        if self.input.is_key_pressed('left'):
            self.translation.data[0] -= distance
        if self.input.is_key_pressed('right'):
            self.translation.data[0] += distance
        if self.input.is_key_pressed('down'):
            self.translation.data[1] -= distance
        if self.input.is_key_pressed('up'):
            self.translation.data[1] += distance
        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


class Test16(Base):
    def initialize(self):
        print('Initializing program...')

        ### initialize program ###
        vs_code = """
        in vec3 position;
        uniform mat4 projectionMatrix;
        uniform mat4 modelMatrix;
        void main()
        {
            gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
        }
        """

        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        ### render settings ###
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        ### set up vao ###
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        ### set up vertex attribute ###
        position_data = [
            [0.0, 0.2, 0.0],
            [0.1, -0.2, 0.0],
            [-0.1, -0.2, 0.0],
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### set up uniforms ###
        m_matrix = Matrix.make_translation(0, 0, -1)
        self.model_matrix = Uniform('mat4', m_matrix)
        self.model_matrix.locate_variable(self.program_ref, 'modelMatrix')

        p_matrix = Matrix.make_perspective()
        self.projection_matrix = Uniform('mat4', p_matrix)
        self.projection_matrix.locate_variable(self.program_ref, 'projectionMatrix')

        # movement speed, units per second
        self.move_speed = 0.5
        self.turn_speed = 90 * (math.pi / 180)

    def update(self):
        # update data
        move_amount = self.move_speed * self.delta_time
        turn_amount = self.turn_speed * self.delta_time

        # global translation
        if self.input.is_key_pressed('w'):
            m = Matrix.make_translation(0, move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('s'):
            m = Matrix.make_translation(0, -move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('a'):
            m = Matrix.make_translation(-move_amount, 0, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('d'):
            m = Matrix.make_translation(move_amount, 0, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('z'):
            m = Matrix.make_translation(0, 0, move_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('x'):
            m = Matrix.make_translation(0, 0, -move_amount)
            self.model_matrix.data = m @ self.model_matrix.data

        # global rotation
        if self.input.is_key_pressed('q'):
            m = Matrix.make_rotation_z(turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('e'):
            m = Matrix.make_rotation_z(-turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data

        # local translation
        if self.input.is_key_pressed('i'):
            m = Matrix.make_translation(0, move_amount, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed('k'):
            m = Matrix.make_translation(0, -move_amount, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed('j'):
            m = Matrix.make_translation(-move_amount, 0, 0)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed('l'):
            m = Matrix.make_translation(move_amount, 0, 0)
            self.model_matrix.data = self.model_matrix.data @ m

        # local rotation (around object center)
        if self.input.is_key_pressed('u'):
            m = Matrix.make_rotation_z(turn_amount)
            self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed('o'):
            m = Matrix.make_rotation_z(-turn_amount)
            self.model_matrix.data = self.model_matrix.data @ m

        ### render scene ###
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_ref)
        self.projection_matrix.upload_data()
        self.model_matrix.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
