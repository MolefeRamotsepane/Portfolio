from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='templates/static')

events = []


@app.route('/', methods=['GET', 'POST'])
def event_add():
    if request.method == 'POST':
        title = request.form.get('title')
        dscript = request.form.get('dscript')
        date = request.form.get('date')
        ticket_link = request.form.get('ticket_link')
        location = request.form.get('location')

        events.append({
            'title': title,
            'dscript': dscript,
            'date': date,
            'ticket_link': ticket_link,
            'location': location
        })

        return redirect(url_for('upcoming_events'))
    return render_template('event_add.html')


@app.route('/upcoming_events')
def upcoming_events():
    return render_template('upcoming_events.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)
