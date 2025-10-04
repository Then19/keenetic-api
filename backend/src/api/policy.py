from fastapi import APIRouter, Body, Query

from src.api.dependencies import service_exception_handler
from src.service.keenetic.keenetic_controller import keenetic_controller_client
from src.service.keenetic.schemas import PolicyInfo

router = APIRouter(prefix="/policy", tags=["policy"])


@router.post('/change')
@service_exception_handler
async def change_policy(
    device_mac: str = Query(...),
    policy_name: str = Query(...),
):
    await keenetic_controller_client.change_device_policy(device_mac, policy_name)


@router.get('/current')
@service_exception_handler
async def current_policy(
    device_mac: str = Query(...),
) -> PolicyInfo:
    return await keenetic_controller_client.get_device_policy(device_mac)
