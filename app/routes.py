from flask import render_template, request, jsonify, current_app as app
from .models import db, User, Waitlist
from .ai import predict_wait_time
from .notifications import send_notification

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkin', methods=['POST'])
def checkin():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    
    user = User(name=name, email=email, phone_number=phone_number)
    db.session.add(user)
    db.session.commit()

    ticket_number = Waitlist.query.count() + 1
    waitlist_entry = Waitlist(user_id=user.id, ticket_number=ticket_number)
    db.session.add(waitlist_entry)
    db.session.commit()

    return jsonify({'ticket_number': ticket_number})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('num_people')
    prediction = predict_wait_time(data)
    return jsonify({'prediction': prediction})

@app.route('/notify', methods=['POST'])
def notify():
    user_id = request.json.get('user_id')
    waitlist_entry = Waitlist.query.filter_by(user_id=user_id, status='waiting').first()

    if waitlist_entry:
        send_notification(waitlist_entry.user.phone_number, "Your number is about to be called. Please check in at the reception.")
        waitlist_entry.status = 'notified'
        db.session.commit()
    
    return jsonify({'message': 'Notification sent'})
