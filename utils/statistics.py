from database.db import db
from database.models import ApiStatistic
from database.models import SearchHistory
from utils.logger import logger


def get_statistics_row():
    stats = ApiStatistic.query.first()

    if stats:
        logger.info(
            f"Statistics row retrieved: Total={stats.total_requests}, Success={stats.successful_requests}"
        )
    else:
        logger.info("No statistics row found, creating new entry.")

    if not stats:
        stats = ApiStatistic()
        db.session.add(stats)
        db.session.commit()

    return stats


def increment_total_requests():
    stats = get_statistics_row()

    stats.total_requests += 1

    db.session.commit()


def increment_successful_requests():
    stats = get_statistics_row()

    stats.successful_requests += 1

    db.session.commit()


def increment_failed_requests():
    stats = get_statistics_row()

    stats.failed_requests += 1

    db.session.commit()


def track_destination_search(destination):
    history = SearchHistory.query.filter_by(destination=destination.lower()).first()

    if history:
        history.search_count += 1

    else:
        history = SearchHistory(
            destination=destination.lower(),
            search_count=1,
        )

        db.session.add(history)

    db.session.commit()
