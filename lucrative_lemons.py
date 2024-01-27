# BODY
class OrderState:
    def __init__(self):
        self.limits = {'stores': 0, 'per_beverage_total': 0}
        self.stores = {}
        self.orders = {'total_orders': 0, 'num_orders': {}}

    def UpdateLimit(self, numberOfStores: int, perBeverageTotal: int) -> None:
        self.limits['stores'] = numberOfStores
        self.limits['per_beverage_total'] = perBeverageTotal
        self.CheckLimits()

    def ProcessOrder(self, uniqueId: int, storeId: int, beverageName: str, quantity: int) -> None:
        if storeId not in self.stores:
            self.stores[storeId] = {'total_orders': 0, 'num_orders': {}}

        # Remove previous order for the same beverage for the given scout
        if uniqueId in self.stores[storeId]['num_orders']:
            prev_order_quantity = self.stores[storeId]['num_orders'][uniqueId].get(beverageName, 0)
            self.orders['total_orders'] -= prev_order_quantity
            self.stores[storeId]['total_orders'] -= prev_order_quantity

        # Update the order for the given scout and store
        if uniqueId not in self.stores[storeId]['num_orders']:
            self.stores[storeId]['num_orders'][uniqueId] = {}
        self.stores[storeId]['num_orders'][uniqueId][beverageName] = quantity
        self.orders['total_orders'] += quantity
        self.stores[storeId]['total_orders'] += quantity

        self.CheckLimits()

    def CloseStore(self, storeId: int) -> None:
        if storeId in self.stores:
            closed_store_orders = self.stores.pop(storeId)
            for uniqueId, beverage_quantity in closed_store_orders['num_orders'].items():
                for beverage, quantity in beverage_quantity.items():
                    self.orders['total_orders'] -= quantity
                    if uniqueId in self.orders['num_orders']:
                        self.orders['num_orders'][uniqueId] -= quantity

    def PrintState(self) -> None:
        print(f"{self.limits['stores']} {self.limits['per_beverage_total']} {self.orders['total_orders']} {len(self.orders['num_orders'])}")

    def CheckLimits(self):
        if self.limits['stores'] < len(self.stores) or self.limits['per_beverage_total'] < self.orders['total_orders']:
            self.CloseAllStores()

    def CloseAllStores(self):
        for storeId in self.stores.copy():
            self.CloseStore(storeId)

# TAIL
if __name__ == "__main__":
    import sys

    def read_line(): return sys.stdin.readline().split()

    orderState = OrderState()

    while True:
        line = read_line()
        if len(line) == 0:
            break

        operation = line[0]
        if operation == 'UPDATE_LIMIT':
            numberOfStores = int(line[1])
            perBeverageTotal = int(line[2])
            orderState.UpdateLimit(numberOfStores, perBeverageTotal)
        elif operation == 'ORDER_UPDATE':
            uniqueId = int(line[1])
            storeId = int(line[2])
            beverageName = str(line[3])
            quantity = int(line[4])
            orderState.ProcessOrder(uniqueId, storeId, beverageName, quantity)
        elif operation == 'CLOSE_STORE':
            storeId = int(line[1])
            orderState.CloseStore(storeId)
        elif operation == 'PRINT_STATE':
            orderState.PrintState()
        else:
            raise ValueError('Invalid Input')
