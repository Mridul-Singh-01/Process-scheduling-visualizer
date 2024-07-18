class FCFS:
    def __init__(self, processes):
        self.processes = processes  # List of processes, each process is a dictionary with 'pid', 'arrival_time', 'burst_time'

    def schedule(self):
        n = len(self.processes)
        completion_time = [0] * n
        turnaround_time = [0] * n
        waiting_time = [0] * n

        # Sort processes by arrival time
        self.processes.sort(key=lambda x: x['arrival_time'])
        for i in range(n):
            if i == 0:
                completion_time[i] = self.processes[i]['arrival_time'] + self.processes[i]['burst_time']
            else:
                if self.processes[i]['arrival_time'] > completion_time[i-1]:
                    completion_time[i] = self.processes[i]['arrival_time'] + self.processes[i]['burst_time']
                else:
                    completion_time[i] = completion_time[i-1] + self.processes[i]['burst_time']
            turnaround_time[i] = completion_time[i] - self.processes[i]['arrival_time']
            waiting_time[i] = turnaround_time[i] - self.processes[i]['burst_time']
            
        for i in range(n):
            self.processes[i]['completion_time'] = completion_time[i]
            self.processes[i]['turnaround_time'] = turnaround_time[i]
            self.processes[i]['waiting_time'] = waiting_time[i]
        return self.processes
    def print_gantt_chart(self):
        timeline = []
        current_time = 0

        for process in self.processes:
            if process['arrival_time'] > current_time:
                idle_time = process['arrival_time'] - current_time
                timeline.append(('Idle', idle_time))
                current_time = process['arrival_time']
            
            timeline.append((f"P{process['pid']}", process['burst_time']))
            current_time += process['burst_time']

        # Print Gantt Chart
        print("Gantt Chart:")
        for task, duration in timeline:
            print(f"{task}: {'#' * duration} ({duration})")

if __name__ == "__main__":
    processes = [
        {'pid': 1, 'arrival_time': 0, 'burst_time': 4},
        {'pid': 2, 'arrival_time': 1, 'burst_time': 3},
        {'pid': 3, 'arrival_time': 2, 'burst_time': 1},
        {'pid': 4, 'arrival_time': 12, 'burst_time': 2}
    ]
    scheduler = FCFS(processes)
    scheduled_processes = scheduler.schedule()
    print("PID  Arrival  Burst  Completion  Turnaround  Waiting")
    for process in scheduled_processes:
        print(f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t{process['completion_time']}\t\t{process['turnaround_time']}\t{process['waiting_time']}")
    scheduler.print_gantt_chart()