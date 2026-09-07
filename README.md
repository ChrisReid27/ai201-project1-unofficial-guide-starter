# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.
---
## Video Demo

https://drive.google.com/file/d/1AQyJyp9PsGilBTWvQcsEVkiwW2QwhuL-/view?usp=sharing
---

## Domain
My domain is where on Howard's campus and the surrounding DC area students can go to study. This would be useful because at some points in the day different spots might be better than others depending on if the students wants to just hang with peers, study, or work on group projects.
<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |Best Places To Study On Campus |Howard's student led newspaper detailing the different options of on-campus study spots. |https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/ |
| 2 |Seven Places to Study on Howard's Campus |Short student testimonies are given on a few different on-campus study and hangout spots. |https://thedig.howard.edu/all-stories/seven-places-study-howards-campus |
| 3 |Howard Founders Library |The Founders Library Main page with guide detailing facilities, quiet study zones, private desk availability, and historical archive spaces. |https://founders.howard.edu/ |
| 4 |Howard Business Library |Business Library Main page with info on facilities, operating hours, how to properly acess, and specialized research environment rules. |https://businesslibrary.howard.edu/ |
| 5 |r/Howard University - Where is a quiet place on campus that I can take a meeting uninterrupted |Thread about where on campus students could find a place to do online meetings without distractions |https://www.reddit.com/r/HowardUniversity/comments/1qjt4e2/where_is_a_quiet_place_on_campus_that_i_can_take/ |
| 6 |Louis Stokes Health Science Library About Page |Short overview of the Howard health science library including operating hours and location on campus. |https://hsl.howard.edu/library/about |
| 7 |Study and Remote Work Locations in DC |Spreadsheet detailing a selection of study spots around D.C., also including amenities like whether or not the spaces have free wifi and the like. |https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982 |
| 8 |r/washingtondc - Most beautiful places to study/read in DC? |A thread where people share the spots that they think are the most beautiful for studying or reading around the city. |https://www.reddit.com/r/washingtondc/comments/8rh2bj/most_beautiful_places_to_studyread_in_dc/ |
| 9 |r/washingtondc - Underrated study spots |A thread where people share what they consider niche study spots around D.C. |https://www.reddit.com/r/washingtondc/comments/1kggh4w/underrated_study_spots/ |
| 10 |r/washingtondc - Best Cafes in DC for working or studying? |A thread dedicated to specifically cafes around D.C. suitable for studying and getting work done. |https://www.reddit.com/r/washingtondc/comments/1521vi4/best_cafes_in_dc_for_working_or_studying/ |
---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
My final chunk size is *1000*. It used to be 1,100 but that less than recommended chunks.

**Overlap:**
My overlap size is *200* characters. It was 175, but I changed it to match the change I made for chunk size.

**Why these choices fit your documents:**
My documents are split in three main categories. These insclude journalistic rankings, online forum discussions (just Reddit basically), and official web pages (plus a collaborative spreadsheet). These documents aren't super wordy, so the chunks couldn't be too small, but because some were denser than others like the google sheets being more comprehensive versus some of the shorter reddit threads, the chunks had to be sizeable enough to fit complete thoughts.

**Final chunk count:**
The original chunk count was 39. After cleaning up the chunks and fixing some issues regarding the reddit sources not appearing in raw text (had to copy paste and manually edit) the chunk count was 45. Because I wanted to get near or over 50 I changed my chunk size and overlap values to their minimum and maximum that I allowed respectively (1000 for chunk size and 200 for overlap) which made it 49 overall. The final amount is *53* chunks after reorganizing the chunks that have data from my spreadsheet source to be formatted better for context to be handled easier by the system.

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

### 1. Seven Places to Study on Howard's Campus

```text
Emissary in DuPont.
When I’ve been (weekend) it’s soooo full. Also, some tables are cramped and it was pretty loud.
It’s usually crowded. There are no outlets except for one or maybe two in the back. The wifi sucks.
I would still go for evening cocktails or a date, but I'd never recommend it as a good place to work or study.
```

