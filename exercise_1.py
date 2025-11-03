class StringFoo:
    def __init__(self, string,):
        self.string = string
    def print_string(self):
        print(f"I AM{self.string}")

message = StringFoo(string="i am ryan")
message.print_string()

