import streamlit as st


def main():
    st.subheader("Introduction")
    st.write("This is a simple simulation of a stock exchange. The simulation is based on the Bristol Stock Exchange (BSE) which is a fully electronic order-driven trading system.")
    st.write(" The BSE is a simulation of a real stock exchange and is used by the University of Bristol for research and teaching. The BSE is a continuous double auction market, meaning that orders are matched continuously throughout the trading day.")
    st.write(" The BSE is a fully electronic system, meaning that all orders are submitted electronically and there is no physical trading floor.")

if __name__ == "__main__":
    main()
