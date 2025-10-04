import httpx
import hashlib
from src.config import config
from src.service.keenetic.exceptions import MacNotFound, PolicyNotFound
from src.service.keenetic.schemas import PolicyInfo


class KeeneticController:
    TIMEOUT = 60
    BASE_URL = f"http://{config.keenetic.ip}"
    AUTH_URL = BASE_URL + "/auth"
    RCI_URL = BASE_URL + "/rci"

    _client: httpx.AsyncClient

    _login: str
    _password: str

    def __init__(self, login=config.keenetic.user, password=config.keenetic.password):
        self._login = login
        self._password = password
        self._client = httpx.AsyncClient(timeout=self.TIMEOUT)

    async def keenetic_auth(self):
        response = await self._client.get(self.AUTH_URL)

        if response.status_code == 401:
            md5 = self._login + ":" + response.headers["X-NDM-Realm"] + ":" + self._password
            md5 = hashlib.md5(md5.encode('utf-8'))
            sha = response.headers["X-NDM-Challenge"] + md5.hexdigest()
            sha = hashlib.sha256(sha.encode('utf-8'))
            await self._client.post(self.AUTH_URL, json={"login": self._login, "password": sha.hexdigest()})

    async def change_device_policy(self, mac_address, policy_name):
        await self.keenetic_auth()
        await self._client.post(f"{self.RCI_URL}/ip/hotspot/host", json={"mac": mac_address, "policy": policy_name, 'permit': True})
        await self._client.post(f"{self.RCI_URL}/system/configuration/save",json={})

    async def get_device_policy(self, mac_address: str) -> PolicyInfo:
        await self.keenetic_auth()

        mac_address = mac_address.lower()
        policy_data = (await self._client.get(f"{self.RCI_URL}/show/sc/ip/hotspot/host")).json()
        for info in policy_data:
            if info["mac"] == mac_address:
                policy = info.get("policy")
                if policy:
                    return PolicyInfo(mac=mac_address, policy=policy)
                raise PolicyNotFound()
        raise MacNotFound()


keenetic_controller_client = KeeneticController()
