import os

def load_logs(filename: str) -> list:
    """log.txt 파일을 읽어 각 줄을 리스트로 저장하여 반환"""
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 파일의 디렉토리
    file_path = os.path.join(script_dir, filename)  # 절대 경로 생성

    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
    
def parse_logs(log_lines: list) -> dict:
    """로그 리스트를 날짜별 사용자 활동 딕셔너리로 변환"""

    log_data = {}

    for line in log_lines:

        date, user, activity = line.split() # 줄마다 형식이 정해져있으니 변수에 각각 들어가게 한다

        if date not in log_data:
            log_data[date] = {}

        if user not in log_data[date]:
            log_data[date][user] = []

        log_data[date][user].append(activity)
        
    return log_data

def get_user_activity(log_data: dict, user_id: str) -> dict:
    """특정 사용자의 활동 내역을 날짜별로 반환"""

    user_act = {}

    for date, users in log_data.items():
        if user_id in users:
            user_act[date] = users[user_id]
    
    return user_act

def save_summary(log_data: dict, filename: str) -> None:
    """날짜별 사용자 활동 내역을 summary.txt 파일로 저장"""

    with open(filename, "w", encoding="utf-8") as file:
        for date, users in sorted(log_data.items()):
            file.write(f"{date}\n")
            for user, activities in users.items():
                activity_list = ", ".join(activities)
                file.write(f"- {user}: {activity_list}\n")
            file.write("\n")