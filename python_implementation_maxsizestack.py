class MaxSizeStack:
    def __init__(self):
        self.stack = bytearray()
        self.max_size = 520

    def push(self, data):
        if len(self.stack) + len(data) > self.max_size:
            print("Stack overflow! Data exceeds maximum size.")
            return
        self.stack.extend(data)

    def pop(self, size):
        if size > len(self.stack):
            print("Stack underflow! Not enough data to pop.")
            return bytearray()
        popped_data = self.stack[-size:]
        del self.stack[-size:]
        return popped_data

    def push_n_pop(self, data1, data2):
        # Pop the top two elements from the stack
        popped_data1 = self.pop(len(data1))
        popped_data2 = self.pop(len(data2))

        # Combine the popped data and push it back onto the stack
        combined_data = popped_data1 + popped_data2
        self.push(combined_data)

# Example Usage:
stack = MaxSizeStack()

# Pushing data onto the stack
stack.push(b"Hello, ")
stack.push(b"world!")

# Checking the current size of the stack
print("Current stack size:", stack.size())

# Using push_n_pop to pop the top two elements and push a combined one
stack.push_n_pop(b"Hello, ", b"world!")

# Checking the updated size of the stack
print("Updated stack size:", stack.size())