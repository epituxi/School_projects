def initial():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year', 'Month', 'Start', 'Monthly', 'End',
                                                                           'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('', '', 'balance', 'Profit', 'balance',
                                                                           'Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('', '', e, e, e, e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1
    months = years * 12

    return initial_investment, annual_profit_percent, per_month_investment, years, annual_profit_multiplier, \
           monthly_profit_multiplier, months


def main():
    initial_investment, annual_profit_percent, per_month_investment, years, annual_profit_multiplier, \
    monthly_profit_multiplier, months = initial()

    balance_start = initial_investment
    monthly_profit = balance_start * monthly_profit_multiplier
    balance_end = balance_start + monthly_profit + per_month_investment

    cumulative_profits = 0

    for month in range(1, int(months) + 1):
        if int(month % 12) == 0:
            year = int(month % 12) + (month / 12)
        else:
            year = int(month / 12) + 1
        monthly_profit = balance_start * monthly_profit_multiplier
        cumulative_profits += monthly_profit
        balance_end = balance_start + monthly_profit + per_month_investment
        if balance_end > 0:
            print('{:>5.0f} | {:>5.0f} | {:10.2f} | {:10.2f} | {:10.2f} | {:10.2f}'.format(year, month - (year - 1) * 12,
                                                                                        balance_start,
                                                                                        monthly_profit, balance_end,
                                                                                        cumulative_profits))
            if month - (year - 1) * 12 == 12:
                print('-' * 65)
                balance_start = balance_end
            else:
                balance_start = balance_end  # Next period start position is current period end position
        else:
            print('')
            print("Stopped printing as balance cannot go negative.")
            print('{:<20s} {:>9.2f} eur'.format('End balance:', balance_start))
            print('{:<20s} {:>9.2f} eur'.format('Total profit:', cumulative_profits - monthly_profit))
            print('{:<20s} {:>9.2f} eur'.format('Total net deposit:', balance_start - cumulative_profits + monthly_profit))
            break
    else:
        print('')
        print('{:<20s} {:>9.2f} eur'.format('End balance:', balance_end))
        print('{:<20s} {:>9.2f} eur'.format('Total profit:', cumulative_profits))
        print('{:<20s} {:>9.2f} eur'.format('Total net deposit:', balance_end - cumulative_profits))


main()
