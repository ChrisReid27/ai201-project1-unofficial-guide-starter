# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

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
My chunk size is evenly in between 1000 and 1,200 characters at 1,100 characters (Aka in between 200-250 words). This ensures my chunks aren't too small but also not to big, I didn't want my chunks to exactly hit the minimum or max limit.

**Overlap:**
My overlap size is 175 characters. It's in the threshold that works best for my documents (150-200 or 30-40 words.)

**Why these choices fit your documents:**
My documents are split in three main categories. These insclude journalistic rankings, online forum discussions (just Reddit basically), and official web pages (plus a collaborative spreadsheet). These documents aren't super wordy, so the chunks couldn't be too small, but because some were denser than others like the google sheets being more comprehensive versus some of the shorter reddit threads, the chunks had to be sizeable enough to fit complete thoughts.

**Final chunk count:**
The original chunk count was 39. After cleaning up the chunks and fixing some issues regarding the reddit sources not appearing in raw text (had to copy paste and manually edit) the final chunk count is 45.

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 |Seven Places to Study on Howard's Campus |The Writing Center in Locke Hall
“The Writing Center has lots of natural lighting with a huge table that allows me to spread out my work.”
Founders Library
“My favorite place to study on campus is Founders Library! It’s historic and sentimental to me, so it’s very easy for me to study there.”
Stokes Health Sciences Library
“I like HSL because it's usually quiet and scarcely populated.” |
| 2 |Howard Business Library |Business Library
Welcome to the Howard University School of Business Library
Reserving a Study Space.
Book a meeting room for a group or sign up to use for private study. Each room can be used for 2 hours.

Business Library Hours
Monday - Thursday: 8am-10pm
Friday: 8am-5pm
Saturday: 9am-6pm
Sunday: 1pm-9pm

Undergraduate Library Hours
Monday - Thursday: 8:00 am - 10:00 pm
Friday: 8:00 am- 5:00 pm
Saturday: 9:00 am- 10:00 pm
Sunday: 1:30 pm-10:00 pm |
| 3 |Where is a quiet place on campus that I can take a meeting uninterrupted |Where is a quiet place on campus that I can take a meeting uninterrupted
doesn't the library have those rooms where groups meet to study?
maybe an area in blackburn (upstairs)?
but it really depends on the type of meeting as well as meeting logistics
Original Poster
Interview:) do I need to reserve library rooms
Yes, through the website
miner hall can be pretty quiet |
| 4 |Study and Remote Work Locations in DC |Tynan Coffee & Tea | Y | Moderate | Breakfast | Moderate | $
Compass Coffee | Y | Plenty | Light Fare | Moderate | $ | | There is a hidden nook towards the front and to the right, good for meetings
Grace Street Coffee | Y | Plenty | Light Fare | Moderate | $ | N | Feels like a French cafe
Panera Bread | Y | Plenty | Full Meal Options | Moderate | $ | | Right outside of Dupont Circle Metro stop, very quiet downstairs many outlets there |
| 5 |Best Cafes in DC for working or studying? |Emissary in DuPont.
When I’ve been (weekend) it’s soooo full. Also, some tables are cramped and it was pretty loud.
It’s usually crowded. There are no outlets except for one or maybe two in the back. The wifi sucks.
I would still go for evening cocktails or a date, but I'd never recommend it as a good place to work or study. |

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 2:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 3:**

Top returned chunks:
-
-
-

Relevance explanation:

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query:

Response:

Source attribution:

---

**Grounded response 2**

Query:

Response:

Source attribution:

---

**Out-of-scope query**

Query:

System response (refusal):

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

**Output format:**

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** 

> **System:** 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

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

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

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

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
