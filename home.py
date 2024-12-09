import streamlit as st
import pandas as pd
import os

local_file_path = os.path.join("data", "sample_data.csv")
df = pd.read_csv(local_file_path)

df['CREATED'] = pd.to_datetime(df['CREATED'])
df['LAST_ALTERED'] = pd.to_datetime(df['LAST_ALTERED'])

def home():
    st.title('Hi, Andrea Gurnari!')

    def human_bytes(B):
        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        if B < KB:
            return '{0} {1}'.format(B, '')
        elif KB <= B < MB:
            return '{0:.2f}'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f}'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f}'.format(B / GB)
        elif TB <= B:
            return '{0:.2f}'.format(B / TB)

    def human_bytes_text(B):
        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        if B < KB:
            return 'Bytes'
        elif KB <= B < MB:
            return 'KB'
        elif MB <= B < GB:
            return 'MB'
        elif GB <= B < TB:
            return 'GB'
        elif TB <= B:
            return 'TB'

    def human_format(num):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return ('%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])).replace('.00', '')

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def remote_css(url):
        st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

    def header_bg(table_type):
        if table_type == "BASE TABLE":
            return "tablebackground"
        elif table_type == "VIEW":
            return "viewbackground"
        else:
            return "mvbackground"

    remote_css("https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css")
    local_css("style.css")

    table_scorecard = """
    <div class="ui five small statistics">
    <div class="grey statistic">
        <div class="value">""" + str(df[df['TABLE_TYPE'] == 'BASE TABLE']['TABLE_ID'].count()) + """
        </div>
        <div class="grey label">
        Tables
        </div>
    </div>
        <div class="grey statistic">
            <div class="value">""" + str(df[df['TABLE_TYPE'] == 'AUGMENTED TABLE']['TABLE_ID'].count()) + """
            </div>
            <div class="label">
            Augmented Tables
            </div>
        </div>
        <div class="grey statistic">
            <div class="value">""" + str(2656988) + """
            </div>
            <div class="label">
            Reasoning Steps
            </div>
        </div>    
    <div class="grey statistic">
        <div class="value">
        """ + human_format(df['ROW_COUNT'].sum()) + """
        </div>
        <div class="label">
        Rows
        </div>
    </div>

    <div class="grey statistic">
        <div class="value">
        """ + human_bytes(df['BYTES'].sum()) + " " + human_bytes_text(df['BYTES'].sum()) + """
        </div>
        <div class="label">
        Data Size
        </div>
    </div>
    </div>"""

    table_scorecard += """<br><br><br><div id="mydiv" class="ui centered cards">"""

    for index, row in df.iterrows():
        table_scorecard += """
    <div class="card"">   
        <div class=" content """ + header_bg(row['TABLE_TYPE']) + """">
                <div class=" header smallheader">""" + row['TABLE_NAME'] + """</div>
        <div class="meta smallheader">""" + row['TABLE_CATALOG'] + "." + row['TABLE_SCHEMA'] + """</div>
        </div>
        <div class="content">
            <div class="description"><br>
                <div class="column kpi number">""" + human_format(row['ROW_COUNT']) + """<br>
                    <p class="kpi text">Rows</p>
                </div>
                <div class="column kpi number">""" + human_bytes(row['BYTES']) + """<br>
                    <p class="kpi text">""" + human_bytes_text(row['BYTES']) + """</p>
                </div>
                <div class="column kpi number">""" + "{0:}".format(row['COLUMN_COUNT']) + """<br>
                    <p class="kpi text">Columns</b>
                </div>
            </div>
        </div>
        <div class="extra content">
            <div class="meta"><i class="table icon"></i> Table Type: """ + (row['TABLE_TYPE']) + """</div>
            <div class="meta"><i class="user icon"></i> Owner: """ + str(row['TABLE_OWNER']) + """ </div>
            <div class="meta"><i class="calendar alternate outline icon"></i> Created On: """ + (row['CREATED'].strftime("%Y-%m-%d")) + """</div>
        </div>
        <div class="extra content" style="display: none;"> 
            <div class="meta"><i class="history icon"></i> Time Travel: """ + str((row['RETENTION_TIME'])).strip(".0") + """</div>
            <div class="meta"><i class="edit icon"></i> Last Altered: """ + (row['LAST_ALTERED'].strftime("%Y-%m-%d")) + """</div>
            <div class="meta"><i class="calendar times outline icon"></i> Transient: """ + str(row['IS_TRANSIENT']) + """ </div>
            <div class="meta"><i class="th icon"></i> Auto Clustering: """ + str(row['AUTO_CLUSTERING_ON']) + """ </div>
            <div class="meta"><i class="key icon"></i> Clustering Key: """ + str(row['IS_TRANSIENT']) + """ </div>
            <div class="meta"><i class="comment alternate outline icon"></i> Comment: """ + str(row['IS_TRANSIENT']) + """ </div>
        </div>
    </div>"""

    st.markdown(table_scorecard, unsafe_allow_html=True)