### 2. Howard Business Library

```text
Business Library
Welcome to the Howard University School of Business Library
Reserving a Study Space.
Book a meeting room for a group or sign up to use for private study. Each room can be used for 2 hours. Please see the staff at the service desk.
Library Hours
Business Library Hours
Monday - Thursday: 8am-10pm
Friday: 8am-5pm
Saturday: 9am-6pm
Sunday: 1pm-9pm
Undergraduate Library Hours
Monday – Thursday: 8:00 am – 10:00 pm
Friday: 8:00 am- 5:00 pm
Saturday: 9:00 am- 10:00 pm
Sunday: 1:30 pm-10:00 pm
```

### 3. Howard University Quiet Meeting Places

```text
Where is a quiet place on campus that I can take a meeting uninterrupted
8mo ago
doesn't the library have those rooms where groups meet to study?
maybe an area in blackburn (upstairs)?
but it really depends on the type of meeting as well as meeting logistics
oh, the school of b may have space...
Ok-Promise-7928
Original Poster
Interview:) do I need to reserve library rooms
Yes, through the website
miner hall can be pretty quiet
```

### 4. Study and Remote Work Locations in DC

```text
A Baked Joint | N | Plenty | Full Meal Options | Moderate | $$ | | Has baked goods from Baked & Wired (same owner)
Tryst | Y | Plenty | Light Fare | Moderate | $ | |
Emissary | Y | Plenty | Full Meal Options | Moderate | $$ | N | Feels like a French cafe. They have 1.5 hour table limits, as told by server in 2023
Compass Coffee | Y | Moderate | Light Fare | Loud | $ | | Lots of natural light, can get busy, roastery at this location is very loud
Jacob Coffee House | Y | Moderate | Breakfast/Lunch | Loud | $ | | very good bagel sandwiches, friendly staff. 9 tables and outdoor seating. natural light
```

### 5. Best Cafes in DC for Working or Studying

```text
Soho tea and coffee in dupont has lots of tables, wifi and is quiet, that’s my favorite. Emissary is also good but go to the 20st Street location, the one on P is really loud. Mt pleasant library is also great. Other faves around the city are lost sock in Takoma (no wifi though), dua coffee in mcpherson square, buna in petworth, and a baked joint (loud and no wifi though).
Dans Cafe
If you’re looking for quaint the Open City coffee shop in the National Cathedral is great. Barely crowded and has an amazing view if you sit on the porch. Feels like you’re in Europe
```

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2

**Production tradeoff reflection:**
If I was deploying this for real users and cost was a non issue I would have to weigh the tradeoff of context length and domain specific text. If I was to use voyage-3 or voyage 3 large, that model can tke in way more broad swaths of data from sources, so then I'd have to be more manual when thinking about context and having to narrow down data to relevant info for my domain instead of for example an entire reddit forum page rather than a thread.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**
What libraries would still be open around Howard's campus on weekends past 12:00 pm?
Top returned chunks:
- "Business Library Welcome to the Howard University School of Business Library Reserving a Study Space. Book a meeting room for a group or sign up to use for private study. Each room can be used for 2 hours. Please see the staff at the service desk. Library Hours Business Library Hours Monday - Thursday: 8am-10pm Friday: 8am-5pm Saturday: 9am-6pm Sun..."
Distance: 0.518931
Source: Howard Business Library
URL: https://businesslibrary.howard.edu/
Chunk ID: 0
- Top result: "Welcome to Founders Library Founders Library and the Wayne A.I. Frederick Undergraduate Library (UGL) Hours of Operation Monday – Thursday: 8:00 am – 10:00 pm Friday: 8:00 am – 5:00 pm Saturday: 9:00 am – 6:00 pm Sunday: 1:30 pm – 10:00 pm Library Resources Using the Library Howard University Libraries offer students, faculty, and staff access to a..."
Distance: 0.747356
Source: Howard Founders Library
URL: https://founders.howard.edu/
Chunk ID: 0
- Top result: "needing to focus completely on a project, and everywhere you turn, there is a social gathering on campus. The one place where you can escape the madness is located in the center of the Yard: Founders Library. This Howard landmark’s vast quiet spaces will keep you focused and diligent. Founders is the place to “lock-in.” Hours of operation: Monday t..."
Distance: 0.762434
Source: Best Places To Study On Campus
URL: https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/
Chunk ID: 1

