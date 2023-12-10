from django.shortcuts import render
import random

# Create your views here.
def root(request):
    context = {
        'is_user_anwser_form':False,
        'is_success':False,
        'is_high':False,
        'is_low':False
    }
    # Check If session already have a random number
    random_number=None
    if "right_number" not in request.session:
        # Create A New Var and save a random number (update random_number)
        random_number = random.randint(1,100)
        # Create Key = right_number and value = var ( random_number )
        request.session["right_number"] = random_number
        # Save
        request.session.save()
    
    #############################################
    #############################################
    ## Start Collect Input From User 
    if request.method == "POST":
        ## Set Vars  ##
        guess_number = int(request.POST.get("guess"))       #get number from user (input html name=guess)
        right_number = request.session["right_number"]
        context['is_user_anwser_form'] = True 
        #################
        ## Check For 1 in 3 Status
        ## Check If Success 
        if guess_number == right_number:
            context['is_success'] = True
            ### Winner
            ### Return Game From Begin And Reset Saved Guess Number
            ## Set Session ##
            # Delete Key , Value from Dict Session
            del request.session['right_number']
            random_number = random.randint(1,100)
            request.session["right_number"] = random_number
            request.session.save()
            ####################
            return render(request,"index.html",context)
        
        if guess_number > right_number:
            print("Too High")
            context['is_high'] = True

        if guess_number < right_number:
            print("Too Low")
            context['is_low'] = True
            # return redirect('/result')
        print(request.POST.get("guess"))
        ## Return For Request.method 'POST'
        return render(request,"index.html",context)
    ## End Of Form
    #############################################
    ## Return For General >> By Default 'GET"
    return render(request,"index.html",context)
