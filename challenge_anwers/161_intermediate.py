"""
Given a number of potential jobs/workers, assign jobs to workers
based on unique skill matches. My solution didn't work, but I've
included the most elegant solution presented on Reddit.
"""

def my_solution():
    num_jobs_workers = int(raw_input("How many jobs/workers? "))

    job_input_count = num_jobs_workers
    worker_input_count = num_jobs_workers
    avail_jobs = []
    avail_workers = {}

    while job_input_count > 0:
        job = raw_input("Please enter a job (%s left): " % job_input_count)
        avail_jobs.append(job)
        job_input_count -= 1

    while worker_input_count > 0:
        worker = raw_input("Please enter a worker followed by skill "
                           "list (%s left): " % worker_input_count)
        name, skills = worker.split(' ', 1)
        skill_list = skills.split(',')
        avail_workers[name] = skill_list
        worker_input_count -= 1

    for jobs in avail_jobs:
        for worker, skill in avail_workers.iteritems():
            if job in skill:
                print "%s\t%s" % (worker, jobs)
                avail_jobs.remove(job)

def elegant_solution():
    from itertools import product

    jobs = {}
    worker = ' '

    while worker:
        worker, sep, skills = input().strip().partition(' ')
        if skills:
            jobs[worker] = {skill.strip() for skill in skills.split(',')}

    for name, job in zip(jobs, next(x for x in product(*jobs.values()) if len(x) == len(set(x)))):
        print(name + ' ' + job)