import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


class Charts:

    #########################################################
    # Line Chart
    #########################################################

    @staticmethod
    def line(
        data,
        x,
        y,
        title="",
        color=None
    ):

        fig = px.line(
            data,
            x=x,
            y=y,
            color=color,
            markers=True,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450,
            title_x=0.02,
            margin=dict(
                l=10,
                r=10,
                t=50,
                b=10
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Bar Chart
    #########################################################

    @staticmethod
    def bar(
        data,
        x,
        y,
        title="",
        color=None,
        text=None
    ):

        fig = px.bar(
            data,
            x=x,
            y=y,
            color=color,
            text=text,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450,
            title_x=0.02
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Horizontal Bar
    #########################################################

    @staticmethod
    def horizontal_bar(
        data,
        x,
        y,
        title=""
    ):

        fig = px.bar(
            data,
            x=x,
            y=y,
            orientation="h",
            text=x,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=500,
            title_x=0.02
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Pie Chart
    #########################################################

    @staticmethod
    def pie(
        data,
        names,
        values,
        title=""
    ):

        fig = px.pie(
            data,
            names=names,
            values=values,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Donut Chart
    #########################################################

    @staticmethod
    def donut(
        data,
        names,
        values,
        title=""
    ):

        fig = px.pie(
            data,
            names=names,
            values=values,
            hole=.5,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Area Chart
    #########################################################

    @staticmethod
    def area(
        data,
        x,
        y,
        title=""
    ):

        fig = px.area(
            data,
            x=x,
            y=y,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Scatter
    #########################################################

    @staticmethod
    def scatter(
        data,
        x,
        y,
        color=None,
        size=None,
        title=""
    ):

        fig = px.scatter(
            data,
            x=x,
            y=y,
            color=color,
            size=size,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Histogram
    #########################################################

    @staticmethod
    def histogram(
        data,
        x,
        title=""
    ):

        fig = px.histogram(
            data,
            x=x,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Box Plot
    #########################################################

    @staticmethod
    def box(
        data,
        x,
        y,
        title=""
    ):

        fig = px.box(
            data,
            x=x,
            y=y,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Treemap
    #########################################################

    @staticmethod
    def treemap(
        data,
        path,
        values,
        title=""
    ):

        fig = px.treemap(
            data,
            path=path,
            values=values,
            title=title
        )

        fig.update_layout(
            margin=dict(
                t=40,
                l=5,
                r=5,
                b=5
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    #########################################################
    # Gauge
    #########################################################

    @staticmethod
    def gauge(
        value,
        maximum,
        title=""
    ):

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=value,
                title={"text": title},
                gauge={
                    "axis": {
                        "range": [0, maximum]
                    }
                }
            )
        )

        fig.update_layout(
            height=350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )