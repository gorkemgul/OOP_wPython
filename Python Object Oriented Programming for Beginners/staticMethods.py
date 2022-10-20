# ========================================================================================== #
#                             The Concept of the Static Methods                              #
# ========================================================================================== #

# Define a class that includes some methods that are not specific to an instance
class Math:

    # Static means not changing, staying the same. They don't have access to anything
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def sub10(x):
        return x - 10

    @staticmethod
    def sub5(x):
        return x - 5

    @staticmethod
    def multip2(x):
        return x * 2

    @staticmethod
    def div4(x):
        return x / 4

    @staticmethod
    def pr():
        print('print')

# Use the static methods
print(Math.add5(5))
print(Math.div4(4))
print(Math.multip2(10))
print(Math.sub10(25))