from dataclasses import dataclass, field
from src.bootstrap.app_service import AppServices
from src.bootstrap.dashboard_data import DashboardData
from typing import Optional

@dataclass
class AppContext:
    services: Optional[AppServices] = None
    dashboard_data: DashboardData = field(default_factory=DashboardData)