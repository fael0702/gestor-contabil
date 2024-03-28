from sqlalchemy.orm import Session
from app.entities.revenue import RevenueDb


def create_revenue_db(new_revenuer: RevenueDb, db: Session):
    db.add(new_revenuer)
    db.commit()
    db.refresh(new_revenuer)
    return new_revenuer
