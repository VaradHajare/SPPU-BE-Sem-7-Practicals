# Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for name, deadline, profit in jobs:
        for j in range(deadline, 0, -1):
            if slots[j] is None:
                slots[j] = name
                total_profit += profit
                break

    return slots[1:], total_profit


n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    name, deadline, profit = input("Enter job, deadline, profit: ").split()
    jobs.append((name, int(deadline), int(profit)))

schedule, profit = job_sequencing(jobs)

print("\nScheduled Jobs:", schedule)
print("Total Profit:", profit)