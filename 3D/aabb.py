# coding=utf-8
from OpenGL.GL import glCallList, glMatrixMode, glPolygonMode, glPopMatrix, glPushMatrix, glTranslated, \
                      GL_FILL, GL_FRONT_AND_BACK, GL_LINE, GL_MODELVIEW
from primtive import G_OBJ_CUBE
import numpy
import math

# 判断误差
EPSILON = 0.000001


class AABB(object):

    def __init__(self, center, size):
        self.center = numpy.array(center)
        self.size = numpy.array(size)

    def scale(self, scale):
        self.size *= scale

    def ray_hit(self, origin, direction, modelmatrix):
        """
        :param origin: 激光原点
        :param directuin: 激光方向
        :param modelmatrix: 世界坐标到局部坐标的转换矩阵
        :return: True 击中
        """
        aabb_min = self.center - self.size
        aabb_max = self.center + self.size
        tmin = 0.0
        tmax = 100000.0

        obb_pos_worldspace = numpy.array([modelmatrix[0, 3], modelmatrix[1, 3], modelmatrix[2, 3]])
        delta = (obb_pos_worldspace - origin)

        # test intersection with 2 planes perpendicular to OBB's x-axis
        xaxis = numpy.array((modelmatrix[0, 0],modelmatrix[0, 1], modelmatrix[0, 2]))
        e = numpy.dot(xaxis, delta)
        f = numpy.dot(direction, xaxis)
        if math.fabs(f) > 0.0 + EPSILON:
            t1 = (e + aabb_min[0])/f
            t2 = (e + aabb_max[0])/f
            if t1 > t2:
                t1, t2 = t2, t1
            if t2 < tmax:
                tmax = t2
            if t1 > tmin:
                tmin = t1
            if tmax < tmin:
                return (False, 0)
        else:
            if (-e + aabb_min[0] > 0.0 + EPSILON) or (-e + aabb_max[0] < 0.0 - EPSILON):
                return False, 0

        yaxis = numpy.array((modelmatrix[1, 0],modelmatrix[1, 1], modelmatrix[1, 2]))
        e = numpy.dot(yaxis, delta)
        f = numpy.dot(direction, yaxis)
        if math.fabs(f) > 0.0 + EPSILON:
            t1 = (e + aabb_min[0])/f
            t2 = (e + aabb_max[0])/f
            if t1 > t2:
                t1, t2 = t2, t1
            if t2 < tmax:
                tmax = t2
            if t1 > tmin:
                tmin = t1
            if tmax < tmin:
                return (False, 0)
        else:
            if (-e + aabb_min[0] > 0.0 + EPSILON) or (-e + aabb_max[0] < 0.0 - EPSILON):
                return False, 0

        zaxis = numpy.array((modelmatrix[2, 0],modelmatrix[2, 1], modelmatrix[2, 2]))
        e = numpy.dot(zaxis, delta)
        f = numpy.dot(direction, zaxis)
        if math.fabs(f) > 0.0 + EPSILON:
            t1 = (e + aabb_min[0])/f
            t2 = (e + aabb_max[0])/f
            if t1 > t2:
                t1, t2 = t2, t1
            if t2 < tmax:
                tmax = t2
            if t1 > tmin:
                tmin = t1
            if tmax < tmin:
                return (False, 0)
        else:
            if (-e + aabb_min[0] > 0.0 + EPSILON) or (-e + aabb_max[0] < 0.0 - EPSILON):
                return False, 0
        return True, tmin

    def render(self):
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslated(self.center[0], self.center[1], self.center[2])
        glCallList(G_OBJ_CUBE)
        glPopMatrix()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

