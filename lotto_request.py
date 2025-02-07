import requests
import json

def get_lotto_numbers(start_round, end_round):
    lotto_numbers = []
    
    for round in range(start_round, end_round+1):
        url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['returnValue'] == 'success':
                numbers = [
                    data["drwtNo1"], data["drwtNo2"], data["drwtNo3"], 
                    data["drwtNo4"], data["drwtNo5"], data["drwtNo6"]
                ]
                lotto_numbers.append(numbers)
    
    return lotto_numbers

print(get_lotto_numbers(1156, 1157))