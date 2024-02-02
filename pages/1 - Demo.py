#Modules and Libraries for Smooth Functioning
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
#Importing BSE.py Function for interaction.
from BSE import market_session

def setup():
    st.markdown('''
                 ### <span style="color:green">Setup</span>
                 ''', unsafe_allow_html=True)
    
    st.code(''' 
        # Importing market_session from BSE.py for interaction.
        from BSE import market_session
        ''')
    
    with st.expander("market_session Function", expanded=False):
        st.markdown('''
                     The `market_session` function is imported from BSE.py and is used for interaction with the BSE market.
                     It has the following parameters:
                     - `trial_id`: The ID of the trial.
                     - `start_time`: The start time of the market session.
                     - `end_time`: The end time of the market session.
                     - `traders_spec`: Specification of traders in the market.
                     - `order_sched`: The order schedule for the market session.
                     - `dump_flags`: Flags for dumping market data.
                     - `verbose`: Flag for enabling verbose output.
                     ''', unsafe_allow_html=True)
    
    st.code('''
        # Example of market_session function
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        # Attribute definitions
        start_time=0
        # Experiment Lasts for 10 Minutes
        end_time=60*10
        # Order Schedule - includes supply schedule, demand schedule, interval, timemode
        # Supply Schedule - includes from time, to time, range, stepmode
        # Demand Schedule - includes from time, to time, range, stepmode
    
        # Based on Vernon Smith Experiment - 1962 JPE Paper - Range - (80,320)
        chart_range = (80, 320)
        # Defining Supply Schedule and Demand Schedule with fixed stepmode
        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
        # For order interval, we define it to be every 60 seconds.
        order_interval = 60
        # Time Mode - Periodic as used by Vernon Smith (start of each day)
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
       # Trader Type - ZIP, reasonaly human-like dynamics.
        sellers_spec = [('ZIP', 11)]
        # Buyer Spec = Seller Spec for consistency
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
        # Verbose - False to minimize text output (can be turned on however leads to large output)
        verbose = False
        # Dump Flags - Dumping market data
        # For BSE, files are written in CSV for later analysis, requiring a directory to be specified and a session identifier with dump_flags for specifiying the type of data to be dumped.
        tdump=open('data/demo/avg_balance.csv', 'w')
        trial_id = 'data/demo/demo_'
    ''')
    
    with st.expander("dump_flags attribute", expanded=False):
        st.markdown('''
                     The `dump_flags` attribute is imported from BSE.py and is used for interaction with the market_session.
                     It has the following options:
                        - `dump_blotters`: record the blotter(record of trades executed) for each trader
                        - `dump_lobs`: Dumping limit order book data.
                        - `dump_strats`: Dumping strategies data.
                        - `dump_avgbals`: Dumping average balance data.
                        - `dump_tape`: dump the tape (transactions only -- not writing cancellations)
                     ''', unsafe_allow_html=True)
    
    st.code('''
        # Example of dump_flags
        dump_flags = {'dump_blotters': True, 'dump_lob': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
        ''')


def one_one_market():
    st.markdown('''
                 ### <span style="color:green">1-Trader 1-Session Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    x = np.empty(0)
    y = np.empty(0)
    with open(prices_fname, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            time = float(row[1])
            price = float(row[2])
            x = np.append(x,time)
            y = np.append(y,price)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='1-Trader 1-Session Market')
    st.pyplot(fig, format='png', use_container_width=True)
    # st.pyplot(plt.savefig(sys.stdout.buffer), format='png', use_container_width=True)

def one_multi_market():
    st.markdown('''
                 ### <span style="color:green">1-Trade Multi-Session Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'data/demo/demo_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname =  trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='1-Trader Multi-Session Market')
    st.pyplot(fig, format='png', use_container_width=True)

def periodic_poisson_market():
    st.markdown('''
                 ### <span style="color:green">Periodic to Poisson Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'data/demo/demo_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='Periodic to Poisson Market')
    st.pyplot(fig, format='png', use_container_width=True)


def multi_multi_market():
    st.markdown('''
                 ### <span style="color:green">Multi-Trader Multi-Session Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    sellers_spec = [('ZIP', 40)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'data/demo/demo_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='Multi-Trader Multi-Session Market')
    st.pyplot(fig, format='png', use_container_width=True)

def multi_multi_type_market():
    st.markdown('''
                 ### <span style="color:green">Multi-Trader Multi-Session Multi-Type Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 1

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'data/demo/demo_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='Multi-Trader Multi-Session Multi-Type Market')
    st.pyplot(fig, format='png', use_container_width=True)

def shock_market():
    st.markdown('''
                 ### <span style="color:green">Shock Introduction Market</span>
                 ''', unsafe_allow_html=True)
    start_time=0
    end_time=60*10
    chart_range = (80, 320)
    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart_range], 'stepmode': 'fixed'}]
    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': 'periodic'}
    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}
    verbose = False
    tdump=open('data/demo/avg_balance.csv', 'w')
    trial_id = 'data/demo/demo_'
    dump_flags = {'dump_blotters': True, 'dump_lobs': False, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
    prices_fname = trial_id + '_tape.csv'
    shocked_range = (300, 400)
    shock_time = int(end_time / 2)

    supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart_range], 'stepmode':'fixed'},
                {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                ]
    demand_schedule = supply_schedule

    sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 1

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'data/demo/demo_' + str(sess)
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
        prices_fname = trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', color='black')
    ax.set(xlabel='Time', ylabel='Price', title='Shock Introduction Market')
    st.pyplot(fig, format='png', use_container_width=True)

def demo_simulator():
    st.markdown('''
                 ### <span style="color:green">Demo Simulator</span>
                 ''', unsafe_allow_html=True)
    
    st.write("Under Construction")

def main():
    st.title("Demo [BSE-S]")
    
    with st.expander("Information", expanded=False):
        st.markdown('''
                    
                    Demo of the BSE-S is based on <span style="text-decoration:underline"> Vernon Smith Experiment - 1962 JPE Paper</span>.
                    It showcases the following features:
                    - Setup BSE Market Sessions.
                    - Alteration and Extension to match real-world market scenarios.
                    - Introducing heterogeneous mix of trader-types.
                    - Simulating supply/demand assignments arriving randomly.
                    - Simulating supply/demand schedules altering during the session.
                    - Custom input simulation for Demo.
                    ''', unsafe_allow_html=True)


    st.divider()
    st.sidebar.subheader("Choose Step -")

    step_choice=st.sidebar.radio("", ["Setup", "1-Trader 1-Session Market", "1-Trade Multi-Session Market", "Periodic to Poisson Market", "Multi-Trader Multi-Session Market", "Multi-Trader Multi-Session Multi-Type Market", "Shock Introduction Market", "Demo Simulator"])

    if step_choice=="Setup":
        setup()
    elif step_choice=="1-Trader 1-Session Market":
        one_one_market()
    elif step_choice=="1-Trade Multi-Session Market":
        one_multi_market()
    elif step_choice=="Periodic to Poisson Market":
        periodic_poisson_market()
    elif step_choice=="Multi-Trader Multi-Session Market":
        multi_multi_market()
    elif step_choice=="Multi-Trader Multi-Session Multi-Type Market":
        multi_multi_type_market()
    elif step_choice=="Shock Introduction Market":
        shock_market()
    elif step_choice=="Demo Simulator":
        demo_simulator()





    



if __name__ == "__main__":
    main()
