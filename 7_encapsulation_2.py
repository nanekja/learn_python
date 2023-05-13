
class MyInt(object):
    def set_val(self, val):
        try:
            val = int(val)

        except ValueError:
            return

        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1


a_obj = MyInt()

a_obj.set_val(10)

print(a_obj.get_val())

a_obj.set_val('hello')

print(a_obj.increment_val())
