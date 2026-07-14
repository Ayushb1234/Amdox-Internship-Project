from pathlib import Path

import streamlit as st


class Layout:

    @staticmethod
    def load_css():

        css = (

            Path(__file__)

            .parent.parent

            / "css"

            / "theme.css"

        )

        with open(

            css,

            encoding="utf-8"

        ) as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )