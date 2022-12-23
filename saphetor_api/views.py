from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from .generic_authorization import generic_auth
import json
from .pagination import paginate
from .processing import Processing

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

@api_view(["DELETE"])
def delete_vcf_data(request):
    
    filename= f'{dir_path}/data/output'
    if generic_auth(request) == "Unauthorized": return Response("Invalid token" , status=403) 
    
    id = request.GET.get("id")  

    processing = Processing()
    msg = processing.delete_data_from_file(id, 
                                        filename,                                         
                                        ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"])

    return Response("id does not exist" , status=404) if msg== "EMPTY_DELETION" else Response("successfull update" ,status=204)


@api_view(["PUT"])
def update_vcf_data(request):
    filename= f'{dir_path}/data/output'
    if generic_auth(request) == "Unauthorized": return Response("Invalid token" , status=403) 
    
    id = request.GET.get("id")  
    body = json.loads(request.body)

    processing = Processing()
    msg = processing.update_data_in_file(id, 
                                        filename, 
                                        body ,
                                        ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"])
    return Response("id does not exist" , status=404) if msg== "EMPTY_UPDATE" else Response("successfull update" ,status=200)


@api_view(["POST"])
def post_vcf_data(request):
    filename= f'{dir_path}/data/output'
    if generic_auth(request) == "Unauthorized": return Response("Invalid token" , status=403) 
    body = json.loads(request.body)
    processing = Processing()
    processing.add_json_to_file(filename , 
                                body, 
                                ["CHROM" ,"POS","ID","REF","ALT"])

    return Response(status=201)

@api_view(["GET"])
@renderer_classes([JSONRenderer, XMLRenderer])
def get_vcf_data(request):  

    filename= f'{dir_path}/data/output'
    page = request.GET.get("page")
    limit = request.GET.get("limit")
    id = request.GET.get("id")
    hash_key  = str(hash((page,limit,id)))
    if_none_match = request.headers.get("If-None-Match",None)

    if if_none_match:
        if if_none_match == hash_key:
            return Response(status=304)

    processing = Processing()
    records_list = processing.read_vcf_file(filename, ["CHROM", "POS", "ID", "REF","ALT"] ,id )

    if records_list == []:
        return Response("no records with this id", status=404)

    if request.headers['Accept'] in ["*/*" , "application/json"]:
        mydata = {"resources": paginate(records_list, page, limit)}
        return Response(mydata, headers={'ETAG':hash_key} )
    elif request.headers['Accept'] in ["application/xml"]:
        return Response({"resources": paginate(records_list, page, limit)}, headers={'ETAG':hash_key})
    else:
        return Response("invalid accept headers", status=406)