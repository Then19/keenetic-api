from src.service.exceptions import create_service_exception

MacNotFound = create_service_exception('Mac address not found', 404)
PolicyNotFound = create_service_exception('Policy not found', 404)
