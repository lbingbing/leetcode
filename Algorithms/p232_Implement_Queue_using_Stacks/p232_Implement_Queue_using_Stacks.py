class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def test_and_shift(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in[-1])
                self.stack_in.pop()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.test_and_shift()
        self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.test_and_shift();
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_out and not self.stack_in
