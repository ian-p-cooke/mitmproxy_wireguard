from typing import Awaitable, Callable, Optional

class WireguardServer:
    def getsockname(self) -> tuple[str, int]: ...
    def send_datagram(self, data: bytes, src_addr: tuple[str, int], dst_addr: tuple[str, int]) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...

class WireguardConf:
    @staticmethod
    def build(listen_port: int, server_private_key: str, peer_keys: list[tuple[str, Optional[str]]]) -> WireguardConf: ...
    @staticmethod
    def load_from_path(path: str) -> WireguardConf: ...
    @staticmethod
    def load_from_str(string: str) -> WireguardConf: ...

class TcpStream:
    async def read(self, n: int) -> bytes: ...
    def write(self, data: bytes): ...
    async def drain(self) -> None: ...
    def write_eof(self): ...
    def close(self): ...
    def get_extra_info(self, name: str) -> tuple[str, int]: ...
    def __repr__(self) -> str: ...

async def start_server(
    host: str,
    conf: WireguardConf,
    handle_connection: Callable[[TcpStream], Awaitable[None]],
    receive_datagram: Callable[[bytes, tuple[str, int], tuple[str, int]], None],
) -> WireguardServer: ...
def genkey() -> str: ...
def pubkey(private_key: str) -> str: ...
