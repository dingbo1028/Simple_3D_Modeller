# coding=utf-8


class Scene(object):
    # 放置节点的深度
    PLACE_DEPTH = 15.0

    def __init__(self):
        # 场景下的节点队列
        self.node_list = list()

    def add_node(self, node):
        """ 在场景中加入一个节点 """
        self.node_list.append(node)

    def render(self):
        """ 遍历场景下所有的节点并渲染 """
        for node in self.node_list:
            node.render()
