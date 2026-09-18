# === Stage 36: Add templates for quickly creating common records ===
# Project: RoutePlanner
class Template:
    """Factory for common RoutePlanner records."""
    @staticmethod
    def new_stop(name, address, lat=None, lon=None):
        return Stop(name, address, lat=lat, lon=lon)

    @staticmethod
    def new_schedule(date, time, duration, notes=""):
        return Schedule(date, time, duration, notes=notes)

    @staticmethod
    def new_route(stops, distance=0.0, vehicle="van"):
        return Route(stops, distance, vehicle)

    @staticmethod
    def new_driver(name, phone, license_id):
        return Driver(name, phone, license_id)

    @staticmethod
    def new_vehicle(model, plate, capacity=0):
        return Vehicle(model, plate, capacity)

    @staticmethod
    def new_delivery_item(product, quantity=1, price=0):
        return DeliveryItem(product, quantity, price)

    @staticmethod
    def new_order(customer, items, priority="normal"):
        return Order(customer, items, priority)

    @staticmethod
    def new_completions(route, notes="Completed", duration=0):
        return Completions(route, notes, duration)
