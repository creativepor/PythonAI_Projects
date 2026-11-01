

import pandas as pd

agents = pd.DataFrame({
    "agent_id": ["A101", "A102", "A103", "A104", "A105", "A106", "A107", "A108"],
    "team": ["Billing", "Tech", "Billing", "Tech", "Onboarding", "Billing", "Tech", "Onboarding"],
    "tickets_closed": [42, 57, 35, 61, 29, 50, 44, 38],
    "satisfaction_pct": [88, 91, 79, 84, 93, 86, 76, 82],
})

print(agents)

qualified = agents.loc[agents["satisfaction_pct"] > 80]
ranking = qualified.sort_values(by=["team", "tickets_closed"], ascending=[True, False])

print(qualified)

print(ranking)
