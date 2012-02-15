from django.shortcuts import render_to_response

def unsupport_ie(f):
    def wrap(request,*args,**kwargs):
        if "MSIE" in request.META["HTTP_USER_AGENT"]:
            return render_to_response("dammit.html",{},RequestContext(request))
        else:
            return f(request,*args,**kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
    
