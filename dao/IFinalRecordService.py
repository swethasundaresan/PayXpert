from entity import FinancialRecord
from typing import List
import datetime


class IFinalRecordService:
    def add_financial_record(self,RecordID:int, employee_id: int, record_date: datetime.date, description: str, record_type: str) -> None:
        raise NotImplementedError("Method not implemented")

    def get_financial_record_by_id(self, record_id: int) -> FinancialRecord:
        raise NotImplementedError("Method not implemented")

    def get_financial_records_for_employee(self, employee_id: int) -> List[FinancialRecord]:
        raise NotImplementedError("Method not implemented")

    def get_financial_records_for_date(self, record_date: datetime.date) -> List[FinancialRecord]:
        raise NotImplementedError("Method not implemented")
