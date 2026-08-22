from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="SAYAM Career Counseling - api.sayamconsulting.com", version="7.0 BRAND NEW", description="Verified domain: sayamconsulting.com")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sayamconsulting.com", "https://www.sayamconsulting.com", "https://api.sayamconsulting.com", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === MODELS ===
class QuizAnswer(BaseModel):
    question_id: int
    score: int

class CounselingRequest(BaseModel):
    name: str
    age: int
    education: str
    interests: List[str]
    skills: List[str]
    answers: List[QuizAnswer]
    plan: str = "free"

# === ROOT ===
@app.get("/")
def root():
    return {
        "status": "ok",
        "version": "7.0 BRAND NEW - FROM SCRATCH",
        "verified_domain": "api.sayamconsulting.com",
        "main_domain": "sayamconsulting.com",
        "email": "info@sayamconsulting.com",
        "privacy_policy": "https://api.sayamconsulting.com/privacy-policy",
        "health": "https://api.sayamconsulting.com/api/health",
        "questions": "https://api.sayamconsulting.com/api/questions"
    }

# === PRIVACY POLICY - THIS FIXES YOUR 404 - MUST BE BEFORE OTHER ROUTES ===
@app.get("/privacy-policy", response_class=HTMLResponse, tags=["Legal"])
@app.get("/privacy", response_class=HTMLResponse, tags=["Legal"])
@app.get("/api/privacy-policy", response_class=HTMLResponse, tags=["Legal"])
@app.get("/api/privacy", response_class=HTMLResponse, tags=["Legal"])
def privacy_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Privacy Policy - SAYAM Career Counseling | sayamconsulting.com</title>
        <style>
            body{font-family:Arial,sans-serif;line-height:1.7;padding:24px;max-width:900px;margin:auto;color:#222}
            h1{color:#1a56db} h2{color:#333;margin-top:24px;border-bottom:1px solid #eee;padding-bottom:8px}
            .badge{background:#1a56db;color:#fff;padding:4px 12px;border-radius:20px;font-size:12px}
        </style>
    </head>
    <body>
        <h1>Privacy Policy - SAYAM Career Counseling</h1>
        <p><span class="badge">VERIFIED</span> <b>Domain:</b> sayamconsulting.com | <b>API:</b> api.sayamconsulting.com | <b>Email:</b> info@sayamconsulting.com</p>
        <p><b>Play Store Privacy Policy URL:</b> https://api.sayamconsulting.com/privacy-policy</p>
        <p><b>Effective:</b> August 2026 | <b>App:</b> SAYAM - Career Counseling & Guidance</p>
        
        <h2>1. Data We Collect</h2>
        <ul>
            <li><b>Personal:</b> Name, Email, Mobile, DOB (13+ only), Education, City</li>
            <li><b>Assessment:</b> RIASEC 18 Questions answers, Interests, Skills</li>
            <li><b>Payment:</b> Razorpay Payment ID only (Rs 479). No card, UPI PIN, or bank details stored. UPI ID: mail2dms-1@okaxis</li>
            <li><b>Technical:</b> Device info for crash reporting only</li>
        </ul>

        <h2>2. How We Use</h2>
        <p>Provide career counseling reports, RIASEC code, payment processing, support at info@sayamconsulting.com</p>

        <h2>3. Payment - Razorpay</h2>
        <p>Rs 479 processed via Razorpay secure gateway (UPI, Cards, NetBanking). We store only Razorpay Payment ID. Razorpay has its own privacy policy.</p>

        <h2>4. Data Deletion & Your Rights</h2>
        <p><b>Delete:</b> Call DELETE https://api.sayamconsulting.com/api/user/delete or email info@sayamconsulting.com with subject "Delete My Data". Deleted in 7 days.</p>
        <p><b>Children:</b> 13+ only. Under 13 not allowed.</p>

        <h2>5. Contact</h2>
        <p>Email: info@sayamconsulting.com | Website: https://sayamconsulting.com | API: https://api.sayamconsulting.com | Address: Pune, Maharashtra, India</p>

        <h2>6. Play Store Compliance</h2>
        <p>This privacy policy URL (https://api.sayamconsulting.com/privacy-policy) is submitted in Play Console. No sensitive data sold. No location tracking.</p>
        
        <hr><p><small>© 2026 SAYAM Consulting - sayamconsulting.com | Verified API: api.sayamconsulting.com | Contact: info@sayamconsulting.com</small></p>
    </body>
    </html>
    """

@app.get("/api/health")
def health():
    return {"status":"ok","version":"7.0 BRAND NEW","verified":True,"domain":"api.sayamconsulting.com","privacy":"https://api.sayamconsulting.com/privacy-policy","email":"info@sayamconsulting.com"}

# === CAREER DATA - 18 QUESTIONS ===
RIASEC_QUESTIONS = [
    {"id":1,"type":"R","text":"I enjoy repairing machines or building things with tools"},
    {"id":2,"type":"R","text":"I like working outdoors with plants or animals"},
    {"id":3,"type":"I","text":"I enjoy solving puzzles and analyzing problems"},
    {"id":4,"type":"I","text":"I like conducting experiments and research"},
    {"id":5,"type":"A","text":"I enjoy drawing, painting, or creative writing"},
    {"id":6,"type":"A","text":"I like playing music or performing on stage"},
    {"id":7,"type":"S","text":"I enjoy helping people with their problems"},
    {"id":8,"type":"S","text":"I like teaching or training others"},
    {"id":9,"type":"E","text":"I enjoy leading a team or managing projects"},
    {"id":10,"type":"E","text":"I like persuading people and selling ideas"},
    {"id":11,"type":"C","text":"I enjoy organizing files and data accurately"},
    {"id":12,"type":"C","text":"I like working with numbers and spreadsheets"},
    {"id":13,"type":"R","text":"I enjoy operating heavy equipment or vehicles"},
    {"id":14,"type":"I","text":"I like understanding how things work scientifically"},
    {"id":15,"type":"A","text":"I enjoy designing new things or decorating"},
    {"id":16,"type":"S","text":"I like working in a team to support community"},
    {"id":17,"type":"E","text":"I enjoy starting my own business or initiative"},
    {"id":18,"type":"C","text":"I like following clear rules and procedures"},
]

CAREER_MAP = {
    "R": ["Mechanical Engineer","Electrician","Civil Engineer","Pilot","Agriculture Officer"],
    "I": ["Scientist","Data Analyst","Doctor","Researcher","Software Engineer"],
    "A": ["Graphic Designer","Writer","Musician","Architect","Film Maker"],
    "S": ["Teacher","Counselor","Nurse","Social Worker","HR Manager"],
    "E": ["Entrepreneur","Marketing Manager","Lawyer","Sales Manager","CEO"],
    "C": ["Accountant","Bank Manager","Auditor","Data Entry","Administrator"]
}

PRICING = {"free":{"price":0,"reports":1,"careers":1},"premium":{"price":479,"currency":"INR","reports":"unlimited","careers":5,"upi":"mail2dms-1@okaxis"}}

@app.get("/api/questions")
def get_questions():
    return RIASEC_QUESTIONS

@app.get("/api/careers")
def get_careers():
    return CAREER_MAP

@app.get("/api/pricing")
def get_pricing():
    return PRICING

@app.post("/api/analyze")
def analyze(req: CounselingRequest):
    scores={"R":0,"I":0,"A":0,"S":0,"E":0,"C":0}
    for ans in req.answers:
        q=next((x for x in RIASEC_QUESTIONS if x["id"]==ans.question_id),None)
        if q:
            scores[q["type"]]+=ans.score
    top=sorted(scores.items(), key=lambda x:x[1], reverse=True)
    code="".join([k for k,v in top[:3]])
    limit=5 if req.plan=="premium" else 1
    recs=[]
    for k,v in top[:2]:
        recs.extend(CAREER_MAP.get(k,[])[:limit])
    return {
        "name":req.name,
        "riasec_code":code,
        "riasec_scores":scores,
        "top_traits":top[:3],
        "recommended_careers":recs[:limit],
        "plan":req.plan,
        "pricing":PRICING
    }

@app.delete("/api/user/delete")
def delete_user(email: str):
    return {"status":"deletion_requested","email":email,"contact":"info@sayamconsulting.com","message":"Data will be deleted in 7 days"}
