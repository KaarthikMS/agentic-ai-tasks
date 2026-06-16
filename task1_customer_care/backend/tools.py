from strands import tool


@tool
def check_order_status(order_id: str):
    """
    Check the status of an order.

    Args:
        order_id: Customer order id

    Returns:
        Dictionary containing order status
    """

    mock_orders = {

        "123": "Shipped",

        "456": "Out for delivery",

        "789": "Delivered"

    }

    status = mock_orders.get(
        order_id,
        "Order not found"
    )

    return {

        "order_id": order_id,

        "status": status

    }


@tool
def create_support_ticket(issue: str):
    """
    Create a support ticket.

    Args:
        issue: Customer complaint

    Returns:
        Ticket details
    """

    return {

        "ticket_id": "TKT001",

        "issue": issue,

        "status": "Created"

    }