# ---------------------------- #
# a1----------a2               #
#         b1--------------b2   #
# ---------------------------- #
def is_overlapping(a1, a2, b1, b2):
    return a1 <= b2 and a2 >= b1


class Edge:
    def __init__(self, source_node, dest_node, distance):
        self.sourceNode = source_node
        self.destNode = dest_node
        self.distance = distance

    def __str__(self):
        return '%s --> %s' % (self.sourceNode, self.destNode)


class Road(Edge):
    def __init__(self, source_node, dest_node, distance):
        super().__init__(source_node, dest_node, distance)
        self.users = {}

    def _can_user_join(self, user):
        startX = - user.length / 2
        endX = user.length / 2

        for roadUser in self.users:
            if user != roadUser:
                startX2, endX2 = self._get_user_position(roadUser)
                if is_overlapping(startX, endX, startX2, endX2):
                    return False
        return True

    def join_user(self, user):
        if self._can_user_join(user):
            self.users[user] = 0
            return True
        else:
            return False

    def can_user_move(self, user, vector):
        currentPosition = self.users.get(user)
        currentEndX = currentPosition + user.length / 2
        destinationEndX = currentEndX + vector

        for roadUser in self.users:
            if user != roadUser:
                startX, endX = self._get_user_position(roadUser)
                if is_overlapping(currentEndX, destinationEndX, startX, endX):
                    return False
        return True

    def move_user(self, user, vector):
        self.users[user] += vector

    def leave_user(self, user):
        self.users.pop(user)

    def _get_user_position(self, user):
        position = self.users.get(user, -1)
        return position - user.length / 2, position + user.length / 2
