from typing import Optional, Dict, Any, List

from requests import Request, Session, Response


class TradingBotService:
    def __init__(
            self,
            base_url: str,
    ) -> None:
        self._session = Session()
        self._base_url = base_url

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('GET', path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('POST', path, json=params)

    def _delete(self,
                path: str,
                params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('DELETE', path, json=params)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._base_url + path, **kwargs)
        response = self._session.send(request.prepare())

        return self._process_response(response)

    @staticmethod
    def _process_response(response: Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            raise
        else:
            if not data:
                raise Exception(data)
            return data

    def get_status(self) -> str:
        return self._get('status')

    def get_markets(self) -> List[str]:
        return self._get('markets')