Relevance explanation:
These chunks are relevant since they give operating hours, letting the users easily know when certain places would still be open post midday. All places listed are correctly listed as libraries that do exist on Howard's campus.

---

**Query 2:**
I have an online assignment due soon but I'm nowhere near the Howard Campus right now, where can I go in the city to work that has wifi I can use to submit this real quick?
Top returned chunks:
- Top result: "from another library in the WRLC consortium? Yes, you have study privileges and can check out materials from other WRLC consortium libraries that Howard University is affiliated with (see WRLC link). Some restrictions may apply, so we recommend you check with the library before you visit. You can also request that the book be delivered to the Healt..."
Distance: 1.031300
Source: Louis Stokes Health Science Library About Page
URL: https://hsl.howard.edu/library/about
Chunk ID: 13
- Top result: "Blue Bottle Coffee | wifi: Y | Seating: Plenty | Food: Light Fare | Noise: Quiet | cost: $$$ | Notes: Lots of natural light Source: Study and Remote Work Locations in DC | Place: The Wydown | wifi: N | Seating: Plenty | Food: Light Fare | Noise: Quiet | cost: $$ | Notes: Connected to hotel lobby with plenty of seating Source: Study and Remote Work ..."
Distance: 1.081531
Source: Study and Remote Work Locations in DC
URL: https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982
Chunk ID: 8
- Top result: "in DC | Place: Kaldi's Social House | wifi: Y | Seating: Plenty | Food: Full Meal Options | Noise: Loud | cost: $ | Notes: Wifi can be spotty. Lounge area upstairs available in the afternoons Source: Study and Remote Work Locations in DC | Place: Ebenezer's Coffeehouse | wifi: Y | Seating: Limited | Food: Light Fare | Noise: Moderate | cost: $ | No..."
Distance: 1.084333
Source: Study and Remote Work Locations in DC
URL: https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982
Chunk ID: 1

Relevance explanation: The top choice is relevant since it talks about the other libraries that Howard library facilites are connected to, that do not exist on campus but at other institutions. The user is not on Howard's campus so this can be helpful since you can study at any of the other D.C. collegiate libraries as long as they are in the WLRC group. The other two chunks are also relevant since they denote specific conditions of certain spots around D.C., not Howard specific, suited for what the user is looking for.

---

**Query 3:**
What do other students say about some of the study spaces at Howard?
Top returned chunks:
- Top result: "Seven Places to Study on Howard's Campus N'dia Webb (student contributor) Aug 12, 2022 2 minutes As the school year approaches, the time comes once again for students to choose where to study. But where does a student, especially a freshman, start to find that special place? We asked several students about their favorite place to crack open the boo..."
Distance: 0.597425
Source: Seven Places to Study on Howard's Campus
URL: https://thedig.howard.edu/all-stories/seven-places-study-howards-campus
Chunk ID: 0
- Top result: "Also known as “Stokes” Over his 30-year career, Rep. Louis Stokes increased funding to expand access to biomedical research for people of color. If you like places where you can whisper to your study buddy without feeling the shame of opening a bag of chips, you will love Louis Stokes Library. Down the street from Annex, sits this campus library wi..."
Distance: 0.768691
Source: Best Places To Study On Campus
URL: https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/
Chunk ID: 3
- Top result: "ports facilitate easy laptop computer use and data retrieval. There are 21 group- and single-study rooms in total: 11 small study rooms each have a table and 4 chairs; 8 Problem Based Learning rooms are furnished with a table, and seats 10. There are also two single-study rooms for students studying for their board exams. A whiteboard is mounted in..."
Distance: 0.841330
Source: Louis Stokes Health Science Library About Page
URL: https://hsl.howard.edu/library/about
Chunk ID: 4

