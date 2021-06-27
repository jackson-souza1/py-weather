"""Contem payloads necessarios parar o processo do crawler
"""

headers = {
    "Connection":"keep-alive",
    "sec-ch-ua": '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "Accept": "*/*",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://openweathermap.org/",
    "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"

}