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

## Idea 2: Yale RideShare

**Tagline:** a ride board for Yale students sharing trips between New Haven and
New York, especially to and from the airports.

### Major user journeys

- **As a rider,** I log in with my Yale email and enter where I'm leaving from,
  where I'm going, and the date. I get a list of matching trips. Each one shows
  the departure time, seats left (or how many co-riders the poster wants),
  whether it's an Uber, a rental, or the poster's own car, the make and model if
  it's their car, and the price per person. I pick one and message the poster to
  sort out pickup.
- **As a trip organizer,** I log in and post my trip: start, destination, date
  and time, how I'm going (my car, a rental, or an Uber I want to split), car
  details if it's mine, number of seats, and price per seat. Riders find my trip
  in search and message me. I mark seats as filled when people confirm, and the
  trip comes off the board once it's full or has left.
- **As a confirmed rider,** I pay my share in the app with a credit card, debit
  card, PayPal, or bank account.
- **As a student flying out of JFK with no plan yet,** I enter where I am and
  where I need to end up. The app tells me the best way to get there using the
  rides posted right now, for example a seat in a car going to Manhattan that
  afternoon plus how to cover the last stretch.
- **As someone who makes the same trip often,** I save my usual route (say, Yale
  to LaGuardia) and get an email each morning with the trips posted for it.

### Core features (MVP)

1. **Trip posting and search:** post a trip, and search by start, destination,
   and date.
2. **Messaging:** inbox-style messages between a rider and the trip poster.
3. **Payments:** riders pay their share by credit card, debit card, PayPal, or
   bank account.
4. **Car rental search:** for organizers who want to rent, show rental options
   for their date and pickup location.
5. **AI trip planner and daily digest** (below).

**What we'd skip:** cryptocurrency payments, driver ratings and reviews, live
GPS tracking, and a native mobile app.

### AI feature

- **Trip planner:** the user enters a starting point and final destination. The
  app sends the LLM the trips currently posted that could help (matching or
  nearby endpoints, close departure times), and the LLM writes back a short
  recommendation: which ride to join and how to handle any leg the posted rides
  don't cover.
- **Daily digest:** each morning, for users with a saved route, the LLM turns
  that day's matching trips into a short email listing what's available.

## Idea 3: Travel AIgent

**Tagline:** an AI-powered travel agent that creates personalized itineraries
and books your entire trip, excluding flights.

### Major user journeys

- **As a traveler,** I enter my destination, dates, budget, and interests. I
  receive a personalized itinerary, review suggested hotels and activities, and
  confirm bookings.
- **As a traveler,** I modify my itinerary, swap activities, or adjust my
  budget, and the agent updates my trip accordingly.
- **As an admin,** I manage hotel and activity listings, monitor bookings, and
  resolve booking issues.

### Core features (MVP)

1. **Profiles:** user profiles and trip preference collection.
2. **Itinerary planning:** itinerary creation and day-by-day trip planning.
3. **Hotel and activity search:** listings with pricing and availability.
4. **Bookings:** booking confirmation and centralized trip management.
5. **Editing and budget:** itinerary editing and budget tracking.

**What we'd skip:** flight bookings, complex payment processing, multi-user
collaboration, and a native mobile app.

### AI feature

An LLM-powered travel agent that generates personalized itineraries based on
user preferences, budget, and destination. It recommends relevant hotels and
activities, optimizes the itinerary by location and timing, and adapts plans
based on user feedback.
