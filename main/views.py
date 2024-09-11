from django.shortcuts import render

def show_main(request):
    # Data yang akan dikirim ke template
    context = {
        'app_name': 'flihh.market',  # Nama aplikasi
        'name': 'Mohamad Rafli Hidayat',  # Nama
        'class_name': 'PBP A',  # Kelas
    }
    return render(request, 'main.html', context)  # Mengembalikan respons ke template
