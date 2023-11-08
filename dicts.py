dividends = {
    'title':'dividends',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Dividends per share(FY)':'dps_common_stock_prim_issue_fy',
    'Dividends per share(FQ)':'dps_common_stock_prim_issue_fq',
    'Dividend yield %(TTM)':'dividends_yield_current',
    'Dividend yield FWD %':'dividends_yield',
    'Payout ratio %(TTM)':'dividend_payout_ratio_ttm',
    'Dividends per share growth %(Annual YoY)':'dps_common_stock_prim_issue_yoy_growth_fy',
    'Continuous dividend payout':'continuous_dividend_payout',
    'Continuous dividend growth':'continuous_dividend_growth'}


performance = {
    'title':'performance',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Price':'close',
    'Change % 1D':'change',
    'Performance % 1W':'Perf.W',
    'Performance % 1M':'Perf.1M',
    'Performance % 3M':'Perf.3M',
    'Performance % 6M':'Perf.6M',
    'Performance % YTD':'Perf.YTD',
    'Performance % 1Y':'Perf.Y',
    'Performance % 5Y':'Perf.5Y',
    'Performance % All Time':'Perf.All',
    'Volatility 1W':'Volatility.W',
    'Volatility 1M':'Volatility.M',
   
    
    
}



valuation = {
    
    'title':'valuation',    
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Market cap':'market_cap_basic',
    'Market cap perf % 1Y':'Perf.1Y.MarketCap',
    'P/E':'price_earnings_ttm',
    'PEG (TTM)':'price_earnings_growth_ttm',
    'P/S':'price_sales_current',
    'P/B':'price_book_fq',
    'P/CF':'price_to_cash_f_operating_activities_ttm',
    'P/FCF':'price_free_cash_flow_ttm',
    'P/C':'price_to_cash_ratio',
    'EV':'enterprise_value_current',
    'EV / revenue (TTM)':'enterprise_value_to_revenue_ttm',
    'EV / EBIT (TTM)':'enterprise_value_to_ebit_ttm',
    'EV / EBITDA (TTM)':'enterprise_value_ebitda_ttm',
    
}


dividends = {
    
    'title':'dividends',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Dividends per share (FY)':'dps_common_stock_prim_issue_fy',
    'Dividends per share (FQ)':'dps_common_stock_prim_issue_fq',
    'Dividend yield % (TTM)':'dividends_yield_current',
    'Dividend yield FWD %':'dividends_yield',
    'Payout ratio % (TTM)':'dividend_payout_ratio_ttm',
    'Dividends per share growth % (Annual YoY)':'dps_common_stock_prim_issue_yoy_growth_fy',
    'Continuous dividend payout':'continuous_dividend_payout',
    'Continuous dividend growth':'continuous_dividend_growth',
       
    
}


profitability = {
    'title':'profitability',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Gross margin % (TTM)':'gross_margin_ttm',
    'Operating margin % (TTM)':'operating_margin_ttm',
    'Pretax margin % (TTM)':'pre_tax_margin_ttm',
    'Net margin % (TTM)':'net_margin_ttm',
    'Free cash flow margin % (TTM)':'free_cash_flow_margin_ttm',
    'ROA % (TTM)':'return_on_assets_fq',
    'ROE % (TTM)':'return_on_equity_fq',
    'ROIC % (TTM)':'return_on_invested_capital_fq',
    'R&D ratio (TTM)':'research_and_dev_ratio_ttm',
    'SG&A ratio (TTM)':'sell_gen_admin_exp_other_ratio_ttm'
                }


incomeStatement = {
    'title':'incomestatement',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'Revenue (TTM)' : 'total_revenue_ttm',
    'Revenue growth % (TTM YoY)':'total_revenue_yoy_growth_ttm',
    'Gross profit (TTM)': "gross_profit_ttm",
    'Operating income (TTM)': 'oper_income_ttm',
    'Net income (TTM)' : 'net_income_ttm',
    "EBITDA (TTM)":'ebitda_ttm',
    'EPS Diluted (TTM)' : 'earnings_per_share_diluted_ttm',
    'EPS Diluted% (TTM YoY)' : 'earnings_per_share_diluted_yoy_growth_ttm'}


balanceSheet = {
                'title':'balancesheet',
                'Name':'description',
                'Currency':'fundamental_currency_code',
                'Assets (FQ)':'total_assets_fq',
                'Current assets (FQ)':'total_current_assets_fq',
                'Cash on hand (FQ)': 'cash_n_short_term_invest_fq',
                'Liabilities (FQ)':'total_liabilities_fq',
                'Debt (FQ)': 'total_debt_fq',
                'Net debt (FQ)': 'net_debt_fq',
                'Equity':'total_equity_fq',
                'Current ratio (FQ)':'current_ratio_fq',
                'Quick ratio (FQ)':'quick_ratio_fq',
                'Debt / equity (FQ)':'debt_to_equity_fq',
                'Cash / debt (FQ)':'cash_n_short_term_invest_to_total_debt_fq'
               }


cashFlow = {
    
    'title':'cashflow',
    'Name':'description',
            'Currency':'fundamental_currency_code',
            'Operating CF (TTM)':'cash_f_operating_activities_ttm',
            'Investing CF (TTM)':'cash_f_investing_activities_ttm',
            'Financing CF (TTM)':'cash_f_financing_activities_ttm',
           'Free cash flow (TTM)':'free_cash_flow_ttm',
            'CAPEX (TTM)': 'capital_expenditures_ttm'
           }


oscillators = {
    
    'title':'oscillators',
    'Name':'description',
    'Oscillators Rating 1D':'Recommend.Other',
    'RSI (14) 1D':'RSI',
    'Momentum (10) 1D':'Mom',
    'Awesome Oscillator 1D':'AO',
    'Commodity Channel Index (20) 1D':'CCI20',
    'Stochastic (14,3,3) 1D %K':'Stoch.K',
    'Stochastic (14,3,3) 1D %D':'Stoch.D',
    'MACD (12,26) 1D Level' : 'MACD.macd',
    'MACD (12,26) 1D Signal':'MACD.signal'
              }


trendFollowing = {
    
    'title':'trendfollowing',
    'Name':'description',
    'Currency':'fundamental_currency_code',
    'MA Rating 1D':'Recommend.MA',
    'Price':'close',
    'Moving Average (20) 1D':'SMA20',
    'Moving Average (50) 1D':'SMA50',
    'Moving Average (200) 1D':'SMA200',
    'Bollinger Bands (20) 1D Upper':'BB.upper',
    'Bollinger Bands (20) 1D Lower':'BB.lower',

    
}

dictsList = [performance, dividends, oscillators, cashFlow, trendFollowing,incomeStatement , balanceSheet, valuation]