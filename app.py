# previous
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chart():
    if request.method == 'POST':
        # Check which form was submitted
        if 'form1' in request.form:
            # Get the updated sizes from the first form
            sizes = [float(request.form.get('size1')),
                     float(request.form.get('size2')),
                     float(request.form.get('size3')),
                     float(request.form.get('size4')),
                     float(request.form.get('size5'))]

            labels = ['100 Seater', '70 Seater', '30 Seater', '17 Seater', 'Taxi']

            # Create a pie chart
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%')
            ax.set_title('Bus Types', pad=30)
            ax.axis('equal')
            ax.legend(labels, loc='upper right', bbox_to_anchor=(1, 0.5), bbox_transform=plt.gcf().transFigure)

        elif 'form2' in request.form:
            # Get the updated sizes from the second form
            sizes = [float(request.form.get('operational')),
                     float(request.form.get('repairing')),
                     float(request.form.get('waiting')),
                     float(request.form.get('decommissioned'))]

            labels = ['Operational', 'Repairing', 'Waiting', 'Out of service']

            # Create a pie chart
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%')
            ax.set_title('Bus Conditions', pad=30)
            ax.axis('equal')
            ax.legend(labels, loc='upper right', bbox_to_anchor=(1, 0.5), bbox_transform=plt.gcf().transFigure)

    else:
        # Data for the initial pie charts
        sizes1 = [12, 19, 30, 7, 21]  # Values representing the size of each slice
        labels1 = ['100 Seater', '70 Seater', '30 Seater', '17 Seater', 'Taxi']

        sizes2 = [30, 13, 2, 5]  # Values representing the size of each slice
        labels2 = ['Operational', 'Repairing', 'Waiting', 'Out of service']

        # Create initial pie charts
        fig, (ax1, ax2) = plt.subplots(1, 2)

        ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%')
        ax1.set_title('Bus Types', pad=30)
        ax1.axis('equal')
        ax1.legend(labels1, loc='upper right', bbox_to_anchor=(1, 0.5), bbox_transform=plt.gcf().transFigure)

        ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%')
        ax2.set_title('Bus Conditions', pad=30)
        ax2.axis('equal')
        ax2.legend(labels2, loc='upper right', bbox_to_anchor=(1, 0.5), bbox_transform=plt.gcf().transFigure)

    # Save the chart to a binary buffer
    chart_buffer = io.BytesIO()
    plt.savefig(chart_buffer, format='png')
    chart_buffer.seek(0)

    # Encode the chart image as base64
    chart_base64 = base64.b64encode(chart_buffer.read()).decode('utf-8')

    return render_template('dashboard.html', chart_base64=chart_base64)

if __name__ == '__main__':
    app.run(debug=True)