from log_analysis import load_logs, parse_logs, get_user_activity, save_summary

logs = load_logs("log.txt")

log_data = parse_logs(logs)

user_activity = get_user_activity(log_data, "user123")
print(user_activity)
save_summary(log_data, "summary.txt")
