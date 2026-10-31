# MGT 656 Project Proposal

<!-- Before submitting: order the three ideas by team preference (1 = favorite). -->

## Idea 1: AI wedding planner (working name: I Do List)

**Tagline:** an AI wedding planner for couples planning without a human one.

### Major user journeys

- **As a newly engaged couple,** I sign up and fill out a short intake form:
  wedding date, city, budget, guest count, style and must-haves. I click
  "Make our plan" and get a dated checklist from now to the wedding day and a
  suggested budget split by category. I edit anything I don't like.
- **As a couple mid-planning,** I log in to a dashboard that shows what's due
  this month, budget spent vs. planned, and RSVPs so far. I mark "Book a
  photographer" done, add the photographer to my vendor list with their quote
  and deposit due date, and the budget updates.
- **As a couple managing guests,** I add households and their guests, then send
  each household its RSVP link. I watch responses and meal counts come in.
- **As a guest,** I open my household's RSVP link (no account needed), answer
  yes or no for each person, choose meals, and submit.

### Core features (MVP)

1. **Checklist and timeline:** tasks with due dates, categories and status, plus
   a "due this month" view.
2. **Budget tracker:** categories with planned vs. actual amounts and payment
   due dates.
3. **Guest list and RSVP:** households, guests, plus-ones and meal choices; a
   private RSVP link per household; a live headcount.
4. **Vendor tracker:** vendors the couple finds on their own, with contact info,
   quote, status (researching, booked) and deposits that feed the budget.

**What we'd skip:**

- A vendor directory, booking or payments. Couples add vendors they found
  themselves; the app tracks money but never moves it.
- Maps, venue search, and any third-party API other than OpenRouter.
- Chat and real-time collaboration. One shared login per couple in the MVP.
- Sending email. The couple shares RSVP links themselves.
- Seating charts, wedding websites and registries.

### AI feature

**The AI writes the plan.** The server sends the intake answers to an LLM
through OpenRouter and asks for JSON in a fixed schema: tasks (title, category,
weeks before the wedding) and a budget split (category, amount). The app
validates the JSON, checks that the budget lines add up, converts weeks into
real dates, and saves everything as ordinary tasks and budget lines the couple
can edit. The plan fits the couple: a six-month engagement gets a compressed
timeline, and a small budget drops the videographer. If the response fails
validation, the app retries once and then falls back to a standard template.
Tests mock the LLM.

### Why it's tractable

- A handful of related tables (weddings, tasks, budget lines, vendors,
  households, guests) edited through server-rendered forms. A good fit for
  Django or Rails with Postgres.
- The only outside service is OpenRouter.
- It leads naturally to technical-challenge items: structured LLM output that
  drives the app, an evaluation set for the plan generator, and later,
  scheduled reminder emails for upcoming tasks.

## Idea 2: TBD

**Tagline:**

### Major user journeys

### Core features (MVP)

**What we'd skip:**

### AI feature

## Idea 3: TBD

**Tagline:**

### Major user journeys

### Core features (MVP)

**What we'd skip:**

### AI feature
