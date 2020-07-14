# controllers are singletons, only this should be imported to external code
from api.controllers.bookings import bookingsController
from api.controllers.cars import carsController
from api.controllers.reports import reportsController
from api.controllers.users import usersController