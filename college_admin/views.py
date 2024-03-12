from django.shortcuts import render, redirect
from college_admin.utils import *
from django.contrib import messages
from college_admin.models import *
import imghdr as im


# data = [{'20BEIT30009': 'BALAT DHYEY'}, {'21BEIT30001': 'AMIN DHVANI KEVALBHAI'}, {'21BEIT30002': 'ARAB AYESHA ABDUL RASHID'}, {'21BEIT30003': 'Bhalala Aditi Bhaveshbhai'}, {'21BEIT30004': 'Bhalodiya Harshkumar Hasmukhbhai'}, {'21BEIT30005': 'Patel Kanvi Bharatkumar'}, {'21BEIT30006': 'BOGHRA MANAV ARVINDBHAI'}, {'21BEIT30007': 'BORAD TEESA JAYESHBHAI'}, {'21BEIT30008': 'CHAHWALA SMIT MITESHKUMAR'}, {'21BEIT30009': 'CHAUDHARI JEEL KIRIRTKUMAR'}, {'21BEIT30010': 'CHAUDHARI OM MAULIKKUMAR'}, {'21BEIT30011': 'Chaudhari sonalben shankarbhai'}, {'21BEIT30012': 'CHAUDHARI YASH DILIPKUMAR'}, {'21BEIT30013': 'CHAUDHARY FALGUNI DALASANGBHAI'}, {'21BEIT30014': 'CHAUDHARY RAHI HASMUKHBHAI'}, {'21BEIT30016': 'CHAUHAN CHINTANSINH VIJAYSINH'}, {'21BEIT30017': 'CHAUHAN JAYKUMAR HITENDRAKUMAR'}, {'21BEIT30018': 'Desai Maulin Kanubhai'}, {'21BEIT30019': 'DHARAJIYA VIKASKUMAR HITESHBHAI'}, {'21BEIT30020': 'Dholakiya Hastiben Prakashbhai'}, {'21BEIT30021': 'DOBARIYA SNEHAL PRAKASHBHAI'}, {'21BEIT30022': 'DOSHI HARDI MEHULKUMAR'}, {'21BEIT30023': 'GAJERA MEETKUMAR ASHOKBHAI'}, {'21BEIT30024': 'GAJJAR ANMOL BHAVESHKUMAR'}, {'21BEIT30025': 'GAJJAR JUHI HASMUKHBHAI'}, {'21BEIT30026': 'Gandhi Khushi Rupeshkumar'}, {'21BEIT30027': 'Goswami Bhaumikkumar Sureshpuri'}, {'21BEIT30028': 'Goswami Princepuri Ashokpuri'}, {'21BEIT30029': 'GOTHI HARITABEN ANILBHAI'}, {'21BEIT30030': 'Joshi kandarp shaileshbhai'}, {'21BEIT30031': 'Kalal lalit'}, {'21BEIT30032': 'Kalariya Parth Rohitbhai'}, {'21BEIT30033': 'Kalariya Prince Hiteshbhai'}, {'21BEIT30034': 'KANJARIYA HARDIK BHARATBHAI'}, {'21BEIT30035': 'Kaurani Divya Dinesh'}, {'21BEIT30036': 'KAVAR DEVKUMAR TUSHARBHAI'}, {'21BEIT30037': 'KHAGAD VISHAL BHAVANBHAI'}, {'21BEIT30038': 'KHANDALA HARDIK NATVARBHAI'}, {'21BEIT30039': 'KHUNT PARTH CHATURBHAI'}, {'21BEIT30040': 'KORAT RAJ ARAVINDBHAI'}, {'21BEIT30041': 'KOTADIYA HARSHKUMAR ASHOKBHAI'}, {'21BEIT30042': 'KOTHARI MIHIR DINESHKUMAR'}, {'21BEIT30043': 'KUNDALIA HARSH HEMAL'}, {'21BEIT30044': 'LADANI DHYEY KIRITBHAI'}, {'21BEIT30045': 'LADANI KEYURKUMAR ASHVINBHAI'}, {'21BEIT30046': 'LAKHANI AKSHI CHANDULAL'}, {'21BEIT30047': 'LATHIYA YASH DAKUBHAI'}, {'21BEIT30048': 'Madi Priyanshu chandresh'}, {'21BEIT30049': 'MAKWANA TIRTHSIH BHARATSINH'}, {'21BEIT30050': 'MARADIA VISHVA NARENDRABHAI'}, {'21BEIT30051': 'MARVANIYA HARSHKUMAR SANJAYBHAI'}, {'21BEIT30052': 'Masot karnkumar chetanbhai'}, {'21BEIT30053': 'MEHTA KARINA VAISHALI'}, {'21BEIT30054': 'MISTRI HEET RAMESHBHAI'}, {'21BEIT30056': 'MITRA SELLY SUDHIRKUMAR'}, {'21BEIT30057': 'NAKRANI SRUSHTIBEN ATULBHAI'}, {'21BEIT30059': 'NAYEE VIVEKKUMAR DASHARATHBHAI'}, {'21BEIT30060': 'PAGHDAR NANDANIBEN VINODBHAI'}, {'21BEIT30061': 'Panchal Palkan Nileshbhai'}, {'21BEIT30062': 'PANCHAL PRITESHKUMAR SHAILESHBHAI'}, {'21BEIT30065': 'PANSURIYA NIRBHAYKUMAR NARESHBHAI'}, {'21BEIT30067': 'Parghi Dhvani Chandrakant'}, {'21BEIT30068': 'PARMAR DEVANSHI ASHOKBHAI'}, {'21BEIT30069': 'PARMAR DHRUVKUMAR MAGANBHAI'}, {'21BEIT30070': 'PARMAR RIDDHI PRAVINBHAI'}, {'21BEIT30071': 'PATEL AERIN BHARATBHAI'}, {'21BEIT30072': 'Patel Aryan Navneetbhai'}, {'222SBEIT30001': 'KRIMA BHARATBHAI BHATT'}, {'222SBEIT30004': 'PARTH SHAILESHKUMAR JOSHI'}, {'222SBEIT30006': 'MEVADA NISHANT D'}, {'222SBEIT30012': 'PRAJAPATI AKSHIT MAHESHKUMAR'}, {'222SBEIT30013': 'SANKET RAMPARIYA'}, {'222SBEIT30014': 'Raval Nishith Vijaybhai '}, {'222SBEIT30017': 'SOLANKI UMANG'}, {'222SBEIT30018': 'MEGHA TRIVEDI'}]
def inserting(enno, name, img):
    enno = enno.upper()
    temp = Insert(enno, name, img)
    if temp != None:
        return True


def empty_database(request):
    try:
        register.objects.all().delete()
        Emptying()
        messages.success(request, "Database cleared successfully.")
    except Exception as e:
        messages.error(request, f"Error clearing database: {str(e)}")
    return redirect("CA_home")


def CA_home(request):
    context = {"page": "Admin", "color": "info"}

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        en_no = data.get("en_no")
        img = request.FILES.get("image")
        img_str = str(img)
        if name == "" or en_no == "" or img_str == "None":
            messages.success(request, "Missing Field's")
            context.update({"color": "danger"})
            return render(request, "CA_index.html", context)
        # elif im.what():
        #     messages.success(request, "Image is not valid")
        #     context.update({"color": "danger"})
        #     return render(request, "CA_index.html", context)

        if register.objects.filter(en_no=en_no).exists():
            messages.success(request, "Enrollment number is Primary Key in DB")
            context.update({"color": "danger"})
            return render(request, "CA_index.html", context)
        # for dict in data:
        #     for key, value in dict.items():
        #         print(key,value)
        # if inserting(str(key),str(value)):
        elif inserting(en_no, name, img):
            messages.success(request, "Data Submitted")
            context.update({"color": "success"})
            # print('inserted')
    return render(request, "CA_index.html", context)
