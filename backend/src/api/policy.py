from fastapi import APIRouter, Body, Query

from src.service.keenetic.keenetic_controller import keenetic_controller_client

router = APIRouter(prefix="/policy", tags=["policy"])


@router.post('/change')
async def change_policy(
    device_mac: str = Query(...),
    policy_name: str = Query(...),
):
    return await keenetic_controller_client.change_device_policy(device_mac, policy_name)
