# from django.shortcuts import render

# def cesium_map(request):
#     return render(request, 'cesium_map.html')


from django.shortcuts import render

def map_view(request):
    return render(request, 'cesium_map.html')
