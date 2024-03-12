from django.shortcuts import render, redirect
from college_admin.models import *
from User.models import *
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from pymongo import *
from faculty.utils import *
from django.contrib import messages
import time
from io import BytesIO

current_time = time.localtime()
current_datetime = datetime.fromtimestamp(time.mktime(current_time))
formatted_date = current_datetime.strftime("%Y-%m-%d")


def Add_Attendance_to_postgres(date):
    data = FetchColumn("attendance_system", "en_no")
    print(data)
    for en in data:
        attendance_data = register.objects.get(en_no=en[0]).attended
        row_column(attendance_data, en[0], date)


def set_false_after_delay():
    SetFalse()


def F_home(request):
    data = register.objects.values("en_no", "name", "attended")
    date = ""
    context = {
        "page": "Faculty",
        "data": data,
        "current_datetime": current_datetime,
    }
    # DropTable('attendance_system')
    # *****************************Add data to postgres************************************************
    # if data:
    #     AddData(data)
    # MakePK('attendance_system','en_no') # private key
    # ***************************************************************************************
    # DropColumn('attendance_system','en_no')
    # Truncate_column('attendance_system',"en_no")
    if request.method == "POST":
        date = request.POST.get("date")
        if not date:
            messages.success(request, "Please enter Date")
            context.update({"color": "danger"})
            return render(request, "F_index.html", context)

        # *****************************content for postgresql only**********************************
        # CreateColumn('attendance_system','en_no','TEXT')
        # CreateColumn('attendance_system','name','TEXT')
        if date:
            CreateColumn("attendance_system", date, "BOOLEAN")
            try:
                Add_Attendance_to_postgres(date)
            except Exception as e:
                print(e)
            # threading.Timer(60, set_false_after_delay).start()
    # ***************************************************************************************
    return render(request, "F_index.html", context)


def download_excel_data(request):
    query = "SELECT * FROM attendance_system"
    data_frame = fetch_data_from_postgres(db_params, query)
    excel_data = BytesIO()
    data_frame.to_excel(excel_data, index=False, engine="openpyxl")
    excel_data.seek(0)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f"attachment; filename={formatted_date}.xlsx"
    response.write(excel_data.read())

    return response


def empty_db(request):
    try:
        register.objects.all().update(attended=False)
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, "cap_images")
        print(file_path)

        if os.path.exists(file_path):
            for img in os.listdir(file_path):
                img_path = os.path.join(file_path, img)

                with open(img_path, "rb") as f:
                    pass

                try:
                    os.remove(img_path)
                    print(f"File {img_path} removed successfully.")
                except Exception as remove_error:
                    print(f"Error removing file {img_path}: {str(remove_error)}")
        else:
            print(f"Directory {file_path} does not exist.")

        messages.success(request, "All Registered students are set to False.")
    except Exception as e:
        messages.error(request, f"Error clearing database: {str(e)}")

    return redirect("F_home")
