# # SOLID
# class Report:
#     def generate(self):
#         return "Отчет"
    
# class ReportSaver:
#     def save_to_file(self, content):
#         with open ("report.txt" 'w') as f:
#                    f.write(content)


# class Orders:
#     def add(self):
#         return "добавлено"
#     def show(self):
#         return'показано"
#     def save(self):
#         return "сохранено"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items


class OrderPrinter:
    def print(self, order: Order):
        for item in order.get_items():
            print(f"Блюдо: {item}")


class OrderSaver:
    def save_to_file(self, order: Order, filename="order.txt"):
        with open(filename, "w") as f:
            for item in order.get_items():
                f.write(f"{item}\n")



order = Order()
order.add_item("Пицца")
order.add_item("Салат")



printer = OrderPrinter()
printer.print(order)

saver = OrderSaver()
saver.save_to_file(order)