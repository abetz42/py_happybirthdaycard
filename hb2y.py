import base64

_a = "CmVjaWxBIGV2b2wgLHRzZWIgZWh0IGxsQQoKc2Ryb3cgZWNpbiBlcm9tIGVtb3MgLHNkcm93IGVjaW4gZXJvbSAsc2Ryb3cgZWNpbiBlcm9tCgouZWNhZiBydW95IG5vIGVsaW1zIGEgc3lhd2xhIGRuYSB5dGlyZXBzb3JwICxodGxhZWggZG9vZyB1b3kgaHNpdyBldyAwMDEgdHhlbiBlaHQgcm9GCiAheWFkaHRyaWIgaHQwMDEgcnVveSBvdCB0c2ViIGVodCBsbEEKCixib0IgcmFlRA=="
_b= "CiAgICwtLgogICB8IHwKICAgfCAiLS0uICAsLS0uLS4sLS4tLS4gLC0uLS0uICwtLiAsLS4KICAgfCAsLS4gXC8gLC0uIHx8ICwtLiBcfCAsLS4gXHwgfCB8IHwKICAgfCB8IHwgfFwgYC0nIHx8IGAtJyAvfCBgLScgL3wgYC0nIHwKICAgYC0nIGAtJyBgLS0nLSd8IC4tLScgfCAuLS0nICBgLS0uIHwKICAgICAgICAgICAgICAgICB8IHwgICAgfCB8ICAgICAgICB8IHwKICAgICAgICAgICAgICAgICBgLScgICAgYC0nICAgICAgICBgLScKLC0uICAgICBfICAgICAgICwtLiAgLC0uICAgICAgICAsLS4KfCB8ICAgIChfKSAgICAgIHwgfF8gfCB8ICAgICAgICB8IHwKfCAiLS0uICwtLiwtLi0tLnwgIF8pfCAiLS0uICAsLS0iIHwgLC0tLi0uLC0uICwtLgp8ICwtLiBcfCB8fCAsLS4vfCB8ICB8ICwtLiBcLyAsLS4gfC8gLC0uIHx8IHwgfCB8CnwgYC0nIC98IHx8IHwgICB8IHwgIHwgfCB8IHxcIGAtJyB8XCBgLScgfHwgYC0nIHwKIi0nLS0nIGAtJ2AtJyAgIGAtJyAgYC0nIGAtJyBgLS0nLScgYC0tJy0nIGAtLS4gfAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfCB8CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBgLQo="

_m = base64.b64decode(_a).decode("utf-8")[::-1]
_p = base64.b64decode(_b).decode("utf-8")

print()
print()
print(_m)

print()

print(_p)