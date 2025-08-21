# Identifying the prospects of Momentum strategy for future use

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The Momentum strategy has long been a profitable quantitative strategy since the 20th century. However, its ability to generate alpha as decreased in the recent decades. Therefore, it is important to decide should the company continue to adopt this type of strategy or serach for newer options in order to create alpha.

## Stakeholder & User
The stakeholders are portfolio managers who currently utilizes momentum strategys in the trading market. The users are analysts who performs the trades and the PMs who are in charge of the whole portfolio.

## Useful Answer & Decision
Momentum strategies are usually traded monthly and that's the interval we will use for the backtesting.
If we see continues alpha generated from data in the past years, we can assume that momenum strategies are still profitable and continue to adopt this type of strategy.
Many decisions may change the outcome of the tests. For example, because we are trading large baskets of stocks, a change in the prediction of trading costs may well effect the profits. Also, the index we benchmark agains can have an effect in the final alpha generated.
We need to find out the proftability of Momentum in the currenty market. The data used should be recent but contain enough to discover trends. We need to check for alpha, volatility on a yearly basis.

## Assumptions & Constraints
<Bullets: data availability, capacity, latency, compliance, etc.>
WE work under the assumption that Major stocks in the US market have been well recorded data since the 21st century.
There is no limit to the capacity of stocks that may be traded.
The time lag is set to 3 hours after the data is published.

## Known Unknowns / Risks
<Bullets: what’s uncertain; how you’ll test or monitor>
We need to consider regime shifts and be careful not to use data from the last centuy.
It's important that we take account into random events that may have an effect on the outcome. For example, momentum strategy generally work well when the market is at least stable. The bear market caused by covid and subsequent events should be taken into consideration when deciding if momentum works.
The data gathered may not be accurate. At the least, most stock prices only show the closing price on a certain date and does not take into account the price shifts during that day.

## Lifecycle Mapping
Goal → Stage → Deliverable
Identifying problems and methods → Problem Framing & Scoping (Stage 01) → Scoping paragraph + persona/memo + project/ repo skeleton
Creating reproducible environemnt → Tooling Setup →  .env
Warm-up coding → Python Fundamentals → hw03_python_fundamentals.ipynb,d ata/processed/summary.csv

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates
