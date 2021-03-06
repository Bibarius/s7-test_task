import aiohttp
from aiohttp import ClientSession, ClientConnectionError
from urllib.parse import urljoin

# booking_service_api_root = 'http://localhost:5000'
booking_service_api_root = 'http://mockservice:5000'


async def book_ski(request):
    orders = await call_booking_service('GET', 'orders', params=request.dict())
    payload = await parse_orders(orders)
    return await call_booking_service('PUT', 'bags', json=payload)



async def parse_orders(orders):
    baggageSelections = []
    for anc_pr in orders['ancillariesPricings']:
        for bag_pr in anc_pr['baggagePricings']:
            for pass_id in bag_pr['passengerIds']:

                unit = {
                    'passengerId': pass_id,
                    'routeId': bag_pr['routeId'],
                    'baggageIds': [],
                    'redemption': False
                }

                for baggage in bag_pr['baggages']:
                    if 'equipmentType' in baggage and baggage['equipmentType'] == 'ski':
                        unit['baggageIds'].append(baggage['id'])

                baggageSelections.append(unit)

    return {'baggageSelections': baggageSelections}



async def call_booking_service(http_method, endpoing, **kwargs):
    async with ClientSession() as session:
        async with session.request(http_method, urljoin(booking_service_api_root, endpoing), **kwargs) as response:
            return await response.json()