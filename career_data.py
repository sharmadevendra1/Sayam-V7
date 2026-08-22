# career_data.py - SAYAM v7.0 BRAND NEW - 18 RIASEC Questions
RIASEC_QUESTIONS = [
    {"id":1,"type":"R","text":"I enjoy repairing machines or building things with tools","options":[1,2,3,4,5]},
    {"id":2,"type":"R","text":"I like working outdoors with plants or animals","options":[1,2,3,4,5]},
    {"id":3,"type":"I","text":"I enjoy solving puzzles and analyzing problems","options":[1,2,3,4,5]},
    {"id":4,"type":"I","text":"I like conducting experiments and research","options":[1,2,3,4,5]},
    {"id":5,"type":"A","text":"I enjoy drawing, painting, or creative writing","options":[1,2,3,4,5]},
    {"id":6,"type":"A","text":"I like playing music or performing on stage","options":[1,2,3,4,5]},
    {"id":7,"type":"S","text":"I enjoy helping people with their problems","options":[1,2,3,4,5]},
    {"id":8,"type":"S","text":"I like teaching or training others","options":[1,2,3,4,5]},
    {"id":9,"type":"E","text":"I enjoy leading a team or managing projects","options":[1,2,3,4,5]},
    {"id":10,"type":"E","text":"I like persuading people and selling ideas","options":[1,2,3,4,5]},
    {"id":11,"type":"C","text":"I enjoy organizing files and data accurately","options":[1,2,3,4,5]},
    {"id":12,"type":"C","text":"I like working with numbers and spreadsheets","options":[1,2,3,4,5]},
    {"id":13,"type":"R","text":"I enjoy operating heavy equipment or vehicles","options":[1,2,3,4,5]},
    {"id":14,"type":"I","text":"I like understanding how things work scientifically","options":[1,2,3,4,5]},
    {"id":15,"type":"A","text":"I enjoy designing new things or decorating","options":[1,2,3,4,5]},
    {"id":16,"type":"S","text":"I like working in a team to support community","options":[1,2,3,4,5]},
    {"id":17,"type":"E","text":"I enjoy starting my own business or initiative","options":[1,2,3,4,5]},
    {"id":18,"type":"C","text":"I like following clear rules and procedures","options":[1,2,3,4,5]},
]

CAREER_MAP = {
    "R": ["Mechanical Engineer","Electrician","Civil Engineer","Pilot","Agriculture Officer","Automobile Engineer"],
    "I": ["Scientist","Data Analyst","Doctor","Researcher","Software Engineer","Biotechnologist"],
    "A": ["Graphic Designer","Writer","Musician","Architect","Film Maker","Fashion Designer"],
    "S": ["Teacher","Counselor","Nurse","Social Worker","HR Manager","Psychologist"],
    "E": ["Entrepreneur","Marketing Manager","Lawyer","Sales Manager","CEO","Business Analyst"],
    "C": ["Accountant","Bank Manager","Auditor","Data Entry Specialist","Administrator","Tax Consultant"]
}

PRICING = {
    "free": {"price":0,"currency":"INR","reports":1,"careers":1,"features":["1 Basic Report","1 Career Suggestion"]},
    "premium": {"price":479,"currency":"INR","reports":"unlimited","careers":5,"upi_id":"mail2dms-1@okaxis","features":["Unlimited Reports","5 Career Suggestions","Detailed RIASEC Analysis","PDF Download","Email Support: info@sayamconsulting.com"]}
}
