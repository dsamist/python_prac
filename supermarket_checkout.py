class SupermarketCheckout:
    def __init__(self):
        self.customers = {}  # Dictionary to store customer information
        self.lines = {}      # Dictionary to store checkout line information

    def on_customer_enter(self, customer_id, line_number, num_items):
        if line_number not in self.lines:
            self.lines[line_number] = []  # Initialize the checkout line if not exists

        # Add customer to the specified checkout line with their basket information
        self.lines[line_number].append({'customer_id': customer_id, 'num_items': num_items})

        # Store customer information for quick access
        self.customers[customer_id] = {'line_number': line_number, 'num_items': num_items}

    def on_basket_change(self, customer_id, new_num_items):
        if customer_id in self.customers:
            line_number = self.customers[customer_id]['line_number']

            # Update the customer's basket information
            for customer in self.lines[line_number]:
                if customer['customer_id'] == customer_id:
                    customer['num_items'] = new_num_items
                    break

            # Update the customer information for quick access
            self.customers[customer_id]['num_items'] = new_num_items

    def on_line_service(self, line_number, num_processed_items):
        # TODO Implement
        processed_customers = []
        
        if line_number in self.lines:
            #process the specified numbers of items in the checkout line
            while num_processed_items > 0 and self.lines[line_number]:
                customer = self.lines[line_number][0]
                #check that the customer has no more items to process
                if customer['num_items'] > num_processed_items:
                    customer['num_items'] -= num_processed_items
                    num_processed_items = 0
                else:
                    num_processed_items -= customer['num_items']
                    #customer has no items and they are free to leave
                    processed_customers.append(customer['customer_id'])
                    self.lines[line_number].pop(0)
        
        if processed_customers:
            for cust_id in reversed(processed_customers):
                print(cust_id)

    def on_lines_service(self):
        # Process one item in every checkout line
        for line_number in self.lines:
            self.on_line_service(line_number, 1)

    def on_customer_exit(self, customer_id):
        # This method is already implemented and should not be changed.
        print(customer_id)

# Main execution
if __name__ == "__main__":
    import sys

    checkout_tracker = SupermarketCheckout()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "CustomerEnter":
            customer_id = int(line[1])
            line_number = int(line[2])
            num_items = int(line[3])
            checkout_tracker.on_customer_enter(customer_id, line_number, num_items)
        elif line[0] == "BasketChange":
            customer_id = int(line[1])
            new_num_items = int(line[2])
            checkout_tracker.on_basket_change(customer_id, new_num_items)
        elif line[0] == "LineService":
            line_number = int(line[1])
            num_processed_items = int(line[2])
            checkout_tracker.on_line_service(line_number, num_processed_items)
        elif line[0] == "LinesService":
            checkout_tracker.on_lines_service()
        else:
            raise Exception("Malformed input!")