Relevance explanation: The user asks what students say about some of the spots so the system brings up chunks from the journalistic sources that I have. They also all talk about different spots and how they might fit your needs which is what the user was trying to gauge.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

My system tells `openai/gpt-oss-120b` to use only the retrieved documents, not general knowledge or information from the linked URLs. It must output "Sorry, I don't have enough information on that." when the retrieved context is insufficient. Each retrieved chunk is labeled with a context number, title, URL, and chunk ID, and the model is instructed to cite those context numbers inline.

**How source attribution is surfaced in the response:**

The app appends a deterministic `Sources` section containing the exact titles and URLs for the retrieved chunks. Context citation numbers stay aligned with that list, they still stay aligned when multiple chunks come from one document.

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query: 
Where can I study in DC with Wi-Fi?"

Response:
You can study at any of the following DC locations that offer Wi‑Fi:

- Blue Bottle Coffee — Wi‑Fi Y, plenty of seating, natural light [2][3]  
- Georgetown University Library — Wi‑Fi Y, plenty of seating [2]  
- DAR Library — Wi‑Fi Y, plenty of seating [2]  
- Georgetown Public Library — Wi‑Fi Y, plenty of seating [2]  
- Library of Congress — Wi‑Fi Y, plenty of seating [3]  
- Three Fifty Bakery and Coffee Bar — Wi‑Fi Y, plenty of seating [3]  
- Big Bear Cafe — Wi‑Fi Y, plenty of seating [3]  
- Swing’s Coffee — Wi‑Fi Y, limited seating [4]  
- Bourbon Coffee — Wi‑Fi Y, moderate seating [4]  
- Solid State Books — Wi‑Fi Y, moderate seating [4]  
- Yoube Cafe — Wi‑Fi Y, moderate seating [4]  
- Kaldi’s Social House — Wi‑Fi Y, plenty of seating [4][5]  
- Ebenezer’s Coffeehouse — Wi‑Fi Y, limited seating [5]  
- Busboys and Poets — Wi‑Fi Y, plenty of seating [5]  
- Capital One Café — Wi‑Fi Y, plenty of seating [5]

Source attribution:
Sources:
- [1] Most beautiful places to study or read in DC — https://www.reddit.com/r/washingtondc/comments/8rh2bj/most_beautiful_places_to_studyread_in_dc/
- [2, 3, 4, 5] Study and Remote Work Locations in DC — https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982

---

**Grounded response 2**

Query:
"What libraries are open on weekends after noon?"

Response:
Answer:
The Howard University libraries that are open after noon on weekends are:

- **Howard Business Library** – open Saturday 9 a.m.–6 p.m. and Sunday 1 p.m.–9 p.m. [2]  
- **Undergraduate Library (UGL)** – open Saturday 9 a.m.–10 p.m. and Sunday 1:30 p.m.–10 p.m. [2]  
- **Founders Library (and the Wayne A.I. Frederick Undergraduate Library)** – open Saturday 9 a.m.–6 p.m. and Sunday 1:30 p.m.–10 p.m. [4]

Source attribution:
Sources:
- [1, 5] Best Places To Study On Campus — https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/
- [2] Howard Business Library — https://businesslibrary.howard.edu/
- [3] Seven Places to Study on Howard's Campus — https://thedig.howard.edu/all-stories/seven-places-study-howards-campus
- [4] Howard Founders Library — https://founders.howard.edu/

---

**Out-of-scope query**

Query:
"When can I watch spongebob?"

System response (refusal):
Sorry, I don't have enough information on that.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

My Streamlit interface in `streamlit_app.py` accepts a question and lets the user choose how many retrieved chunks to supply to `openai/gpt-oss-120b`, defaulting to top-k = 5. The `app.py` CLI can also be used to run the interface from a terminal.

**Output format:**

The output format is an `Answer` section with inline citations, and a `Sources` section that lists the titles of the supporting documents and their URLs. The Streamlit app runs on its default local port, `http://localhost:8501` (or `http://localhost:8502`).

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:**
"what places in dc are near to Howard where I can do an online meeting?"

