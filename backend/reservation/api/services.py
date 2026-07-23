# from reservation.models import Shift
# from datetime import datetime, timedelta, date


# def reservation_dates(self,reservation, start_date=None, end_date=None):
        
        
#     if reservation.checkin_date== reservation.checkout_date:
#         return [{
#             "date":reservation.checkin_date,
#             "shift":Shift.FULLDAY
#         }]
        
#     dates=[]
#     day_num = reservation.days_reservation 
        
#     if reservation.checkin_shift==Shift.DAY: 
#         dates.append({
#             "date":reservation.checkin_date,
#             "shift":Shift.FULLDAY
#         })
#     else:
#         dates.append({
#             "date":reservation.checkin_date,
#             "shift":Shift.NIGHT
#         })
            
#     for n in range(1, day_num + 1):
#         dates.append({
#             "date":reservation.checkin_date+timedelta(days=n),
#             "shift":Shift.FULLDAY
#         })
#     if reservation.checkout_shift==Shift.DAY:
#         dates[-1]['shift']=Shift.DAY
            
#     return dates
    
