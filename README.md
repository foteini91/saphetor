# Saphetor project
## How to run
Under /saphetor run: python3 manage.py runserver

## How to use
We use the VCF file which is under saphetor_api/data/output.
You can try it with Postman request tool:
### Below are some examples of the basic endpoints:
##### GET: 127.0.0.1:8000/saphetor/data/?page=1&limit=100
#
headers: 'Accept' : "\*/\*" | "application/json" | "application/xml"
         'If-None-Match' : None | user's input

```sh
    {
    "resources": {
        "previous_page": null,
        "next_page": 2,
        "data": [
            {
                "CHROM": "chr1",
                "POS": 12783,
                "ID": "rs62635284",
                "REF": "G",
                "ALT": "A"
            },
            ...,
            {
                "CHROM": "chr1",
                "POS": 13116,
                "ID": "rs62635286",
                "REF": "T",
                "ALT": "G"
            }]}
    }
    Response header: 'ETAG':hash_key
```
##### GET: http://127.0.0.1:8000/saphetor/data/?id=rs62635284
#
```sh
    {
    "resources": {
        "previous_page": null,
        "next_page": null,
        "data": [
            {
                "CHROM": "chr1",
                "POS": 12783,
                "ID": "rs62635284",
                "REF": "G",
                "ALT": "A"
            }
        ]
    }
    }
```
##### POST: 127.0.0.1:8000/saphetor/add_records/
#
body: [{"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G",
            "ID": "rs77"}]
headers: Authorization {predifined_token}

```sh
    "Invalid token" (403) or (201) in success
```
##### PUT: 127.0.0.1:8000/saphetor/update_record/?id=rs77
#
body: {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G",
"ID": "rs123488888888"}
headers: Authorization {predifined_token}
```sh
    "id does not exist" (404) or (200) in successfull update
```
##### DELETE: 127.0.0.1:8001/saphetor/delete_record/?id=rs1896666666
#
headers: Authorization {predifined_token}
```sh
    "Invalid token" (403) or (201) in successful deletion
```
## How to test
#
run python3 manage.py test saphetor_api/tests/
#
#
# Thanks for reading!