> **System:**
You have several convenient options within a short walk of Howard University:
Howard Plaza Towers West – The building’s first‑floor study nooks have plenty of seating and outlets, making them ideal for a video call or online meeting [2].
Louis Stokes Health Science Library – Located at 501 W St NW (just a block or two from campus) and offers study space and parking nearby [3].
Kaldi’s Social House – A nearby café with Wi‑Fi (though spotty at times), plenty of seating, and a quieter lounge area in the afternoons [1].
Busboys and Poets – Offers Wi‑Fi, abundant seating, and power outlets under the tables, suitable for a meeting [1].
Capital One Café – Provides Wi‑Fi and plenty of seating for a casual online session [1].
Sources:
[1, 4] Study and Remote Work Locations in DC — https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982
[2] Best Places To Study On Campus — https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/
[3] Louis Stokes Health Science Library About Page — https://hsl.howard.edu/library/about
[5] Underrated study spots in DC — https://www.reddit.com/r/washingtondc/comments/1kggh4w/underrated_study_spots/

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|---|---|---|---|---|
| 1 | What libraries would still be open around Howard's campus on weekends past 12:00 pm? | The libraries that are open would include Founders (Saturdays and Sundays), Busineess Library (Saturdays and Sundays), Undergraduate Library (Saturdays and Sundays), and the Health Science Library (Saturdays and Sundays). | On Saturdays after 12 p.m., the Howard Business Library (9 a.m.–6 p.m.) [1], Founders Library (9 a.m.–6 p.m.) [2], and the Wayne A.I. Frederick Undergraduate Library (9 a.m.–10 p.m.) [2] are all open.<br><br>On Sundays after 12 p.m., the Business Library (1 p.m.–9 p.m.) [1], Founders Library (1:30 p.m.–10 p.m.) [2], and the Undergraduate Library/UGL (1:30 p.m.–10 p.m.) [1] remain open. | Relevant | Accurate |
| 2 | I have an online assignment due soon but I'm nowhere near the Howard Campus right now, where can I go in the city to work that has wifi I can use to submit this real quick? | Bourbon Coffee, Solid State Books, Yoube Cafe, Kaldi's Social House, Capitol One Cafe, Tynan Coffee and Tea, Compass Coffee, Grace Street Coffee, Panera Bread, Rue Cafe, Tryst, Jacob Coffee House, The Den - Politics and Prose, Boundary Stone, Kramerbooks & Afterwords Cafe, Library of Congress, and Three Fifty Bakery and Cofffee Bar. | You can work at a nearby public location that offers Wi‑Fi, such as the Georgetown University Library – it provides Wi‑Fi, plenty of seating and a quiet atmosphere, making it easy to finish and submit your assignment quickly【2】. Another good option is the Library of Congress, which also has Wi‑Fi, ample seating and a quiet setting【4】. Both are off‑campus and suitable for focused online work. | Relevant | Accurate |
| 3 | What do other students say about some of the study spaces at Howard? | Students at Howard have good things to say about the study spaces like how Abraham Cleveland of the class of '23 remarks that the Locke Hall Writing Center "has lots of natural lighting with a huge table that allows me to spread out my work." | Other students highlight several Howard study spots for their atmosphere and amenities. One freshman praised the first‑floor study rooms for their “designs of each room and the consistent quiet environment” that help her focus [1]. A political‑science senior noted that the Writing Center in Locke Hall “has lots of natural lighting with a huge table that allows me to spread out my work” [1]. An African‑American‑studies student said Founders Library is her favorite because it is “historic and sentimental…very easy for me to study there” [1]. | Relevant | Accurate |
| 4 | Any underrated or niche spots at Howard that I should know about whenever I want to go study in peace. | Sure, their are some underrated spots like Miner Hall or any building with a empty classroom since those have wifi, outlets, and A.C. | Howard’s campus actually has a few quieter, lesser‑known study areas you can use:<br><br>Louis Stokes Library – a campus library with both whisper‑quiet and talk‑friendly spaces, ideal for solo work or small‑group collaboration【3】.<br><br>Howard Plaza Towers, West – P‑42 – the largest study room in the building, offering plenty of space for private or group study sessions【3】.<br><br>Howard Plaza Towers, West – first‑floor study nooks – smaller, more private rooms with convenient outlets, perfect for focused work in a low‑traffic spot【3】.<br><br>These locations tend to be less crowded than the main library and provide a peaceful environment for studying. | Relevant | Accurate |
| 5 | Any outside study or lounge areas on campus where I can meet people? | Yes, there is the Caribbean tree on The Yard of Howard. Since it is on The Yard, students walking by is a common site meaning you can easily run into new people or people you know. | Sorry, I don't have enough information on that. | Off-target | Inaccurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
Any outside study or lounge areas on campus where I can meet people?

