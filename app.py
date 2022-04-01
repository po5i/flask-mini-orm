from __future__ import annotations
from datetime import datetime
from typing import Optional, TypedDict

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from flask_sqlalchemy.model import DefaultMeta
from werkzeug import Response


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

BaseModel: DefaultMeta = db.Model


class NotificationsModel(TypedDict):
    id: int
    description: Optional[str]
    email: str
    date: datetime
    url: Optional[str]
    read: bool


class Notifications(BaseModel):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(100))
    email = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    url = Column(String(200))
    read = Column(Boolean, default=False)

    def to_dict(self) -> NotificationsModel:
        return {
            "id": self.id,
            "email": self.email,
            "description": self.description,
            "date": self.date,
            "url": self.url,
            "read": self.read,
        }

    @classmethod
    def get_all(cls) -> list[Notifications]:
        return db.session.query(cls).all()

    @classmethod
    def get_unread(cls) -> list[Notifications]:
        return db.session.query(cls).filter(Notifications.read.is_(False)).all()


@app.route("/")
def index() -> Response:
    return jsonify({"hello": "world"})


@app.route("/notifications", methods=["GET", "POST"])
def notifications() -> Response:
    if request.method == "POST":
        new_notification = Notifications(
            **dict(request.form, date=datetime.fromisoformat(request.form["date"]))
        )
        db.session.add(new_notification)
        db.session.commit()

    notifications = Notifications.get_all()
    return jsonify([notification.to_dict() for notification in notifications])


@app.route("/notifications/unread")
def unread() -> Response:
    notifications = Notifications.get_unread()
    return jsonify([notification.to_dict() for notification in notifications])


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
