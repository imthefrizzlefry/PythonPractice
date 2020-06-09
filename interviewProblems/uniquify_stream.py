''' asked by Google

Given a real-time source of data, “uniquify” all duplications which were received within 10 seconds of each other

“Foo” @12:00:00
“Bar” @12:00:02
“Foo” @12:00:08
“Bar” @12:00:11  <- added by me
“Bar” @12:00:15
“Foo” @12:00:19
“Foo” @12:00:59  <- added by recruiter (follow up)
“Foo” @12:01:00  <- added by recruiter (follow up)
“Foo” @12:02:00  <- added by recruiter (follow up)

A: Foo Bar Bar Foo
'''

# datetime.timedelta()
from datetime import datetime

def u_s(input):
    r_s = []
    w_s = {}
    for line in input:
        
        cur = line.split(" ")
        cur[0] = cur[0].strip('"')
        cur[1] = cur[1].strip('@')
        cur[1] = cur[1].strip('\n')

        w_t = datetime.strptime(cur[1], "%H:%M:%S")
        if cur[0] not in w_s:
            w_s[cur[0]] = w_t
            r_s.append(cur[0])
        else:
            if (w_t - w_s[cur[0]]).total_seconds() > 10: 
                w_s[cur[0]] = w_t
                r_s.append(cur[0])

    return r_s


if __name__ == "__main__":
    f = open("./interviewProblems/timestream.txt", "r", encoding="utf-8")
    print(u_s(f))