**What the system returned:**
Sorry, I don't have enough information on that.

**Root cause (tied to a specific pipeline stage):**
The issue stems from the retrieval stage. The Caribbean Tree information exists in my Seven Places to Study on Howard's Campus source, but the question has wording about outdoor lounges and meeting people that doesn't match the wording in the chunk closely enough. The system only passes the top five retrieved chunks to the model so the Caribbean Tree chunk wasn't even included in the top 5 chunks for generation context for this question. Also, the expected claim about students meeting or running into people is not directly from the document and more of an inference so the grounding instructions I put in made the model give the "Sorry" response instead of guessing.

**What you would change to fix it:**
I would improve the retrieval by adding more descriptive terms such as “social,” “outdoor,” “The Yard,” and “Caribbean Tree” to the source metadata or the query-processing step. This could also be done to many of the other sources so that the retrieval works better across the board and the "Sorry, no info" response can be avoided for actually relevant question.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Most of the specifications from `planning.md` stayed the same in execution. The ingestion (chunking and overlap), the embedding and retrieval, and top k values all stayed largely the same. It helped to ensure that my system followed the grounding requirements in the generation phase too, and also having multiple test questions on hand was greatly valued since there were many testing portions in each milestone involving testing queries.

**One way your implementation diverged from the spec, and why:**
The main differences from my specs were the changes in my chunking sizes and overlap values. They were originally 1,100 and 175 respectively, but to get closer to 50 chunks, I had to change the values to 1000 and 200 respectively which put me at 49 chunks overall. I then had to implement some changes concerning my document that was a spreadsheet, which led to chunk count being able to surpass 50, at 53 overall and that was my final amount. I also did not use Gradio in generation and interface phase. I did end up using a different LLM than I originally planned which was openai/gpt-oss-120b instead of OpenAI GPT-4o or meta-llama/llama-4-scout-17b-16e-instruct. Lastly I made it so that the embedding model I used is forced to the CPU to avoid a meta-tensor loading error which before I fixed it would show up before the grounding "Sorry, no info" response had a chance to print.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* I gave Copilot the planning.md architecture diagram for the interface and generation phase of the program.
- *What it produced:* Copilot produced code but it was implementing OpenAI GPT-4o which I didn't want to use.
- *What I changed or overrode:* I first overrode it to meta-llama/llama-4-scout-17b-16e-instruct which is what the project recommended for Groq. That was giving difficulties so I then changed it to openai/gpt-oss-120b which made the process work smoothly after that.

**Instance 2**

- *What I gave the AI:* Early on, I asked Copilot why my reddit forum sources after being converted to raw text were coming in blank. 
- *What it produced:* It produced a solution after diagnosing that reddit had blocks up on their servers so that scraping wouldn't go through. It suggested copying and pasting and that's what I did and it then said to clean out buttons, unecessary comments, ads, etc from the raw text to make it a pure Howard Study Spot document like the other sources.
- *What I changed or overrode:* I mainly did as it suggested, however, I kept in some information that I thought would be relevant for the system like certain OP usernames for attribution, and date tags because I thought receny or time of posting could be a relevant metric for the system when it answers certain questions.
