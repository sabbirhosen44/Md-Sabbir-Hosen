from database.models import ApiStatistic
from database.models import SearchHistory
from database.models import TravelDeal
from utils.response import api_response


# Get statistics of api
def get_api_statistics():
    stats = ApiStatistic.query.first()

    most_searched = SearchHistory.query.order_by(
        SearchHistory.search_count.desc()
    ).first()

    most_viewed = TravelDeal.query.order_by(TravelDeal.view_count.desc()).first()

    statistics_data = {
        "total_requests": stats.total_requests if stats else 0,
        "successful_requests": stats.successful_requests if stats else 0,
        "failed_requests": stats.failed_requests if stats else 0,
        "most_searched_destination": (
            most_searched.destination if most_searched else None
        ),
        "most_viewed_deal": most_viewed.to_dict() if most_viewed else None,
    }

    return api_response(
        success=True,
        message="Statistics retrieved successfully",
        data=statistics_data,
        status=200,
    )
