# Compare 5-year TCO: Off-the-Shelf vs. Custom Software
#
# Author: Savant Realms
# Website: savantrealms.com
# Date: 2025-06-01

import math

def npv(cash_flows, discount_rate):
    return sum(cf / ((1 + discount_rate) ** year) for year, cf in enumerate(cash_flows))

def build_off_the_shelf_costs(init_sub, sub_growth, setup_fee, init_cust, cust_growth, years):
    flows = [setup_fee + init_sub + init_cust]  # Year 0
    sub, cust = init_sub, init_cust
    for _ in range(1, years):
        sub *= (1 + sub_growth)
        cust *= (1 + cust_growth)
        flows.append(sub + cust)
    return flows

def build_custom_costs(dev_cost, host_monthly, host_growth, maint_rate, years):
    flows = [dev_cost + host_monthly * 12]  # Year 0
    host_annual = host_monthly * 12
    for _ in range(1, years):
        host_annual *= (1 + host_growth)
        flows.append(host_annual + dev_cost * maint_rate)
    return flows

def main():
    # Off-the-Shelf parameters
    init_sub = 10000           # Year-1 subscription
    sub_growth = 0.05          # 5% yearly increase
    setup_fee = 1000           # One-time setup
    init_cust = 2000           # Year-1 customization
    cust_growth = 0.05         # 5% yearly increase

    # Custom Development parameters
    dev_cost = 20000           # Initial build cost
    host_monthly = 500         # Hosting per month Year-1
    host_growth = 0.03         # 3% yearly increase
    maint_rate = 0.20          # 20% of dev_cost per year

    discount_rate = 0.05       # 5% annual discount rate
    years = 5

    ots_flows = build_off_the_shelf_costs(init_sub, sub_growth, setup_fee, init_cust, cust_growth, years)
    custom_flows = build_custom_costs(dev_cost, host_monthly, host_growth, maint_rate, years)

    ots_npv = npv(ots_flows, discount_rate)
    custom_npv = npv(custom_flows, discount_rate)

    print(f"{'Year':<6}{'Off-the-Shelf':>18}{'Custom':>15}")
    print("-" * 40)
    for i in range(years):
        print(f"{i:<6}{ots_flows[i]:>18,.0f}{custom_flows[i]:>15,.0f}")

    print("\nNPV (5-Year Total):")
    print(f"  Off-the-Shelf:   ${ots_npv:,.0f}")
    print(f"  Custom Software: ${custom_npv:,.0f}")
    diff = abs(ots_npv - custom_npv)
    if ots_npv < custom_npv:
        print(f"\n=> Off-the-Shelf is cheaper by ${diff:,.0f}")
    else:
        print(f"\n=> Custom Software is cheaper by ${diff:,.0f}")

if __name__ == "__main__":
    main()
