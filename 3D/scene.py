# coding=utf-8
import numpy

class Scene(object):
    # 放置节点的深度
    PLACE_DEPTH = 15.0

    def __init__(self):
        # 场景下的节点队列
        self.node_list = list()
        self.selected_node = None

    def add_node(self, node):
        """ 在场景中加入一个节点 """
        self.node_list.append(node)

    def render(self):
        """ 遍历场景下所有的节点并渲染 """
        for node in self.node_list:
            node.render()

    def pick(self, start, direction, mat):

        import  sys

        if self.selected_node is not None:
            self.selected_node.select(False)
            self.selected_node = None

        mindist = sys.maxint
        closest_node = None
        for node in self.node_list:
            hit, distance = node.pick(start, direction, mat)
            if hit and distance < mindist:
                mindist, closest_node = distance, node

        if closest_node is not None:
            closest_node.select()
            closest_node.depth = mindist
            closest_node.selected_loc = start + direction * mindist
            self.selected_node = closest_node

    def move_selected(self, start, direction, inv_modelView):
        if self.selected_node is None: return

        node = self.selected_node
        depth = node.depth
        oldloc = node.selected_loc

        newloc = (start + direction * depth)

        translation = newloc - oldloc
        pre_tran = numpy.array([translation[0], translation[1], translation[2], 0])
        translation = inv_modelView.dot(pre_tran)

        node.translate(translation[0], translation[1], translation[2])
        node.selected_loc = newloc